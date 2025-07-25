# Vanesa Carballido : capacitación Python-flask 

_Proyecto:_

Utilicé una API (Pokemón) en Flask y con Python cree los endpoints para utilizarlos en Postman, luego cree el contenedor Docker.

_________________________________

## 💚  ¿Qué hace mi proyecto de Horoscopo Pokemón? 

✨ Calcula, según tu fecha de nacimiento, tu signo del Zodíaco y te asigna el Pokemón que corresponde al mismo.

✨ Crea lista para cada usuario (registrado) de sus Pokemones favoritos, puede agregar, eliminar, buscar Pokemones dentro de la misma o agregar usuarios nuevos.

✨ Puede buscar Pokemones según su tipo (en inglés por la API), por su nombre o ambas opciones, en caso de elegir ambas se retorna el Pokemon y todos los Pokemones del tipo ingresados juntos en una lista.

✨ Calcula un Pokemón y una canción de One Direction del día para el usuario ingresado.

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
Base: http://0.0.0.0:5000

### _GET:_ 

🌸 _/pokemon_:  devuelve una lista con el pokemon ingresado, todos los Pokemones del tipo ingresado o ambas unidas.

⇨ body: {"pokemon":"nombrePokemon", ""tipo":"tipoPokemones"} (opcional al menos uno)

🌸 _/favoritos_ : devuelve la lista de favoritos del usuario ingresado, con nombre de los pokemones e id de cada uno.

⇨ body: {"usuario":"nombre"} 

🌸 _/favoritos/id_ : devuelve la información del Pokemón.

⇨ body: {"usuario":"nombre","id":"idDelPokemonFavorito"}

🌸 _/cancion_ : te asgina un pokemon y una canción del dia utilizando el horoscopo.

⇨ body: {"usuario":"nombre", "fecha": "yyyy-mm-dd"}

### _POST_

🌸 _/favoritos_ : guarda un Pokemón a tu lista de favoritos. 

⇨ body: ("usuario":"nombre", "pokemon":"nombreDelPokemon") 

🌸 _/horoscopo_ : calcula el Pokemón que sos según tu día de nacimiento y tu signo zodiacal. 

⇨ body: ("usuario,": "nombre","fecha":"yyyy-mm-dd")

### _DELETE:_

🌸 _/favoritos_ : elimina el Pokemón de tu lista de favoritos.

⇨ body: {"usuario":"nombre", "id":"idDelPokemonFavorito"}

