# Capacitación Python-flask 

🌸 Vanesa Carballido 🌸 

_Proyecto:_

Utilicé una API (Pokemón) en Flask y con Python cree los endpoints para utilizarlos en Postman, luego cree el contenedor Docker.

_________________________________

## 💚  ¿Qué hace mi proyecto de Horoscopo Pokemón? 

✨ Calcula, según tu fecha de nacimiento, tu signo del Zodíaco y te asigna el Pokemón que corresponde al mismo.

✨ Crea lista para cada usuario (registrado) de sus Pokemones favoritos, puede agregar, eliminar, buscar Pokemones dentro de la misma o agregar usuarios nuevos.

✨ Puede buscar Pokemones según su tipo (en inglés por la API), por su nombre o ambas opciones, en caso de elegir ambas se retorna el Pokemon y todos los Pokemones del tipo ingresados juntos en una lista.

✨ Calcula un Pokemón y una canción de One Direction del día ingresado para el usuario ingresado.

_______________

## 💙 Ejecución con Docker:

-Instalar Flask

-Escribir "docker-compose up --build" en la consola

Al terminar los pasos la consola tendría que mostrar esto y el Docker ejecutarse correctamente

<img width="500" height="165" alt="Captura de pantalla 2025-07-24 212336" src="https://github.com/user-attachments/assets/76a8a345-794c-4aae-9f44-eeab26a15ee9" />

__________________________
## 💜 Ejecución por consola:
-Clonar repositorio

-Instalar Flask

-Activar el venv

-Escribir "python -m app.main" en la consola

Se tendría que mostrar esto al terminar todos los pasos:

<img width="500" height="400" alt="Captura de pantalla 2025-07-24 182831" src="https://github.com/user-attachments/assets/d7af8a44-c96c-4c39-a62e-eefb0dfa16b1" />

## Uso de endpoints en postman:
#GET /pokemon: busca el pokemon segun nombre, tipo o ambos y devuelve una lista con todos 
#(pokemon, tipo) 
#GET /favoritos/id: devuelve el pokemon favorito según id 
#(usuario, id)
#GET /favoritos: despliega la lista de favoritos con su nombre e id 
#(usuario)
#DELETE /favoritos: borrar un pokemon de la lista de favoritos 
#(usuario, id)
#POST /favoritos: guarda un pokemon a tu lista de favoritos 
#(usuario, pokemon) 

#GET /cancion: devuelve tu nombre, un pokemon del dia y una cancion de One Direction del dia 
# (usuario,fecha)
#POST /horoscopo: calcula el pokemon que sos segun tu dia de nacimiento, tu signo zodiacal 
#(usuario, fecha)
_GET:_ 
/

_POST_

_DELETE:_
