#Funcion de sumar
def sumar(x,y):
    print("Suma")
    resultado = x+y
    print ("La suma es de:", resultado)

#Funcion de restar
def restar (x,y):
    print("Resta")
    resultado = x-y
    print ("La resta es de:", resultado)

#Funcion de multiplicar
def multiplicar (x,y):
    print("Multiplicacion")
    resultado = x*y
    print ("La multiplación es de:", resultado)

#Funcion de dividir
def dividir (x,y):
    print("Divison")
    resultado = a/b
    print ("La division es de:", resultado)

print("Bienvenido al programa")
opcion=1
while opcion !=5:
    print("1. Suma\n2. Resta\n3. Multiplicar\n4. Dividir\n5. Salir")
    opcion=int(input("Seleccione una opcion:"))
    if opcion!=5:
        a=int(input("Primer valor:"))
        b =int(input("Segundo valor:"))
    if opcion==1:
        sumar(a,b)
    elif opcion==2:
        restar(a,b)
    elif opcion==3:
        multiplicar(a,b)
    elif opcion==4:
        dividir(a,b)
    elif opcion==5:
        print ("Salir")
    else:
        print("Digitó un numero incorrecto")
