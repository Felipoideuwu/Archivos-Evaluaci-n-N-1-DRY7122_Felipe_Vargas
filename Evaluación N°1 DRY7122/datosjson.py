import json
import datetime
import os

os.system ("clear")

try:
    with open('/home/devasc/labs/devnet-src/parsing/myfile.json') as x:
        json_file = json.load(x)
    token = json_file["access_token"]
    expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=json_file["expires_in"])
    time_left = expiration_time - datetime.datetime.now()
    print("Token: {}".format(token))
    print("Tiempo restante: {}".format(time_left))
except FileNotFoundError:
    print("El archivo no está.")
except json.JSONDecodeError:
    print("El archivo JSON no es válido.")
except KeyError:
    print("El archivo JSON no contiene el campo 'access_token'.")
