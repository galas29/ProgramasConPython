import math


print("Bienvenido al programa para sacar su promedio")
print("ingrese nota n1")
try:
    nota1=float(input())
    print("ingrse nota n2")
    nota2=float(input())
    print("ingrese nota n3")
    nota3=float(input())
    print("Ingrese nota n4")
    nota4=float(input())
except:
    print("debes ingresar un numero separado con un punto")
    print("ejemplo: 4.5")

notas=int(nota1+nota2+nota3+nota4)/4
#notas=math.r(notas)
if notas<4.0:
    print(f"Su promedio es: {notas} 'F' por ti estas REPROBADO ")

else:
    print(f"Su promedio es: {notas} felicidades ud esta APROBADO ")

#print(notas)

