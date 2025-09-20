import requests
from bs4 import BeautifulSoup

url = "https://decatolicos.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    registros = soup.find_all('h1') 

    print("=== TODOS LOS ENLACES ENCONTRADOS ===\n")
    for i, h1 in enumerate(registros, start=1):
        texto = h1.get_text(strip=True)
        #href = h1.get('href')
        if texto:
            print(f"{i}. Texto: {texto}")

except requests.exceptions.RequestException as e:
    print(f"Error al acceder a la página: {e}")
