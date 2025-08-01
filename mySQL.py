import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",          
    password="zb67hr6N=?c4",    
    database="sabadoJulio"
)
cursor = db.cursor()

query = "SELECT * FROM persona"

try:
    cursor.execute(query)
    resultados = cursor.fetchall()  
    print("Datos de la tabla estudiantes:")
    for row in resultados:
        print(row)

except pymysql.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    db.close()