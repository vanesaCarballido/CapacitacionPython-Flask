from datetime import date

Signos = [
    ("Aries",        (date(2004, 3, 21), date(2004, 4, 19))),
    ("Tauro",        (date(2004, 4, 20), date(2004, 5, 20))),
    ("Géminis",      (date(2004, 5, 21), date(2004, 6, 20))),
    ("Cáncer",       (date(2004, 6, 21), date(2004, 7, 22))),
    ("Leo",          (date(2004, 7, 23), date(2004, 8, 22))),
    ("Virgo",        (date(2004, 8, 23), date(2004, 9, 22))),
    ("Libra",        (date(2004, 9, 23), date(2004, 10, 22))),
    ("Escorpio",     (date(2004, 10, 23), date(2004, 11, 21))),
    ("Sagitario",    (date(2004, 11, 22), date(2004, 12, 21))),
    ("Capricornio",  (date(2004, 12, 22), date(2005, 1, 19))),
    ("Acuario",      (date(2004, 1, 20), date(2004, 2, 18))),
    ("Piscis",       (date(2004, 2, 19), date(2004, 3, 20)))
]

SignosPokemon = {
    "Cáncer": "psyduck",
    "Escorpio": "lapras",
    "Piscis": "squirtle", 
    "Tauro": "diglett",
    "Virgo": "cubone",
    "Capricornio": "wooper",
    "Aries": "charmander",
    "Leo": "ponyta",
    "Sagitario": "numel",
    "Géminis": "pidgey",
    "Libra": "zubat",
    "Acuario": "natu"
}

def calculoHoroscopoPokemon(fecha: str) -> tuple:
    fechaArreglo = date.fromisoformat(fecha)
    fechaNueva = fechaArreglo.replace(year=2004)
    for signo, (inicio, fin) in Signos:
        if inicio <= fechaNueva <= fin:
            return signo, SignosPokemon.get(signo)
    return None
