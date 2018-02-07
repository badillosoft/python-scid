import re
import math

def get_words(text):
    words = []
    for m in re.finditer("\w+", text):
        word = m.group(0)
        words.append(word)
    return words

def sim_cos(w1, w2):
    x = list(w1)
    y = list(w2)
    # print("x: {}\ny: {}".format(x, y))
    u = list(map(lambda c: ord(c), x))
    v = list(map(lambda c: ord(c), y))
    k = min(len(u), len(v))
    n = max(len(u), len(v))
    for i in range(k, n):
        if i >= len(u):
            u.append(0)
        if i >= len(v):
            v.append(0)
    # print("u: {}\nv: {}".format(u, v))
    d = 0
    for i in range(n):
        d += float(u[i] * v[i])
    nu = 0
    nv = 0
    for i in range(n):
        nu += u[i] ** 2.
        nv += v[i] ** 2.
    nu = nu ** 0.5
    nv = nv ** 0.5
    # print("{} {} {} {}".format(d, nu, nv, d / (nu * nv)))
    ct = d / (nu * nv)
    return ct


comida = ["pizza", "hamburguesa", "hot dog", "refresco"]
viaje = ["viaje", "vuelo", "reservacion", "taxi", "playa"]
fiesta = ["cerveza", "peda", "beber", "borracho", "alcohol", "chela", "amigo", "fria"]

f = open("messages.txt", "r")

messages = f.read().split("*")

# print(messages)

for message in messages:
    words = get_words(message)
    # print(words)

print(sim_cos("hola", "holi"))