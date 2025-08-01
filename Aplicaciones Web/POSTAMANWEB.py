from flask import Flask, jsonify,request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

ListaPersonas=[]

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

@app.route('/AgregarPersona',methods=['POST'])
def agregar():
    NuevaPersona= request.json.get('persona')
    ListaPersonas.append(NuevaPersona)
    return "Se agrego una nueva persona"

@app.route('/datosBase',methods=['GET'])
def datosBase():
    cursor.execute("SELECT * FROM persona")
    resultadosPersonas = cursor.fetchall()
    return jsonify(resultadosPersonas)

if __name__ == '__main__':
   app.run(debug=True)