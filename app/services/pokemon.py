import requests

URL = "https://pokeapi.co/api/v2"

def existePokemon(nombre: str) -> bool:
    try:
        respuesta = requests.get(f"{URL}/pokemon/{nombre.lower()}")
        return respuesta.status_code == 200
    except:
        return False

def obtenerPokemon(nombre: str) -> dict:
    nombre = nombre.lower()
    respuesta = requests.get(f"{URL}/pokemon/{nombre}")
    respuesta.raise_for_status()
    data = respuesta.json()
    return {
        "Nombre": data["name"],
        "Imagen": data["sprites"]["front_default"],
        "Tipo": [t["type"]["name"] for t in data["types"]],
        "Altura": data["height"],
        "Peso": data["weight"],
        "Habilidades": [h["ability"]["name"] for h in data["abilities"]]
    }

def pokemonesDelTipo(tipo: str) -> list:
    respuesta = requests.get(f"{URL}/type/{tipo.lower()}")
    respuesta.raise_for_status()
    return [p["pokemon"]["name"] for p in respuesta.json()["pokemon"]]
