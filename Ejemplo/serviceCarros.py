from flask import Flask, request, jsonify
import math
from ObjetoCarro import Carro
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'uptc2025'  
jwt = JWTManager(app)

carros = []

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == "edwin" and password == "uptc":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"mensaje": "Credenciales incorrectas"}), 401


@app.route('/listaCarros', methods=['GET'])
@jwt_required()
def lista_carros():
    carro1 = Carro("Mazda","2017","1233","Blanco")
    carro2 = Carro("Renault","2009","4523","Beige")
    carros.append(carro1.to_json())
    carros.append(carro2.to_json())
    return jsonify(carros)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)