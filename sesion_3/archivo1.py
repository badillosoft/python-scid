f = open("diario.txt", "r")

content = f.read()

f.close()

print(content)

print(type(content))

print(len(content))