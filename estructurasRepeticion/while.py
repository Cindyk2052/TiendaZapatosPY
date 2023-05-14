#--------------------------------WHILE---------------------------------------------------
#Se usa cuando no sabemos el numero de repeticiones que se debe hacer

# x = 0

# while x < 5:
#     x = x + 1 #contador
#     print("Num de vueltas: ", x)
#     print("HOLA MUNDO")
   
#Llenar una lista para n entradas que el usuario quiera
#lista = [] #lista vacia
#parada = "no"

#while parada == "no":
#    lista.append(input("Ingerse un elemento: "))
#    parada = input ("Quiere salir del programa(si/no):")

#print("Lista: ", lista)

#While se usa para realizar repeticiones con una extension
#

#Suma de los n numeros ingresados por el usuario
# suma = 0
# parada = "no"

# while parada == "no":
    
#     numero = int(input("Ingrese un número: ")) #5, 10  #Solo ingrese enteros
#     suma = numero + suma        #0+5 = 5, 15
#     parada = input("Quiere salir del programa (si/no): ") #no, si

# print("Resultado de la suma", suma )

#Multiplicacion de los n numeros ingresados por el usuario
mult = 1
parada = "no"

while parada == "no":
    
    numero = int(input("Ingrese un número: ")) #5, 10  #Solo ingrese enteros
    mult = numero * mult        #0+5 = 5, 15
    parada = input("Quiere salir del programa (si/no): ") #no, si

print("Resultado de la multiplicación", mult )

