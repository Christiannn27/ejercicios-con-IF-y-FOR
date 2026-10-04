#Tablas de multiplicar 

num = int(input("Digite un numero del 1 al 9: "))

if 1 <= num <= 9:
    print("tabla de multiplicar del numero: ", num)
    for i in range(1, 11):
        result = num * i
        print(num, "X", i, "=", result)
else:
    print("Error el número ingresado es incorrecto")