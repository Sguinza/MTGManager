import requests
import streamlit as st
import pandas as pd

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

headers = {
    'User-Agent': 'MTGTool'
}

def downloadDB (type):
    
    x = requests.get('https://api.scryfall.com/bulk-data/' + type, headers=headers)
    download_String = x.json()['download_uri']
    response = requests.get(download_String, headers=headers)

    with open ("C:\\temp\\export.json", 'wb') as file:
        file.write(response.content)

st.button("download", on_click=downloadDB, args=["oracle-cards"])