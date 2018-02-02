import random

def gen_experimentos(n):
    experimentos = []

    for i in range(n):
        e = {
            "Tiempo": 10 * i,
            "Temperatura": random.uniform(0, 60),
            "PH": random.uniform(0, 7),
            "Fallido": random.choice(["SI", "NO"])
        }
        
        experimentos.append(e)

    return experimentos

def gen_personas(n, m):
    nombres = ["Ana", "Beto", "Juan", "Maria", "Quique"]
    apellidos = ["Esparza", "Medoza", "Juarez", "Diaz", "Bojorges", "Lara"]

    personas = []

    for i in range(n):

        p = {
            "nombre": "{} {}".format(random.choice(nombres), random.choice(apellidos)),
            "edad": random.randint(18, 70),
            "experimentos": gen_experimentos(m)
        }

        personas.append(p)

    return personas

import json

f = open("d.txt", "w")

f.write("{}".format(gen_personas(100, 10)))

f.close()