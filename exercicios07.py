import json
import os

Data = ('data.json')

def carregar_dados():
    if os.path.exists(Data):
        with open(Data, 'r', encoding= 'utf-8') as arq_json: 
            return json.load(arq_json)
    else:
        return []
    
clientes = carregar_dados()

for cliente in clientes:
    print(clientes ['nome_completo'])
