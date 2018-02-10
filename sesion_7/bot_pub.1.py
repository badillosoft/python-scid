import re

freq = {}

for i in range(ord("a"), ord("z") + 1):
    freq[chr(i)] = 0

text = open("corpus_spa.1.txt", "r").read().lower()

letters = list(text)

for l in letters:
    if l in freq:
        freq[l] += 1
    else:
        freq[l] = 1

def sim_cos(w1, w2):
    x = list(w1)
    y = list(w2)
    u = list(map(lambda c: ord(c) - ord("a") + freq[c] + 1, x))
    v = list(map(lambda c: ord(c) - ord("a") + freq[c] + 1, y))
    if len(u) > len(v):
        d = len(u) - len(v)
        for i in range(d):
            v.append(0)
    elif len(v) > len(u):
        d = len(v) - len(u)
        for i in range(d):
            u.append(0)
    # print("{} / {}".format(u, v))
    d = 0; nu2 = 0; nv2 = 0
    for i in range(len(u)):
        d += u[i] * v[i]
        nu2 += u[i] ** 2
        nv2 += v[i] ** 2
    nu = nu2 ** 0.5
    nv = nv2 ** 0.5
    ct = d / (nu * nv)
    return ct

def get_words(text):
    words = []
    for m in re.finditer("\w+", text):
        w = m.group(0)
        words.append(w.lower()) # upper()
    return words

def normalize(x, a, b):
    return float(x - a) / (b - a) * 100

comida = ["comer", "beber", "pizza", "hambre"]
viaje = ["volar", "taxi", "reservar", "fiesta"]
fiesta = ["fiesta", "reventon", "chela"]

text = "quiero una pizza"

words = get_words(text)

print(words)

for wu in words:
    for wx in comida:
        if sim_cos(wu, wx) >= 0.97:
            print("Sugiere Comida [{}/{}]".format(wu, wx))
    for wx in viaje:
        if sim_cos(wu, wx) >= 0.97:
            print("Sugiere Viaje [{}/{}]".format(wu, wx))
    for wx in fiesta:
        if sim_cos(wu, wx) >= 0.97:
            print("Sugiere Fiesta [{}/{}]".format(wu, wx))
        