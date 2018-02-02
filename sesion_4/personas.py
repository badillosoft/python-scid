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

def obtener_hombres(personas):
    hombres = [] # creo una lista para guardar a los hombres
    for p in personas: # itero cada persona de la lista personas
        if p["sexo"] == "H": # pregunto si la persona (que es un diccionario) en su clave sexo es "H"
            hombres.append(p) # agrego la persona a mi lista de hombres
    return hombres # devuelvo la lista de hombres

def obtener_mujeres(personas):
    mujeres = [] # creo una lista para guardar a los hombres
    for p in personas: # itero cada persona de la lista personas
        if p["sexo"] == "M": # pregunto si la persona (que es un diccionario) en su clave sexo es "H"
            mujeres.append(p) # agrego la persona a mi lista de hombres
    return mujeres # devuelvo la lista de hombres

print("-" * 120)
print(obtener_hombres(personas))

print("-" * 120)
print(obtener_mujeres(personas))

def obtener_edad_0_20(personas):
    sujetos=[]
    for persona in personas :
        if persona["edad"]>=0 and persona["edad"]<=20:
            sujetos.append(persona)
    return sujetos

a=obtener_edad_0_20(personas)
print(len(a))
