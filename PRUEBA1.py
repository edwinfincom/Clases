import pandas as pd

datos = pd.read_excel("Bootcamp.xlsx")

print(datos)

promedio= datos['EDAD'].mean()
desviación = datos['EDAD'].std()
mediana= datos['EDAD'].median()

print("El promedio es: ",promedio)
print("La desviación estandar es: ",desviación)
print("La mediana es: ", mediana)

estadisticas= datos.describe()
print(estadisticas)

def FuncionEdad(datosLeidosExcel):
    promedio= datos['EDAD'].mean()
    desviación = datos['EDAD'].std()
    mediana= datos['EDAD'].median()
    print("El promedio es: ",promedio)
    print("La desviación estandar es: ",desviación)
    print("La mediana es: ", mediana)

print("Explicación Final")
FuncionEdad(datos)

mensaje="BIENVENIDOS AL BOOTCAMP ʕ•́ᴥ•̀ʔっ"
print(mensaje)