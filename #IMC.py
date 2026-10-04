# IMC

for i in range(1, 4):
    print("--- Persona", i, "---")
    n = input("Digite su nombre: ")
    p = float(input("Digite su Peso en Kg: "))
    a = float(input("Digite su Altura en Metros: "))

    imc = p / (a ** 2)

    if imc < 18.5:
        print(n, "Su IMC es de", round(imc, 2), "y esta en Bajo Peso")
    elif imc < 25:
        print(n, "Su IMC es de", round(imc, 2), "y esta en Peso Normal")
    elif imc < 30:
        print(n, "Su IMC es de", round(imc, 2), "y esta en Sobrepeso")
    else:
        print(n, "Su IMC es de", round(imc, 2), "y esta en Obesidad")