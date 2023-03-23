
puntosJugadorA=[[0,0,0],[0,0,0],[0,0,0]]
puntosJugadorB=[[0,0,0],[0,0,0],[0,0,0]]

#Recorre una matriz y pinta sus valores
def pintarMatriz(matriz):
    #Recorrer una matriz
    for fila in range(len(matriz)):
        #Recorre cada fila
        print("Fila numero",fila,matriz[fila])
        for columna in range(len(matriz[fila])):
            #recorre las columnas
            print("En la posicion", fila+1, columna+1, "el valor es:", matriz[fila][columna])
    print("")

def pintarMatrizV2(matriz):
    #Recorrer una matriz
    for fila in range(len(matriz)):
        #Recorre cada fila
        for columna in range(len(matriz[fila])):
            #recorre las columnas
            print(matriz[fila][columna],end=" ")
        print("\n")
    print("")

#Escribir los valores de la matriz

def llenarMatriz(matriz):
    print("matriz inicial", matriz)
    #Recorrer una matriz
    for fila in range(len(matriz)):
        #Recorre cada fila
        for columna in range(len(matriz[fila])):
            valor = input ("Ingrese un valor de la posicion "+str(fila+1)+","+str(columna+1)+": ")
            matriz[fila][columna]=valor
    return matriz

#Llamar a la funcion
matrizResultado = llenarMatriz(puntosJugadorA)

#Pintar la matriz
pintarMatriz(matrizResultado)
                             
#Llamar a la funcion
matrizResultado = llenarMatriz(puntosJugadorB)

#Pintar la matriz
pintarMatriz(matrizResultado)

