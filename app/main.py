from flask import Flask, request, jsonify
from datetime import datetime

from app.services.horoscopos import calculoHoroscopoPokemon
from app.services.pokemon import obtenerPokemon, existePokemon, pokemonesDelTipo

app = Flask(__name__)

favoritos = {}
idProximo = 1

@app.route("/horoscopo", methods=["POST"])
def PostHoroscopo():
    datos = request.get_json() or {}
    usuario = datos.get("usuario", "").strip()
    fecha = datos.get("fecha", "").strip()

    if not usuario:
        return jsonify({"error": "Falta ingresar el nombre"}), 400
    if not fecha:
        return jsonify({"error": "Falta ingresar la fecha"}), 400

    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido"}), 400

    resultado = calculoHoroscopoPokemon(fecha)
    if not resultado:
        return jsonify({"error": "No se pudo calcular el horóscopo"}), 400

    signo, nombrePokemon = resultado
    try:
        ficha = obtenerPokemon(nombrePokemon)
    except:
        return jsonify({"error": "Error al obtener los datos del Pokémon"}), 500

    return jsonify({
        "usuario": usuario,
        "signo": signo,
        "pokemon": ficha
    })


@app.route("/favoritos", methods=["POST"])
def PostGuardarFavorito():
    global idProximo
    datos = request.get_json() or {}
    usuario = datos.get("usuario", "").strip()
    pokemon = datos.get("pokemon", "").strip()

    if not usuario:
        return jsonify({"error": "Falta ingresar el usuario"}), 400
    if not pokemon:
        return jsonify({"error": "Falta ingresar el nombre del pokemon"}), 400
    if not existePokemon(pokemon):
        return jsonify({"error": "El nombre del pokemon no existe"}), 404

    favorito = {"id": idProximo, "nombre": pokemon}
    if usuario not in favoritos:
        favoritos[usuario] = []
    favoritos[usuario].append(favorito)
    idProximo += 1

    return jsonify({f"favoritos de {usuario}": favoritos[usuario]})


@app.route("/favoritos", methods=["DELETE"])
def DeleteFavorito():
    datos = request.get_json() or {}
    usuario = datos.get("usuario", "").strip()
    id_str = datos.get("id", "").strip()

    if usuario not in favoritos:
        return jsonify({"error": "Usuario no encontrado"}), 404

    try:
        idBusqueda = int(id_str)
    except ValueError:
        return jsonify({"error": "El id debe ser un número"}), 400

    antes = len(favoritos[usuario])
    favoritos[usuario] = [f for f in favoritos[usuario] if f["id"] != idBusqueda]
    eliminado = len(favoritos[usuario]) < antes

    return jsonify({"eliminado": eliminado})


@app.route("/favoritos", methods=["GET"])
def GetListaFavoritos():
    datos = request.get_json() or {}
    usuario = datos.get("usuario", "").strip()

    if not usuario:
        return jsonify({"error": "Tenés que ingresar el usuario"}), 400
    if usuario not in favoritos:
        return jsonify({"error": "No tenés lista de favoritos"}), 404

    return jsonify({"favoritos": favoritos[usuario]})


@app.route("/favoritos/id", methods=["GET"])
def GetFavoritoPorID():
    datos = request.get_json() or {}
    usuario = datos.get("usuario", "").strip()
    id_str = datos.get("id", "").strip()

    if not usuario or not id_str:
        return jsonify({"error": "Faltan datos"}), 400
    if usuario not in favoritos:
        return jsonify({"error": "Usuario no encontrado"}), 404

    try:
        idBusqueda = int(id_str)
    except ValueError:
        return jsonify({"error": "El id debe ser un número"}), 400

    for fav in favoritos[usuario]:
        if fav["id"] == idBusqueda:
            return jsonify({"resultado": fav})

    return jsonify({"error": f"No se encontró el Pokémon con id {idBusqueda}"}), 404


@app.route("/pokemon", methods=["GET"])
def GetBuscarPokemon():
    datos = request.get_json() or {}
    pokemon = datos.get("pokemon", "").strip()
    tipo = datos.get("tipo", "").strip()

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


if __name__ == "__main__":
    print(" Iniciando en http://127.0.0.1:5000")
    app.run(debug=True)
