from flask import Flask, jsonify,request,send_file
from flask_cors import CORS
import pymysql.cursors
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
import matplotlib
matplotlib.use('Agg')
app = Flask(__name__)
CORS(app)

ListaPersonas=[]
resultadosPersonas =[]

db = pymysql.connect(
    host="localhost",
    user="root",          
    password="zb67hr6N=?c4",
    database="sabadoJulio"
)
cursor = db.cursor(pymysql.cursors.DictCursor)

@app.route('/mensaje',methods=['GET'])
def mensaje():
    return 'Primera aplicación Web'

@app.route('/ListaPersonas',methods=['GET'])
def listar():
    return jsonify(ListaPersonas)
#Listar
@app.route('/datosBase',methods=['GET'])
def datosBase():
    cursor.execute("SELECT * FROM persona")
    resultadosPersonas = cursor.fetchall()
    return jsonify(resultadosPersonas)
#Agregar
@app.route('/AgregarPersona',methods=['POST'])
def agregar():
    NuevaPersona= request.json.get('persona')
    ListaPersonas.append(NuevaPersona)
    cursor.execute('INSERT INTO persona(identificacion,edad,nombre) values (%s, %s, %s)',
                   (NuevaPersona['identificacion'], NuevaPersona['edad'],NuevaPersona['nombre']))
    db.commit()
    return "Se agrego una nueva persona"
#Buscar
@app.route('/BuscarPersonas/<identificacion>', methods=['GET'])
def buscar(identificacion):
    cursor.execute("SELECT * FROM persona WHERE identificacion = %s",(identificacion,))
    resultadosPersonas =cursor.fetchall()
    return jsonify(resultadosPersonas)
#Actualizar
@app.route('/ActualizarPersonas/<identificacion>', methods=['PUT'])
def actualizar(identificacion):
    datos_nuevos = request.json
    cursor.execute("UPDATE persona SET nombre=%s, edad=%s WHERE identificacion=%s",
                   (datos_nuevos['nombre'], datos_nuevos['edad'], identificacion))
    db.commit()
    return "Persona Actualizada"

#Eliminar
@app.route('/EliminarPersonas/<identificacion>', methods=['DELETE'])
def eliminar(identificacion):
    cursor.execute('DELETE FROM persona WHERE identificacion=%s',
    (identificacion,))
    db.commit()
    return "Persona Eliminada"

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