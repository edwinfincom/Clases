import pandas as pd

ListaDestinos = ["Bucaramanga","Amazonas","Cali","Medellin","Villa de Leyva","Quindio","Santa Marta","San Andres y Providencia","Bogota","Cartagena"]

def PorVisitar(destinos):
    for ciudad in destinos:
        if ciudad =="Bucaramanga":
         print("Falta visitar",ciudad)
        elif ciudad =="Amazonas":
         print("Falta visitar",ciudad)
        elif ciudad =="Cali":
         print("Falta visitar",ciudad)
        elif ciudad == "San Andres y Providencia":
         print("Falta visitar",ciudad)
        else:
           print("Destinos Visitados",ciudad)

PorVisitar(ListaDestinos)

numeros = [20,43,10,9]
print(numeros)

def NumerosPor10(ListaDeNumeros):
    for numero in ListaDeNumeros:
      print(numero*10)

NumerosPor10(numeros)