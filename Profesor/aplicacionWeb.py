from flask import Flask, jsonify, request, send_file, send_from_directory
from flask_cors import CORS
import mysql.connector
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
import matplotlib
matplotlib.use('Agg')  


app = Flask(__name__)
CORS(app)
listaPersonas = []
resultadosPersonas = []

db = mysql.connector.connect(
    host="localhost",
    user="root",           
    password="juanESTEBAN10*#",     
    database="sabadoJulio" 
)
cursor = db.cursor(dictionary=True)
#pymysql.cursors.DictCursor

@app.route('/mensaje',methods=['GET'])
def mensaje():
    return 'Primera aplicacion web'

@app.route('/listarPersonas',methods=['GET'])
def listar():
    return jsonify(listaPersonas)

@app.route('/agregarPersona',methods=['POST'])
def agregar():
    nuevaPersona = request.json.get('persona')
    listaPersonas.append(nuevaPersona)
    return 'Se agrego una nueva persona'

@app.route('/datosDeLaBase',methods=['GET'])
def datosBase():
    cursor.execute("SELECT * FROM persona")
    resultadosPersonas = cursor.fetchall() 
    return jsonify(resultadosPersonas)

@app.route('/agregarPersonaBD',methods=['POST'])
def agregarBD():
    nuevaPersona = request.json.get('persona')
    resultadosPersonas.append(nuevaPersona)
    cursor.execute("INSERT INTO persona(identificacion, nombre, edad) VALUES (%s, %s, %s)",
            (nuevaPersona['identificacion'], nuevaPersona['nombre'], nuevaPersona['edad']))
    db.commit()
    return 'Se agrego una nueva persona'

@app.route('/buscarPersona/<identificacion>', methods=['GET'])
def buscar(identificacion):
    cursor.execute("SELECT * FROM persona WHERE identificacion = %s",(identificacion,))
    resultadoPersona = cursor.fetchall() 
    return jsonify(resultadoPersona)

@app.route('/actualizarPersona/<identificacion>', methods=['PUT'])
def actualizar(identificacion):
    datos_nuevos = request.json
    cursor.execute("UPDATE persona SET  nombre=%s,edad=%s WHERE identificacion=%s",
    (datos_nuevos['nombre'], datos_nuevos['edad'],datos_nuevos['identificacion']))
    db.commit()
    return "Persona actualizada"
    
@app.route('/eliminarPersona/<identificacion>', methods=['DELETE'])
def eliminar(identificacion):
    cursor.execute("DELETE FROM persona WHERE identificacion=%s",
    (identificacion,))
    db.commit()
    return "Persona eliminada"

@app.route('/graficoPersona', methods=['GET'])
def graficoLineal():
    nombres = ["Jorge","Alejandra","Luis","Ana"]
    edades = [31,27,28,45]
    plt.figure(figsize=(10, 6))
    plt.plot(nombres,edades)
    plt.title("Grafico de edad por persona")
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    plt.close()
    
    return send_file(img_buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)


