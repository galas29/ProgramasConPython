
import math

def frase():
    print("ingrese la frase a evaluar")
    frase=input()
    print(frase.replace("matate","****"))

def Nombre():
    print("Ingrese su primer nombre")
    nombre=input()
    print("Inegrese su apellido")
    apellido=input()
    print("Ingrese su edad")
    edad=int(input())
    print(f"Bienvenido {nombre} {apellido} tu edad es {edad} años")

def sub():
    print("Ingrese su nombre completo")
    Nombre=input()
    print("Bienvenido",Nombre[:Nombre.find(" ")])

def Div():
    print("Bienvenido a la evaluacion de divisores")
    print("Debe ingresar 2 numeros para validar si el 2º es o no divisor del 1º")
    print ("ingrese el primer numero")
    try:
        A=int(input())
        print("ingrese el segundo numero")
        B=int(input()) 
        if A%B==0: 
            print(f"{B} es divisor de {A}")
        else:
            print(f"{B} NO es divisor de {A}")
    except ValueError:
        print("El valor que ingreso no es un numero")
    except ZeroDivisionError:
        print("No puedo dividir por 0")
    except:
        print("!ERROR INEPERADO!")

def Cuentas():
    print("Bienvenido al programa de sus cuentas mensuales")
    print("Este programa le mostrara si puede pagar sus cuentas con el sueldo que ud ingrese")
    print("Por favor ingrese su sueldo")
    print("ingrese sueldo")
    sueldo=int(input())
    print("Ingrese el monto de la cuenta de luz")
    luz=int(input())
    print("Ingrese el monto de la cunta de agua")
    agua=int(input())
    print("Ingrese el monto de la cuenta de gas")
    gas=int(input())
    print("ingrese el monto de la cuenta de internet")
    internet=int(input())
    print("ingrese el monto de la colegiatura de sus hijos")
    colegio=int(input())
    total=agua+luz+gas+internet+colegio
    if sueldo>=total:
            print(f"Esta dentro del presupuesto ud debe pagar un total de ${total} pesos")
    else:
            total=total-sueldo 
            print(f"Esta fuera del presupuesto, le faltan ${total} pesos por pagar")

def Kino():
    print("Felicidades ud acaba de ganar de 1.000.000.000")
    print("puede adquirir propiedades de 100, 150 0 250 millones")
    A=math.floor(1000000000/100000000)
    print(f"su presupuesto le alcanza para {A} propiedades de 100 millones")
    B=math.floor(1000000000/150000000)
    print(f"para {B} propiedades de 150 millones")
    C=math.floor(1000000000/250000000)
    print(f"o para {C} propiedades de 250 millones")
    print("!FELICIDADES!")


def menu():
    print("Ingrese una opcion")
    print("1)CiberBullying")
    print("2)Concatenar")
    print("3)SubString")
    print("4)Divisores")
    print("5)PagoCuentas")
    print("6)Premio")
    print("7)Salir")


def inicio():
    op=()
    while op!="7":
        menu()
        op=input()
        if op=="7":
            print("Gracias por usar mi programa")
        else:
            
            if op=="1":
                frase()
            if op=="2":
                Nombre()
            if op=="3":
                sub()
            if op=="4":
                Div()
            if op=="5":
                Cuentas()
            if op=="6":
                Kino()

        

                
            


inicio()
