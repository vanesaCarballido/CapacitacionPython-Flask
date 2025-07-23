import requests
URL= "https://pokeapi.co/api/v2/" #URL base de la API pokemon

#Metodos, acá se van a ingresar y buscar en la URL de la API pokemon.

#existePokemon: controla si el nombre del pokemon es válido o no, para casos de error:
def existePokemon(nombre: str)->bool:
    existe= requests.get(f"{URL}/pokemon/{nombre.lower()})")
    return existe.status_code ==200

#obtenerPokemon: devuelve el pokemon con el nombre ingresado y sus datos:
def obtenerPokemon(nombre:str)->dict:
    nombre=nombre.lower()
    respuesta= existePokemon(nombre)
    respuesta.raise_for_status()
    data= respuesta.json()
    return{"Nombre": data["name"],
           "Imagen": data["sprites"][front_default], 
           "Tipo":[t["type"]["name"] for t in data["types"]],
           "Altura":data["height"],
           "Peso": data["weight"],
           "Habilidades": [h["ability"]["name"]for h in data["abilities"]]
    }


#pookemonesDelTipo: devuelve todos los pokemones de un mismo tipo ingresado
def pokemonesDelTipo(tipo: str)->list:
    respuesta= requests.get(f"{URL}/type/{tipo.lower()}")
    respuesta.raise_for_status()
    return [p["pokemon"]["name"] for p in respuesta.json()["pokemon"]]
                                                                                                        