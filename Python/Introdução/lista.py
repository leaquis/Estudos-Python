minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista_2 = [1, 2, 3, 4, 5]
minha_lista_3 = ["abacaxi", 1, 9.99, True]

print(minha_lista)
print(minha_lista_2)
print(minha_lista_3)
print(minha_lista[1])

for item in minha_lista:
    print(item)

tamanho = len(minha_lista)
print(tamanho)

minha_lista.append("morango")
print(minha_lista)

if 7 in minha_lista_2:
    print("7 esta na lista")
else:
    print("7 não esta na lista")

del minha_lista[2:]
print(minha_lista)

lista = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7, 0]
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
lista.reverse()
print(lista)

lista2 = ["Roberta", "Giovani", "Fernanda", "Erika", "Claudio", "Lucas"]
print(lista2)
lista2.sort()
print(lista2)
