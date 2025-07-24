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

SignosPokemon= {
    "Cáncer": "psyduck",
    "Escorpio": "lapras",
    "Piscis": "squirtle", 
    "Tauro": "diglett",
    "Virgo": "cubone",
    "Capricornio": "wooper",
    "Aries": "charmander",
    "Leo": "numel",
    "Sagitario": "ponyta",
    "Géminis": "pidgey",
    "Libra": "zubat",
    "Acuario": "natu"
    }

SignosCanciones={
    "Cáncer": "What Makes You Beautiful",
    "Escorpio":"Story of My Life",
    "Piscis":"Drag Me Down",
    "Tauro":"Little Things",
    "Virgo":"Steal My Girl",
    "Capricornio":"One Thing",
    "Aries":"Night Changes",
    "Leo":"Live While We're Young",
    "Sagitario":"No Control",
    "Géminis":"Best Song Ever",
    "Libra":"Perfect",
    "Acuario":"History",
    }

#Calcula la fecha arreglada para que se pueda utilizar en el calculo de signos y luego en signosPokemon
def calculoHoroscopoPokemon(fecha: str) ->tuple:
    fechaFormaBien= date.fromisoformat(fecha)
    fechaArreglada = fechaFormaBien.replace(year=2004)
    for signo, (inicio, fin) in Signos:
        if inicio <= fechaArreglada <= fin:
            return signo, SignosPokemon.get(signo)
    return None

