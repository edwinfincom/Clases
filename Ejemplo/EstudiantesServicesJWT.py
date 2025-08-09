from flask import Flask, request, jsonify
import math
from EstudianteGestion import EstudianteEjemplo
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'uptc2025'  
jwt = JWTManager(app)

personas = []
animales = []
carros = []
estudiantes = []


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

  
    if username == "jorge" and password == "uptc":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"mensaje": "Credenciales incorrectas"}), 401


@app.route('/listaEstudiantes', methods=['GET'])
@jwt_required()
def lista_estudiantes():
    estudiante = EstudianteEjemplo("1","Jorge","23")
    estudiantes.append(estudiante.to_json())
    return jsonify(estudiantes)

@app.route('/crearEstudiante', methods=['POST'])
@jwt_required()
def crear_estudiante():
    data = request.get_json()
    nombre = data.get('nombre')
    codigo = data.get('codigo')
    promedio = data.get('promedio')

    estudiante = EstudianteEjemplo(nombre, codigo, promedio)
    estudiantes.append(estudiante.to_json())

    return jsonify({"mensaje": "Estudiante creado exitosamente"}), 201

@app.route('/obtenerEstudiante/<codigo>', methods=['GET'])
@jwt_required()
def obtener_estudiante(codigo):
    estudiante = next((e for e in estudiantes if e['codigo'] == codigo), None)

    if estudiante is not None:
        return jsonify(estudiante), 200
    else:
        return jsonify({"mensaje": "Estudiante no encontrado"}), 404

@app.route('/actualizarEstudiante/<codigo>', methods=['PUT'])
@jwt_required()
def actualizar_estudiante(codigo):
    data = request.get_json()
    estudiante = next((e for e in estudiantes if e['codigo'] == codigo), None)

    if estudiante is not None:
        estudiante['nombre'] = data.get('nombre', estudiante['nombre'])
        estudiante['promedio'] = data.get('promedio', estudiante['promedio'])

        return jsonify({"mensaje": "Estudiante actualizado exitosamente"}), 200
    else:
        return jsonify({"mensaje": "Estudiante no encontrado"}), 404

@app.route('/eliminarEstudiante/<codigo>', methods=['DELETE'])
@jwt_required()
def eliminar_estudiante(codigo):
    global estudiantes
    estudiantes = [e for e in estudiantes if e['codigo'] != codigo]

    return jsonify({"mensaje": "Estudiante eliminado exitosamente"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
