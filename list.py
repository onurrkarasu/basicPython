# List.py

var1=10
var2=20
var3=30

alisverisListe=["domates","salatalık","biber","patlıcan",1,3,5]
listeler=[1,2,3,4,5,6,7,8,9,10]

print(listeler)
print(alisverisListe)
print(type(alisverisListe))

print(listeler[2])
print(alisverisListe[2])

print(alisverisListe[-1]) # list'in en son elemanini verir.

# List Divide 
print(alisverisListe[0:2])
print(alisverisListe[0:3])
print(listeler[0:4])
    

# List built-in-function
# append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort

listeler.append(11) #List sonuna ekleme
print(listeler)

listeler.remove(3) # elemani sil
print(listeler)

listeler.reverse() # terse çevir
print(listeler)

liste2=[1,3,5,6,7,8,2,4,6,10,9]
print(liste2.sort())