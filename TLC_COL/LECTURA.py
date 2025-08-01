import pandas as pd
from flask import Flask, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Por si accedes desde otro origen

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/datos')
def obtener_datos():
    df = pd.read_excel('TLC COL - UNIÓN EUROPEA.xlsx')
    datos = df.to_dict(orient='records')
    return jsonify  (datos)

if __name__ == '__main__':
    app.run(debug=True)

