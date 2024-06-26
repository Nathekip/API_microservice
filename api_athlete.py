from flask import Flask, render_template, request, jsonify
import json

api_jo = Flask(__name__)

def get_json(database:str) -> dict[str, str]:
    try:
        with open(f'{database}.json','r',encoding='utf-8') as file:
            dico = json.load(file)
    except FileNotFoundError:
        print(f"{database}.json not found")
        return {"erreur": f"{database}.json not found"}
    except json.JSONDecodeError:
        return {'erreur':f"{database}.json empty"} 
    return dico

@api_jo.route("/", methods=['GET'])
def menu():
    return '<br>'.join([f'<a href="/{branche}">{branche}</a>' for branche in ('medal', 'sport', 'athlete')])

@api_jo.route("/athlete/", methods = ['PUT', 'POST','GET'])
def athlete():
    dico_athlete = get_json('athletes')
    if request.method == 'PUT':
        data = request.get_json()
        id = data["athlete_id"]
        if str(id) not in dico_athlete.keys():
            return jsonify(dico_athlete), 400
        if data:
            dico_athlete[str(id)] = data
            with open('athletes.json', 'w', encoding='utf-8') as file:
                json.dump(dico_athlete, file)
        return jsonify(dico_athlete)
    if request.method == 'POST':
        try:
            data = request.get_json()
            id = data["athlete_id"]
            if data:
                dico_athlete[str(id)] = data
                with open('athletes.json', 'w', encoding='utf-8') as file:
                    json.dump(dico_athlete, file)
            return jsonify(dico_athlete)
        except:
            return jsonify(dico_athlete), 400
    return jsonify(dico_athlete)

@api_jo.route("/athlete/<int:athleteId>", methods = ['GET', 'DELETE'])
def athlete_athleteId(athleteId:int):
    dico_athlete = get_json('athletes')
    if request.method == 'DELETE':
        if str(athleteId) not in dico_athlete.keys():
            return jsonify(dico_athlete), 400
        dico_athlete = {key:value for key,value in dico_athlete.items() if str(athleteId) != key}
        with open('athletes.json', 'w', encoding='utf-8') as file:
            json.dump(dico_athlete, file)
    return jsonify(dico_athlete)

@api_jo.route("/athlete/findByName/", methods = ['GET'])
def athlete_findByName():
    dico_athlete = get_json('athletes')
    data = request.get_json()
    name = data["name"]
    print(dico_athlete.values())
    if name not in [line["name"] for line in dico_athlete.values()]:
        return jsonify(dico_athlete), 400
    athletes = [x for x in dico_athlete.values() if x["name"] == name]
    athlete = athletes[0] if len(athletes) == 1 else athletes
    return jsonify({"athlete":athlete}), 200

@api_jo.route("/athlete/findBySurname/", methods = ['GET'])
def athlete_findBySurname():
    dico_athlete = get_json('athletes')
    data = request.get_json()
    surname = data["surname"]
    print(dico_athlete.values())
    if surname not in [line["surname"] for line in dico_athlete.values()]:
        return jsonify(dico_athlete), 400
    athletes = [x for x in dico_athlete.values() if x["surname"] == surname]
    athlete = athletes[0] if len(athletes) == 1 else athletes
    return jsonify({"athlete":athlete}), 200

if __name__ == '__main__':
    api_jo.run(port=5000, host="0.0.0.0")
