import json
import os

def read_json(): #aqui se esta crendo una funcion para leer un archivo json
    if not os.path.isfile('salchicha.json'): #busca el archivo json
        with open('salchicha.json','w') as f: #esta linea de codigo y la que sigue es para crear un archivo json si no hay un archivo json 
            json.dump([],f)
    with open('salchicha.json','r') as f: #estas lineas finales son para leer el archivo json
        info= json.load(f)
    return info