#potencia de 3 numeros 

for i in range(1, 4):
    numero = int(input("Escriba un numero: "))
    potencia = numero ** 2
    porcentaje = (potencia * 60) / 100

    print("la potencia del numero es: ", potencia)

    if potencia > 50:
        print("el porcentaje del numero es: ", porcentaje)
    else:
        print("La potencia es muy baja para mostrar el porcentaje")