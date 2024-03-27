import requests
import json
from requests.structures import CaseInsensitiveDict

def test_put(path:str='/', port=5000, data:dict[str, str]= {}) -> tuple[bool, dict]:
    try:
        headers = CaseInsensitiveDict()
        headers['Content-Type'] = 'application/json'
        test = requests.put( f'http://localhost:{port}{path}', headers=headers, data=json.dumps(data))
        return (test.status_code == 200, json.loads(test.text))
    except:
        return "Echec"

def test_get(path:str='/', port=5000, data:dict[str, str]= {}) -> tuple[bool, dict]:
    try:
        headers = CaseInsensitiveDict()
        headers['Content-Type'] = 'application/json'
        test = requests.get( f'http://localhost:{port}{path}', headers=headers, data=json.dumps(data))
        return (test.status_code == 200, json.loads(test.text))
    except:
        return "Echec"

def test_post(path:str='/', port=5000, data:dict[str, str]= {}) -> tuple[bool, dict]:
    try:
        headers = CaseInsensitiveDict()
        headers['Content-Type'] = 'application/json'
        test = requests.post( f'http://localhost:{port}{path}', headers=headers, data=json.dumps(data))
        return (test.status_code == 200, json.loads(test.text))
    except:
        return "Echec"

def test_delete(path:str='/', port=5000, data:dict[str, str]= {}) -> tuple[bool, dict]:
    try:
        headers = CaseInsensitiveDict()
        headers['Content-Type'] = 'application/json'
        test = requests.delete( f'http://localhost:{port}{path}', headers=headers, data=json.dumps(data))
        return (test.status_code == 200, json.loads(test.text))
    except:
        return "Echec"

def test_athlete():
    print("\n[ATHLETE]\n")
    # Test GET /athlete
    print("=======GET=======")
    for id in [1, 437]:
        print(test_get(f'/athlete/{id}', 8081))

    # Test GET /athlete/findByName
    print("=======GET byName=======")
    print(test_get('/athlete/findByName/', 8081, {'name':"Thierry"}))

    # Test GET /athlete/findBySurname
    print("=======GET bySurname=======")
    print(test_get('/athlete/findBySurname/', 8081, {"surname":"LeClou"}))

    # Test PUT /athlete
    print("=======PUT=======")
    for couleur, id in zip(["bronze","silver"], [2, 4370]):
        print(test_put('/athlete/', 8081, {"athlete_id": id,
                                    "name": "Louison",
                                    "surname": "Prudhomme"
                                    }))

    # Test POST /athlete
    print("=======POST=======")
    for couleur, id in zip(["bronze","silver"], [2, 437]):
        print(test_post('/athlete/', 8081, {"athlete_id": id,
                                    "name": "Louison",
                                    "surname": "Prudhomme"
                                    }))
        
    # Test DELETE /athlete
    print("=======DELETE=======")
    for id in [1, 2, 3]:
        print(test_delete(f'/athlete/{id}', 8081))

def test_medal():
    print("\n[MEDAL]\n")
    # Test GET /medal
    print("=======GET=======")
    for id in [1, 437]:
        print(test_get(f'/medal/{id}', 8080))

    # Test GET /medal/findBySport
    print("=======GET SPORT=======")
    print(test_get('/medal/findBySport/', 8080, {'sport_id':38}))

    # Test GET /medal/findByYear
    print("=======GET YEAR=======")
    print(test_get('/medal/findByYear/', 8080, {'year':2005}))

    # Test GET /medal/findByAthlete
    print("=======GET ATHLETE=======")
    print(test_get('/medal/findByAthlete/', 8080, {'athlete_id':14}))

    # Test PUT /medal
    print("=======PUT=======")
    for couleur, id in zip(["bronze","silver"], [2, 4370]):
        print(test_put('/medal/', 8080, {"medal_id": id,
                                    "year": 2004,
                                    "color": couleur,
                                    "athlete_id": 14,
                                    "sport_id": 37
                                    }))

    # Test POST /medal
    print("=======POST=======")
    for couleur, id in zip(["bronze","silver"], [2, 437]):
        print(test_post('/medal/', 8080, {"medal_id": id,
                                    "year": 2004,
                                    "color": couleur,
                                    "athlete_id": 14,
                                    "sport_id": 37
                                    }))
        
    # Test DELETE /medal
    print("=======DELETE=======")
    for id in [1, 2, 3]:
        print(test_delete(f'/medal/{id}', 8080))

def test_sport():
    print("\n[SPORT]\n")

    # Test GET /sport
    print("=======GET=======")
    for id in [4, 12]:
        print(test_get(f'/sport/{id}', 8082))

    # Test GET /sport/findByName
    print("=======GET byName=======")
    print(test_get('/sport/findByName/', 8082, {'name':"rugby"}))

    # Test PUT /sport
    print("=======PUT=======")
    for name, id in zip(["rugby","football"], [2, 4370]):
        print(test_put('/sport/', 8082, {"sport_id": id,
                                        "name": name,
                                        "category": "sports collectifs",
                                        "finalData": "17/12/2028"
                                        }))

    # Test POST /sport
    print("=======POST=======")
    for name, id in zip(["rugby","football"], [2, 4370]):
        print(test_post('/sport/', 8082, {"sport_id": id,
                                        "name": name,
                                        "category": "sports collectifs",
                                        "finalData": "17/12/2028"
                                        }))
        
    # Test DELETE /sport
    print("=======DELETE=======")
    for id in [1, 2, 3]:
        print(test_delete(f'/sport/{id}', 8082))

test_athlete()
test_sport()
test_medal()
