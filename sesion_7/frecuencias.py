# -*- coding: utf-8 -*-

d = {}

for i in range(ord("a"), ord("z") + 1):
    d[chr(i)] = 0

text = open("corpus_spa.1.txt", "r").read().lower()

letters = list(text)

for l in letters:
    if l in d:
        d[l] += 1
    else:
        d[l] = 1

print(d)

x = []

for k in d:
    x.append((k, d[k]))

print(x)

x.sort(key=lambda tup: tup[1])
# sorted(x, key=lambda tup: tup[1])

print(x)