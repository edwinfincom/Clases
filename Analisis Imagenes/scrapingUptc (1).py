import requests
from bs4 import BeautifulSoup
import re

url = "https://es.wikipedia.org/wiki/Universidad_Pedag%C3%B3gica_y_Tecnol%C3%B3gica_de_Colombia"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    registros = soup.find_all('td') 

    print("=== TODOS LOS ENLACES ENCONTRADOS ===\n")
    for i, td in enumerate(registros, start=1):
        texto = td.get_text(strip=True)
        #href = td.get('href')
        if texto and re.match(r'^Licenciatura', texto, re.IGNORECASE):
            print(f"{i}. Texto: {texto}")

except requests.exceptions.RequestException as e:
    print(f"Error al acceder a la página: {e}")
