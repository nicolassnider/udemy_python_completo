lista=[1,2,3,4,5]
print(lista)
lista.append(6)
print(lista)
lista.clear()
print(lista)
lista2=[6,7,8,9,10,10,10]
lista.extend(lista2)
print(lista)
print(lista.count(10))
print(lista.index(10))
lista.insert(3,123)
print(lista)
print(lista.sort())