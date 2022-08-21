def parImpar(n):
    if n % 2== 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")

def primo(n):
    contador=0
    for d in range(1 , (n//2)+1):
        if n % d ==0:
            contador = contador+1
    if contador ==1:
        print(f"{n} es primo")
    else:
        (f"{n} no es primo")

def defectivo(n):
    suma=0
    d=1
    while d<=n//2:
        if n % d ==0:
            suma=suma+d
        d=d+1
    if suma < n:
        print(f"{n} es defectivo")
    else:
        print(f"{n} no es defectivo")

def perfecto(n):
    suma=0
    d=1
    while d<=n//2:
        if n % d ==0:
            suma=suma+d
        d=d+1
    if suma == n:
        print(f"{n} es perfecto")
    else:
        print(f"{n} no es perfecto")

def abundante(n):
    suma=0
    d=1
    while d<=n//2:
        if n % d ==0:
            suma=suma+d
        d=d+1
    if suma > n:
        print(f"{n} es abundante")
    else:
        print(f"{n} no es abundante")

def divisor(a, b):

    if a % b ==0:
        print(f"{b} es divisor de {a}")
    else:
        print(f"{b} no es divisor de {a}")

def nombre (nombre, apellido):
    
    print(f"{nombre} {apellido}")



def menu():
    print("Ingrese una opcion")
    print("a) Evaluar si n es primo")
    print("b) Evaluar si n es par")
    print("C) Evaluar si n es defectivo")
    print("d) Evaluar de n perfecto")
    print("e) Evaluar si n es abundante")
    print("h) Evaluar de b es divisor de a")
    print("g) Nombre")
    print("f) salir")


def inicio():
    op=()
    while op!="f":
        menu()
        op=input()
        if op=="f":
            print("Gracias por usar mi programa")
        else:
            
            if op=="a":
                print("ingrese numero")
                n=int(input())
                primo(n)
            if op=="b":
                print("ingrese numero")
                n=int(input())
                parImpar(n)
            if op=="c":
                print("ingrese numero")
                n=int(input())
                defectivo(n)
            if op=="d":
                print("ingrese numero")
                n=int(input())
                perfecto(n)
            if op=="e":
                print("ingrese numero")
                n=int(input())
                abundante(n)
            if op=="h":
                print("ingrese un numero")
                a=int(input())
                print("ingrese otro numero")
                b=int(input())
                divisor(a, b)
            if op=="g":
                print("ingrese su nombre")
                nombre=input()
                print("ingrese su apellido")
                apellido=input()
                print(f"Bienvenido {nombre} {apellido}")


inicio()