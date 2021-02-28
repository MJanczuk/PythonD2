import random
Kryterium = 0.5
ListaA = []
ListaB = []
for a in range(1,10):
    Losowa = (a,random.random())
    if Losowa[1] > Kryterium:
        ListaA.append(Losowa)
    else:
        ListaB.append(Losowa)
print("Nice")
print(ListaA)
print("Naughty")
print(ListaB)