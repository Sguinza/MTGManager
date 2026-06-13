import requests
import streamlit

headers = {
    'User-Agent': 'MTGTool',
    'From': 'cguinda00@gmail.com'  # This is another valid field
}

x = requests.get('https://api.scryfall.com/bulk-data/oracle-cards', headers=headers)
download_String = x.json()['download_uri']

response = requests.get(download_String, headers=headers)

with open ("export.json", 'wb') as file:
    file.write(response.content)