#--------------------EJERCICIO Tienda de Zapatos OPCION 1-----------------------------

#Creación de Menú 

# print("BIENVENIDO A PAYLESSS SHOES \n\n")

# print("MENÚ DE PRECIOS \n")
# print("1. Compra de hasta 2 pares de zapatos")
# print("2. Compra de 3 a 10 pares de zapatos")
# print("3. Compra más de 10 pares de zapatos")

# opcion = int(input("\nIngrese el número de opción: "))

# if opcion == 1:
#     print("\nEl cliente debe pagar el precio completo de los pares de zapatos\n")

# elif opcion == 2:
#     print("\nTIPO DE DESCUENTO")
#     print("a. Tarjeta de descuento")
#     print("b. SIN tarjeta de descuento")
#     opcion2 = input("\nIngrese la letra de su opción: ")
    
#     if opcion2 == "a" or opcion2 == "A":
#         print("\nUsted tiene un descuento del 12% en su compra\n")
#     else:
#         print("\nUsted tiene un descuento del 5% en su compra\n")

# elif opcion == 3:
#     print("\nSe debe consultar al gerente para realizar el descuento\n")

# else: 
#     print("Error en el valor ingresado")

#--------------------EJERCICIO Tienda de Zapatos OPCION 2-----------------------------

print("----TIPOS DE DESCUENTO----\n")

numShoes = int(input("Ingrese la cantidad de pares de zapatos a comprar: "))

if numShoes <= 2:
    print("\nEl cliente debe pagar el precio completo de los pares de zapatos\n")
elif numShoes >= 3 and numShoes <= 10:
    respuesta = input("\n¿El cliente cuenta con tarjeta de descuento? (S/N): ")
    if respuesta == "S" or respuesta == "s":
        print("\nUsted tiene un descuento del 12% en su compra\n")
    else:
        print("\nUsted tiene un descuento del 5% en su compra\n")
else:
    print("\nSe debe consultar al gerente para realizar el descuento\n")





