lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)

#########    OU    ##########        list comprehension mais de for

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)

]
print(lista)