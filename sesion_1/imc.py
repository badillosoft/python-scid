peso = 80
estatura = 1.72

imc = peso / (estatura ** 2)

if imc < 20:
    print("Bajo de peso")
elif imc >= 20 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 27:
    print("Sobrepeso I")
elif imc >= 27 and imc < 29:
    print("Sobrepeso II")
else:
    print("Sobrepeso III")