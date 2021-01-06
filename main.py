from flask import Flask, request
from waitress import serve
import requests
import json
import werkzeug

app = Flask(__name__)
#GET 1
@app.route('/mobiteli/marka/<put_id>')
def get_1(put_id):
    mobitel_id = int(put_id)
    if mobitel_id <= len(mobiteli) or not 0:
        found_phone = None
        for mobitel in mobiteli:
            found_phone = mobitel if mobitel.get('PkMobitel') == mobitel_id else found_phone

        if found_phone:
            response = {
                "status": "OK",
                "message": "Fetch succesfull.",
                "reponse": {
                    "id": put_id,
                    "Marka": found_phone.get('Marka'),
                    "links": [
                        {
                            "href": put_id + "/marka",
                            "rel": "marka",
                            "type": "GET"
                        }
                    ]
                }
            }
            return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')
    ex_response = {
        'status':'Not founud',
        'message': 'Not found', 
        'response': None
    }
    return app.response_class(response=json.dumps(ex_response), status=404, mimetype='application/json')

#GET2
@app.route('/mobiteli/Naziv/<marka_id>')
def get_2(marka_id):
    phone_id = str(marka_id)
    found_phone = None
    for mobitel in mobiteli:
        found_phone = mobitel if mobitel.get('PkMobitel') == mobitel_id else found_phone 
    
    if found_phone == None:
        ex_response = {
            'status':'Not found',
            'message': 'Not found', 
            'response': None
        }
        return app.response_class(status=404, response=json.dumps(ex_response), mimetype='application/json')
    naziv = request_params.get('Naziv')
    response = {
        "status": "OK",
        "message": "Fetch succesfull.",
        "reponse": {
            "Marka": marka_id,
            "Naziv": found_phone.get('Naziv'),
            "links": [
                {
                "href": marka_id + "/" + marka_id,
                "rel": "naziv",
                "type": "GET"
                }
            ]   
        }
    }
    return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')
   
#GET3
@app.route('/mobiteli/boje/<put_id>')
def get_3(put_id):
    mobitel_id = int(put_id)
    if mobitel_id <= len(mobiteli) or not 0:
        found_phone = None
        for mobitel in mobiteli:
            found_phone = mobitel if mobitel.get('PkMobitel') == mobitel_id else found_phone
        if found_phone:    
            response = {
        "status": "OK",
        "message": "Fetch succesfull.",
        "reponse": {
            "PkMobitel": put_id,
            "Boje": found_phone.get('Boje'),
            "links": [
                {
                "href": put_id + "/boje" ,
                "rel": "boje",
                "type": "GET"
                }
            ]
        }
    }
            return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')
        ex_response = {
        'status':'Not founud',
        'message':'Not found', 
        'response': None
    }
    return app.response_class(response=json.dumps(ex_response), status=404, mimetype='application/json')

#GET 4
@app.route('/mobiteli/datum/<naziv_id>')
def get_4(naziv_id):
    phone_id = str(naziv_id)
    found_phone = None
    for mobitel in mobiteli:
        found_phone = mobitel if mobitel.get('Naziv') == mobitel_id else found_phone 
    
    if found_phone == None:
        ex_response = {
            'status':'Not founud',
            'message':'Not found', 
            'response': None
        }
        return app.response_class(status=404, response=json.dumps(ex_response), mimetype='application/json')
    response = {
        "status": "OK",
        "message": "Fetch succesfull.",
        "reponse": {
            "Naziv": naziv_id,
            "DatumIzdanja": found_phone.get('DatumIzdanja'),
            "links": [
                {
                "href": naziv_id + "/datum" ,
                "rel": "datum",
                "type": "GET"
                }
            ]
        }
    }
    return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')
      
#GET5
@app.route('/mobiteli/naziv/<put_id>')
def get_5(put_id):
    mobitel_id = int(put_id)
    if mobitel_id <= len(mobiteli) or not 0:
        found_phone = None
        for mobitel in mobiteli:
            found_phone = mobitel if mobitel.get('PkMobitel') == mobitel_id else found_phone
        if found_phone:    
            response = {
            "status": "OK",
            "message": "Fetch succesfull.",
            "reponse": {
                "id": put_id,
                "Naziv": found_phone.get('Naziv'),
                "links": [
                    {
                    "href": put_id + "/naziv",
                    "rel": "naziv",
                    "type": "GET"
                    }
                ]
            }
        }
            return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')
        ex_response = {
        'status':'Not founud',
        'message': 'Not found', 
        'response': None
    }
    return app.response_class(response=json.dumps(ex_response), status=404, mimetype='application/json')

#POST endpoint
@app.route('/mobiteli/post', methods=['POST'])
def post_mobile():
    ex_response = {
        'status':'Invalid input',
        'message': 'Invalid json', 
        'response': None
    }
    try:
        request_params = request.get_json()
    except:
        return app.response_class(status=400, response=json.dumps(ex_response), mimetype='application/json')
    
    marka = request_params.get('Marka')
    naziv = request_params.get('Naziv')
    datum = request_params.get('DatumIzdanja')
    dimenzije = request_params.get('Dimenzije')
    boje = request_params.get('Boje')
    rezolucija = request_params.get('Rezolucija')
    os = request_params.get('OS')
    kamera = request_params.get('Kamera')
    zvucnik = request_params.get('Zvucnik')
    cijena = request_params.get('Zvucnik')
    blt = request_params.get('Bluetooth')
    wlink = request_params.get('Wikilink')

    if not marka or not naziv or not datum or not dimenzije or not datum or not dimenzije or not boje or not rezolucija or not os or not kamera or not zvucnik or not cijena or not blt or not wlink:
        ex_response = {
            'status':'Invalid input',
            'message': 'A resource is missing', 
            'response': None
        }
        return app.response_class(status=400, response=json.dumps(ex_response), mimetype='application/json')

    new_mobile = {
        'PkMobitel': len(mobiteli) + 1,
        'Marka': marka,
        'Naziv': naziv,
        'DatumIzdanja': datum,
        'Dimenzije': dimenzije,
        'Boje': boje,
        'Rezolucija': rezolucija,
        'OS': os,
        'Kamera': kamera,
        'Zvucnik': zvucnik,
        'Cijena': cijena,
        'Bluetooth': blt,
        'Wikilink': wlink
    }

    mobiteli.append(new_mobile)
    response = {
        'status':'OK',
        'message':'Posted succesfully',
        'response': new_mobile
    }
    return app.response_class(status=200, response=json.dumps(response), mimetype='application/json')

#PUT endpoint
@app.route('/mobiteli/dimenzije/<put_id>', methods=['PUT'])
def put_dimenzije(put_id):
    ex_response = {
        'status':'Invalid input',
        'message': 'Invalid json', 
        'response': None
    }
    try:
        request_params = request.get_json()
    except:
        return app.response_class(status=400, response=json.dumps(ex_response), mimetype='application/json')
   
    tezina = request_params.get('Tezina')
    mjere = request_params.get('Mjere')
    if not tezina or not mjere:
        ex_response = {
            'status':'Invalid input',
            'message': 'A resource is missing', 
            'response': None
        }
        return app.response_class(status=400, response=json.dumps(ex_response), mimetype='application/json')

    found_index = None
    for mobitel in mobiteli:
        found_index = mobiteli.index(mobitel) if mobitel.get('PkMobitel') == int(put_id) else found_index

    if found_index is not None:
        mobiteli[found_index]['Tezina'] = tezina
        mobiteli[found_index]['Mjere'] = mjere    
        response = {
            "status":"OK",
            "message":"Put resource",
            "response": {
                "id": put_id,
                "Tezina":tezina,
                "Mjere":mjere,
                "links": [{
                    "href":put_id + "/Dimenzije", 
                    "rel": "dimenzije",
                    "type":"PUT"
                }]
            }
        }
        return app.response_class(status=200, response=json.dumps(response), mimetype='application/json')
    ex_response = {
        "status": "Invalid input",
        "message": "Invalid resources",
        "response": None
    }
    return app.response_class(status=400, response=json.dumps(ex_response), mimetype='application/json') 

#DELETE endpoint
@app.route('/mobiteli/delete/<put_id>', methods=['DELETE'])
def delete_resource(put_id):
    found_index = None
    for mobitel in mobiteli:
        found_index = mobiteli.index(mobitel) if mobitel.get('PkMobitel') == int(put_id) else found_index

    if found_index is not None:
        mobiteli.pop(found_index)
        return app.response_class(status = 204, response = json.dumps({}), mimetype = 'application/json')
    
    ex_response = {
        'status':'Not founud',
        'message': 'Not found', 
        'response': None
    }
    return app.response_class(status = 404, response = json.dumps(ex_response), mimetype='application/json')
    
#501 handler
@app.errorhandler(werkzeug.exceptions.NotImplemented)
def handle_not_implemented(e):
    response = e.get_response()
    response.data = json.dumps({
        "status":"Not Implemented",
        "message":"Method not implemented for requested resource",
        "response": None
    })
    response.content_type = "application/json"
    return response

#Main
if __name__ == "__main__":
    global mobiteli
    url = 'https://raw.githubusercontent.com/ViktorijaSml/Release/main/mobiteli.json'
    mob = requests.get(url, headers={'Content-Type':'application/json'})
    mobiteli = mob.json()
    serve(app, host="0.0.0.0", port=9040)  
