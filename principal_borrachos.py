from metodos import estimar, cotizar, borrachos


#estimar cuantas botellas de vodka debo comprar
#estimar cunatas botellas de jugo de naranja debo comprar

#750ml-> vodka
#1500-> jugo
print("Bienvenido al programa para estimar un carrete")
print("cuantas persona invitaras al carrete")
invitados=int(input())
mlVodka=100
mlJugo=200
tragosPersona=0

op= borrachos()
if op==1:
    tragosPersona=2
if op==2:
    tragosPersona=4
if op==3:
    tragosPersona=10
#invitados*tragosPersona*mlVodka-->totalMlVodka
#invitados*tragosPersona*mlJugo-->totalMlJugo
cantidadVodka=estimar(invitados,mlVodka,tragosPersona,"Vodka", 750)
cantidadJugo=estimar(invitados,mlJugo,tragosPersona,"Jugo de naranja",1500)
print("ingrese precio vodka")
precio=int(input())
subTotalVodka=cotizar(cantidadVodka,precio)
print("ingrese precio jugo")
precio=int(input())
subTotalJugo=cotizar(cantidadJugo,precio)
print(f"el total a gastar en el carrete es de:{subTotalJugo+subTotalVodka}")