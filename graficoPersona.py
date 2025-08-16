import matplotlib.pyplot as plt
import pymysql
import pandas as pd
db = pymysql.connect(
    host="localhost",
    user="root",          
    password="zb67hr6N=?c4",    
    database="sabadoJulio" 
)

cursor = db.cursor(pymysql.cursors.DictCursor)
resultadoPersona = []
cursor.execute("SELECT * FROM persona")
resultadoPersona = cursor.fetchall()
print(resultadoPersona)
persona =pd.DataFrame(resultadoPersona)
print(persona)

nombre = ["Camila","Aleja","Manuel"]
edad = [23,34,41]

plt.plot(nombre,edad)
plt.title("Grafico de edad por persona")
plt.show()

plt.bar(nombre,edad)
plt.title("Grafico de barras edad por persona")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.show()

plt.scatter(nombre,edad)
plt.title("Grafico de dispersion edad por persona")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.show()

#ventas por mes

labels = ["Marzo","Abril","Mayo","Junio"]
sizes =[23,56,12,32]

plt.pie(sizes,labels = labels, autopct='%1.1f%%',startangle=90)
plt.title("Grafico de torta de venta por mes")
plt.axis('equal')
plt.show()