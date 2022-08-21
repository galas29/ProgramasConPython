import math 

#modulo math
#round()---> Devuelve el entero mas proximo
#39.5->round()-->40
#39.2->round()-->39
#39.9->round()-->40
#39.0->round()-->39

#floor()-> piso,suelo----> devuelve el entero mas bajo
#39.5->floor()-->39
#39.2->floor()-->39
#39.9->floor()-->39
#39.0->floor()-->39

#ceil()-> devuelve el entero que esta mas arriba
#39.5->ceil()-->40
#39.2->ceil()-->40
#39.9->ceil()-->40
#39.0->ceil()-->39

#metodos sin retorno sin argumento

def estimar(cantidadInv, medidaVaso, vasosPer,ingredientes,volumen):
    total=cantidadInv*medidaVaso*vasosPer
    total=math.ceil(total/volumen) 
    print(f"Debes comprar {total} de {ingredientes}")
    return total
    #return es cuando al momento de invocar al metodo devuelvo una variable


def cotizar(cantidad, precio):
    total= cantidad*precio
    print(f"El total es: {total}")
    return total


def borrachos():
    print("que tan borrachos son tus invitados")
    print("1) lo normal")
    print("2) muy borrachos")
    print("3) extremadamente borrachos")
    opcion = int(input())
    return opcion