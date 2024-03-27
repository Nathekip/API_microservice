from flask import Flask, render_template, request, jsonify
import json

api_jo = Flask(__name__)

def get_json(database:str) -> dict[str, str]:
    try:
        with open(f'{database}.json','r',encoding='utf-8') as file:
            dico = json.load(file)
    except FileNotFoundError:
        print(f"{database}.json not found")
        return {
                "message": f"{database}.json not found",
                "details": {},
                "description": "The database set does not exist.",
                "code": 1002,
                "http_response": {
                    "message": "We could not find the resource you requested.",
                    "code": 404
                }
            }
    except json.JSONDecodeError:
        print(f"{database}.json vide")
        return {
                "message": f"{database}.json empty",
                "details": {},
                "description": "The database is empty.",
                "code": 1002,
                "http_response": {
                    "message": "The resource you requested was empty.",
                    "code": 404
                }
            }    
    return dico

@api_jo.route("/", methods=['GET'])
def menu():
    return '<br>'.join([f'<a href="localhost:{port}/{branche}">{branche}</a>' for port, branche in zip([5000, 5001, 5002], ['medal', 'sport', 'athlete'])])

@api_jo.route("/sport/", methods = ['PUT', 'POST','GET'])
def sport():
    dico_sport = get_json('sports')
    if request.method == 'PUT':
        data = request.get_json()
        id = data["sport_id"]
        if str(id) not in dico_sport.keys():
            return jsonify(dico_sport), 400
        if data:
            dico_sport[str(id)] = data
            with open('sports.json', 'w', encoding='utf-8') as file:
                json.dump(dico_sport, file)
        return jsonify(dico_sport)
    if request.method == 'POST':
        try:
            data = request.get_json()
            id = data["sport_id"]
            if data:
                dico_sport[str(id)] = data
                with open('sports.json', 'w', encoding='utf-8') as file:
                    json.dump(dico_sport, file)
            return jsonify(dico_sport)
        except:
            return jsonify(dico_sport), 400
    return jsonify(dico_sport)

@api_jo.route("/sport/<int:sportId>", methods = ['GET', 'DELETE'])
def sport_sportId(sportId:int):
    dico_sport = get_json('sports')
    if request.method == 'DELETE':
        if str(sportId) not in dico_sport.keys():
            return jsonify(dico_sport), 400
        dico_sport = {key:value for key,value in dico_sport.items() if str(sportId) != key}
        with open('sports.json', 'w', encoding='utf-8') as file:
            json.dump(dico_sport, file)
    return jsonify(dico_sport)

@api_jo.route("/sport/findByName/", methods = ['GET'])
def sport_findByName():
    dico_sport = get_json('sports')
    data = request.get_json()
    sport_name = data["name"]
    if sport_name not in [line["name"] for line in dico_sport.values()]:
        return jsonify(dico_sport), 400
    sports = [x for x in dico_sport.values() if x["sport_id"] == sport_name]
    sport = sports[0] if len(sports) == 1 else sports
    return jsonify({"sport":sport}), 200

if __name__ == '__main__':
    api_jo.run(port=5000, host="0.0.0.0")
