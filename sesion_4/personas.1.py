def cargar_personas(nombre_archivo):
    f = open(nombre_archivo, "r") # abro el archivo

    f.readline() # ignoro la primer linea

    personas = [] # creo una lista para guardar los datos de las personas

    for linea in f: # leo cada linea restante en el archivo: "Ana,23,M,12000"
        d = linea.split(",") # separo la linea mediante el separador ",": ["Ana", "23", "M", "12000"]
        p = {
            "nombre": d[0], # "Ana"
            "edad": int(d[1]), # 23
            "sexo": d[2], # "M"
            "salario": float(d[3]) # 12000.0
        }
        personas.append(p) # [{ ... }]

    f.close()

    return personas

personas = cargar_personas("datos.csv")

print(personas)

def F_Hombres(p):
    if p["sexo"] == "H":
        return True

def F_Mujeres(p):
    return p["sexo"] == "M"

def F_edad_0_20(p):
    return p["edad"] >= 0 and p["edad"] <= 20

hombres = filter(F_Hombres, personas)
mujeres = filter(F_Mujeres, personas)
sujetos = filter(F_edad_0_20, personas)

hombres2 = filter(lambda p: p["sexo"] == "H", personas)