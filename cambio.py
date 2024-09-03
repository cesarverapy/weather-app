import requests

url = "https://open.er-api.com/v6/latest/PYG"

respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()

    tasa_cambios = datos["rates"]["USD"]

    cantidad_guaranies = float(input("ingrese la cantidad de guaranies que desea convertir a dolares"))

    cantidad_dolares = cantidad_guaranies * tasa_cambios
    print(f"{cantidad_guaranies} PYG = {cantidad_dolares} USD")

else:
    print("error en la solicitud")