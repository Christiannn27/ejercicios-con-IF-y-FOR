#Area de un tringulo

print("PROGRAMA PARA SABER EL AREA DE 3 TRIANGULOS")

for i in range(3):
    x = float(input("Digita la base del triangulo: "))
    y = float(input("Digita la altura del triangulo: "))
    
    if x > 0:
        if y > 0:
            area = (x * y) / 2
            print("El area del triangulo es: ", area)
        else:
            print("La altura debe ser mayor a 0")
    else:
        print("La base debe ser mayor a 0")