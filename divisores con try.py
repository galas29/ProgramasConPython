
try:
    print("ingrese un numero")
    A=int(input())
    print("ingrese otro numero")
    B=int(input())
    if A%B==0:
        print(f"{B} es divisor de {A} ")
    else:
        print(f"{B} No es un divisor de {A}")
except ZeroDivisionError:
    print("No puedo dividir por cero")  
except ValueError:
    print("El valor ingresado no es un numero")
except:
    print("ohhh ha ocurrido un error")  