#Importar metodos a usar en todo el codigo main:

from flask import Flask, request, jsonify
from datetime import datetime

from app.services.horoscopos import calculoHoroscopoPokemon, SignosCanciones
from app.services.pokemon import obtenerPokemon, existePokemon, pokemonesDelTipo

app = Flask(__name__)

#Global para poder guardar datos (para usar en favoritos)
favoritos = {}
idProximo = 1


#POST /horoscopo: calcula el pokemon que sos segun tu dia de nacimiento, tu signo zodiacal 
#(usuario, fecha)
@app.route("/horoscopo", methods=["POST"])
def PostHoroscopo():
    datos = request.get_json() or {}
    usuario = (datos.get("usuario", "").strip()).lower()
    fecha = datos.get("fecha", "").strip()

    if not usuario:
        if not fecha:
             return jsonify({"error": "Falta ingresar el nombre y la fecha"}), 400
    if not usuario:
        return jsonify({"error": "Falta ingresar el nombre"}), 400
    if not fecha:
        return jsonify({"error": "Falta ingresar la fecha"}), 400
    try:
        fechaValida = datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "El formato de la fecha no es inválido"}), 400
    
    resultado = calculoHoroscopoPokemon(fecha)
    if not resultado:
        return jsonify({"error": "No se pudo calcular el signo del horóscopo"}), 400
    signo, nombrePokemon = resultado
    try:
        ficha = obtenerPokemon(nombrePokemon)
    except:
        return jsonify({"error": "no se han podido obtener los datos del Pokémon"}), 400

    return jsonify({
        "usuario": usuario,
        "signo": signo,
        "pokemon": ficha
    })


#GET /cancion: devuelve tu nombre, un pokemon del dia y una cancion de One Direction del dia 
# (usuario,fecha)
@app.route("/cancion", methods=["GET"])
def GetCancionDe1D():
    datos = request.get_json() or {}
    usuario= (datos.get("usuario","").strip()).lower()
    fecha = datos.get("fecha", "").strip()

    if not fecha:
        return jsonify({"error": "Falta ingresar la fecha"}), 400
    if not usuario:
         return jsonify({"error": "Falta ingresar la fecha"}), 400
    try:
        fechaValida = datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "El formato de la fecha no es válido"}), 400

    resultado = calculoHoroscopoPokemon(fecha)
    if not resultado:
        return jsonify({"error": "No se pudo calcular el signo del horóscopo"}), 400
    signo, nombrePokemon = resultado
    try:
        ficha = obtenerPokemon(nombrePokemon)
    except:
        return jsonify({"error": "No se han podido obtener los datos del Pokémon"}), 400
    cancion = SignosCanciones.get(signo, "Canción no asignada")

    return jsonify({
        "Hola":usuario,
        "Tu Pokemón del dia es": nombrePokemon,
        "Tu canción del dia de One Direction es": cancion
    })

#POST /favoritos: guarda un pokemon a tu lista de favoritos 
#(usuario, pokemon) 
@app.route("/favoritos", methods=["POST"])
def PostGuardarFavorito():
    global idProximo
    datos = request.get_json() or {}
    usuario = (datos.get("usuario", "").strip()).lower()
    pokemon = (datos.get("pokemon", "").strip()).lower()

    if not usuario:
        return jsonify({"error": "Falta ingresar el usuario"}), 400
    if not pokemon:
        return jsonify({"error": "Falta ingresar el nombre del pokemon"}), 400
    if not existePokemon(pokemon):
        return jsonify({"error": "El nombre del pokemon no existe"}), 404
    
    favorito = {"id": idProximo, "nombre": pokemon}
    if usuario not in favoritos:
        favoritos[usuario] = []
    antes = len(favoritos[usuario])
    if pokemon not in [f["nombre"] for f in favoritos[usuario]]:
        favoritos[usuario].append(favorito)
        idProximo += 1
    despues = len(favoritos[usuario])
    if despues > antes:
        return jsonify({
            "mensaje": f"Se ha ingresado correctamente el pokemon {pokemon} a la lista de favoritos de {usuario}"
        })

    return jsonify({
        "mensaje": f"El pokemon {pokemon} ya estaba en la lista de favoritos de {usuario}"
    })


#DELETE /favoritos: borrar un pokemon de la lista de favoritos 
#(usuario, id)
@app.route("/favoritos", methods=["DELETE"])
def DeleteFavorito():
    datos = request.get_json() or {}
    usuario = (datos.get("usuario", "").strip()).lower()
    idPokemon = datos.get("id", "").strip()

    if usuario not in favoritos:
        return jsonify({"error": "Usuario no encontrado"}), 404
    try:
        idBusqueda = int(idPokemon)
    except ValueError:
        return jsonify({"error": "El id debe ser un número"}), 400
    
    antes = len(favoritos[usuario])
    favoritos[usuario] = [f for f in favoritos[usuario] if f["id"] != idBusqueda]
    eliminado = len(favoritos[usuario]) < antes

    return jsonify({"eliminado": eliminado})


#GET /favoritos: despliega la lista de favoritos con su nombre e id 
#(usuario)
@app.route("/favoritos", methods=["GET"])
def GetListaFavoritos():
    datos = request.get_json() or {}
    usuario = (datos.get("usuario", "").strip()).lower()

    if not usuario:
        return jsonify({"error": "Tenés que ingresar el usuario"}), 400
    if usuario not in favoritos:
        return jsonify({"error": "No tenés lista de favoritos"}), 404

    return jsonify({"favoritos": favoritos[usuario]})


#GET /favoritos/id: devuelve el pokemon favorito según id 
#(usuario, id)
@app.route("/favoritos/id", methods=["GET"])
def GetFavoritoPorID():
    datos = request.get_json() or {}
    usuario = (datos.get("usuario", "").strip()).lower()
    idPokemon = datos.get("id", "").strip()

    if not usuario or not idPokemon:
        return jsonify({"error": "Faltan datos"}), 400
    if usuario not in favoritos:
        return jsonify({"error": "Usuario no encontrado"}), 404
    try:
        idBusqueda = int(idPokemon)
    except ValueError:
        return jsonify({"error": "El id debe ser un número"}), 400

    for fav in favoritos[usuario]:
        if fav["id"] == idBusqueda:
            return jsonify({"resultado": fav})

    return jsonify({"error": f"No se encontró el Pokémon con id {idBusqueda}"}), 404

#GET /pokemon: busca el pokemon segun nombre, tipo o ambos y devuelve una lista con todos 
#(pokemon, tipo)
@app.route("/pokemon", methods=["GET"])
def GetBuscarPokemon():
    datos = request.get_json() or {}
    pokemon = ((datos.get("pokemon", "").strip()).lower()).lower()
    tipo = ((datos.get("tipo", "").strip()).lower()).lower()

    if not pokemon and not tipo:
        return jsonify({"error": "Se debe ingresar al menos un dato"}), 400
    if pokemon and tipo:
        try:
            lista = pokemonesDelTipo(tipo)
            if pokemon not in lista:
                lista.append(pokemon)
            return jsonify({"resultado": lista})
        except:
            return jsonify({"error": "Alguno de los datos no es válido"}), 400
        
    if pokemon:
        try:
            return jsonify({"resultado": obtenerPokemon(pokemon)})
        except:
            return jsonify({"error": "El nombre del pokemón no es válido"}), 400
    if tipo:
        try:
            lista = pokemonesDelTipo(tipo)
            return jsonify({"resultado": lista})
        except:
            return jsonify({"error": "El tipo del pokemón no es válido"}), 400


#Puerto
if __name__ == "__main__":
    print(" Iniciando en http://0.0.0.0:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)
