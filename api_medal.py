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

# Medal
@api_jo.route("/medal/", methods = ['PUT', 'POST'])
def medal():
    dico_medal = get_json('medals')
    if request.method == 'PUT':
        data = request.get_json()
        id = data["medal_id"]
        if str(id) not in dico_medal.keys():
            return jsonify(dico_medal), 400
        if data:
            dico_medal[str(id)] = data
            with open('medals.json', 'w', encoding='utf-8') as file:
                json.dump(dico_medal, file)
        return jsonify(dico_medal)
    if request.method == 'POST':
        try:
            data = request.get_json()
            id = data["medal_id"]
            if data:
                dico_medal[str(id)] = data
                with open('medals.json', 'w', encoding='utf-8') as file:
                    json.dump(dico_medal, file)
            return jsonify(dico_medal)
        except:
            return jsonify(dico_medal), 400

@api_jo.route("/medal/<int:medalId>", methods = ['GET', 'DELETE'])
def medal_medalId(medalId:int):
    dico_medal = get_json('medals')
    if request.method == 'DELETE':
        if str(medalId) not in dico_medal.keys():
            return jsonify(dico_medal), 400
        dico_medal = {key:value for key,value in dico_medal.items() if str(medalId) != key}
        with open('medals.json', 'w', encoding='utf-8') as file:
            json.dump(dico_medal, file)
    if str(medalId) not in dico_medal.keys():
        return jsonify(dico_medal), 400
    print(str(medalId))
    return jsonify({"medal":dico_medal[f"{medalId}"]}), 200

@api_jo.route("/medal/findBySport/", methods = ['GET'])
def medal_findBySport():
    dico_medal = get_json('medals')
    data = request.get_json()
    sport_id = data["sport_id"]
    if sport_id not in [line["sport_id"] for line in dico_medal.values()]:
        return jsonify(dico_medal), 400
    medals = [x for x in dico_medal.values() if x["sport_id"] == sport_id]
    medal = medals[0] if len(medals) == 1 else medals
    return jsonify({"medal":medal}), 200

@api_jo.route("/medal/findByYear/", methods = ['GET'])
def medal_findByYear():
    dico_medal = get_json('medals')
    data = request.get_json()
    year = data["year"]
    if year not in [line["year"] for line in dico_medal.values()]:
        return jsonify(dico_medal), 400
    medals = [x for x in dico_medal.values() if x["year"] == year]
    medal = medals[0] if len(medals) == 1 else medals
    return jsonify({"medal":medal}), 200

@api_jo.route("/medal/findByAthlete/", methods = ['GET'])
def medal_findByAthlete():
    dico_medal = get_json('medals')
    data = request.get_json()
    athlete_id = data["athlete_id"]
    if athlete_id not in [line["athlete_id"] for line in dico_medal.values()]:
        return jsonify(dico_medal), 400
    medals = [x for x in dico_medal.values() if x["athlete_id"] == athlete_id]
    medal = medals[0] if len(medals) == 1 else medals
    return jsonify({"medal":medal}), 200

if __name__ == '__main__':
    api_jo.run(port=5000, host="0.0.0.0")
