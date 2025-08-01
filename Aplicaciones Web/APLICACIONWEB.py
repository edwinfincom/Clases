from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/mensaje',methods=['GET'])

def mensaje():
    return 'Primera aplicación Web'
"""
@app.route('/Nombres',methods=['GET'])

def listar():
    Nombres= ['Edwin','Laura','Mateo','Diana']
    return jsonify(Nombres)
"""
@app.route('/ListaPersonas',methods=['GET'])

def listar():
    ListaPersonas= [{"Nombre": "Edwin","Edad": "24","Profesion": "Finanzas"},
    {"Nombre": "Laura","Edad": "23","Profesion": "Finanzas"},                
    {"Nombre": "Mateo","Edad": "34","Profesion": "Economista"}],
    return jsonify(ListaPersonas)

if __name__ == '__main__':
   app.run(debug=True)