# DOLAR A PESO

dolares = int(input("Ingrese la cantidad de dolares a convertir a pesos: "))

for dia in range(1, 4):
    print("--- Dia", dia, "---")
    tasa_cambio = int(input("Ingrese la tasa de cambio (TRM): "))
    pesos = dolares * tasa_cambio
    print("El valor en pesos colombianos (COP) es: $", pesos)
    
    if pesos > 100000:
        print("Es una cantidad alta de pesos")
    else:
        print("Es una cantidad normal de pesos")