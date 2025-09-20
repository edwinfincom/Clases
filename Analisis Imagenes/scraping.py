import requests
from bs4 import BeautifulSoup
import re

query = 'site:latamairlines.com/co/es "vuelo" "precio"'
url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    
    print(f"Status Code: {response.status_code}")    
    print(f"Final URL: {response.url}")
    vuelos = []
    if response.status_code == 200:
        print(response.text[:1000])  

        soup = BeautifulSoup(response.text, 'html.parser')
        
        vuelosObtenidos = []
        for i, result in enumerate(soup.find_all('h3'),start = 1):
            descripcion_vuelo = result.get_text()
            print(" resultado    -->  "+descripcion_vuelo)
            vuelos.append({"descripcion": descripcion_vuelo})
            precio = f"${300 + i * 50}"
            vuelosObtenidos.append({
                "id": i,
                "descripcion": descripcion_vuelo,
                "precio": f"${300 + i * 50}"
            })
        for i in range(len(vuelos)):
            vuelos[i]["precio"] = f"${300 + i * 50}"

        print("Vuelos encontrados:")
        for vuelo in vuelos:
            print(f"Descripción: {vuelo['descripcion']}, Precio: {vuelo['precio']}")

        print("Arreglo de vuelos encontrados:")
        for vueloLATAM in vuelosObtenidos:
            print(f"ID: {vueloLATAM['id']}, Descripción: {vueloLATAM['descripcion']}, Precio: {vueloLATAM['precio']}")
    else:
        print(f"Error: Código de estado {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error al realizar la solicitud: {e}")
finally:
    print("Final")
