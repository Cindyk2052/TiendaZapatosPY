#METODO BURBUJA
#PARA LISTAS PEQUEÑAS

lista = [4,8,100,10,11,25,3,3.5,0.25, 0] # Creamos una lista de 9 elementos
num = len(lista)

# Imprimimos la lista obtenida al principio (Desordenada)
print("El vector a ordenar es:", lista)
    
for i in range(num-1): 
    # Le damos un rango n para que complete el proceso. 
    for j in range(0, num-i-1): 

        # Revisa la matriz de 0 hasta n-i-1
        if lista[j] > lista[j+1] :
            lista[j], lista[j+1] = lista[j+1], lista[j]
        # Se intercambian si el elemento encontrado es mayor 
        # Luego pasa al siguiente

print ("El vector ordenado es: ",lista)