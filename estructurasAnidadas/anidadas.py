#Multiplo de un numero (anidacion de estructuras)

num = int(input("Ingrese un número: "))

if num % 2 == 0:
    if num % 5 == 0:
        print(f"El número {num} es múltiplo de 2 y 5")
    else:
        print(f"El número {num} es múltiplo de 2")

if num % 3 == 0:
    if num % 5 == 0:
        print(f"El número {num} es múltiplo de 3 y 5")
    else:
        print(f"El número {num} es múltiplo de 3")