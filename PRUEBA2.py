import pandas as pd

datos = pd.read_excel("Bootcamp.xlsx")

def mostrarDatos(x):
    print(x)

mensajeParaPrueba = "PruebaFuncion"
numero=43
mostrarDatos(mensajeParaPrueba)
mostrarDatos(numero)
mostrarDatos(datos)

def mostrarCuadrado(numero):
    print(numero*numero)

mostrarCuadrado(3)
mostrarCuadrado(8)
mostrarCuadrado(12)

def ACadaNumeroQueIngreseResteDos(numero):
    print(numero-2)

ACadaNumeroQueIngreseResteDos(7)
ACadaNumeroQueIngreseResteDos(65)
ACadaNumeroQueIngreseResteDos(74)