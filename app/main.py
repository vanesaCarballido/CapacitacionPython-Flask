from flask import Flask, request, jaonify
from datetime import datetime
from app.services.horoscopos import calculoHoroscopoPokemon #para poder usar el metodo
from app.services.pokemon import obtenerPokemon, existePokemon,pokemonesDelTipo

app= Flask(__name__)

#Horoscopo pokemon: metodo POST atributos (usuario, fecha)
@app.route("/horoscopo", methods=["Post"])
def PostHoroscopo():
    datos= request.get_json() or {}
    usuario= datos.get("usuario","").strip() #strip elimina espacios en blanco
    fecha= datos.get("fecha","").strip()

    if not usuario or not fecha:
        if not usuario:
            return jsonify({"Falta ingresar el nombre"})
        if not usuario:
            return jsonify({"Falta ingresar la fecha"})
    else:
        try: 
            fecha.datetime,strptime(fecha, "%Y-%m-%d").date

        except: 
            return jsonify ({"Formato de fecha inválido"})
    pokemonHoroscopo=calculoHoroscopoPokemon(fecha)
    if not pokemonHoroscopo:
        return ({"Ha ocurrido un error al buscar el pokemón"})
    else:
        try:
            fichaPokemon= obtenerPokemon(pokemonHoroscopo)
        except:
            return jsonify({"Pokemon no valido"})
        
    return jsonify({"Usuario": usuario, "Signo": pokemonHoroscopo ,"Pokemón": fichaPokemon})


#Favoritos: agregar, eliminar y buscar
favoritos={}
idProximo=1

#Guardar favoritos:  metodo POST atributos (usuario, pokemon)
@app.route("/favoritos", methods=["POST"])
def PostGuardarFavorito():
    global idProximo
    datos= request.get_json() or {}
    usuario= datos.get("usuario",""),strip()
    pokemon= datos.get("pokemon",""),strip()
    if not user:
        return jsonify({"Falta ingresar el usuario"})
    if not pokemon:
        return jsonify({"Falta ingresar el nombre del pokemon"})
    if not existePokemon(pokemon):
        return jsonify ({"El nombre del pokemon no existe"})
    favorito= {"id":idProximo, "nombre":pokemon}
    favoritos.setdefault(user,[].append(favorito))
    idProximo+=1
    return jsonify ({"SLa lista de ", usuario ,"se ha actualizado:" ,favoritos[usuario]})


#Eliminar favorito: metodo DELETE, atributos (usuario, id)
@app.route("/favoritos", methods=["DELETE"])
def DeleteFavorito():
    datos= request.get_json() or {}
    usuario= datos.get("usuario",""),strip()
    id= datos.get("id",""),strip()
    if usuario not in favoritos:
        return jsonify({False}),404
    antes=len(favoritos[usuario])
    favoritos[usuario]=[f for f in favoritos[usuario] if ["id"]!= id]
    return jsonify({len(favoritos[usuario]<antes)}) #si es menor que antes entonces e eliminó correctamente


#Listar los favoritos: metodo GET, atributos (usuario)
@app.route("/favoritos", methods=["DELETE"])
def GetListaFavoritos():
    datos= request.get_json() or {}
    usuario= datos.get("usuario",""),strip()
    if usuario not in favoritos:
        return jsonify({"No tenes lista de favoritos"}) 
    if not usuario:
        return jsonify({"Tenes que ingresar el usuario"})
    return jsonify({"Los favoritos de", usuario, "son: ", favoritos[usuario]})


#Buscar entre los favoritos: metodo GET, atributos (usuario, id)


#Buscar pokemon: metodo GET, atributos (uno opcional) (pokemon, tipo)
 
    
    
        

