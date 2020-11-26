from random import randint

listaNumeros = [344, 987, 284, 123, 775, 232]

numQuesalio = 123

posNumQueSalio = listaNumeros.index(numQuesalio)

listaNumeros.pop(posNumQueSalio)

print(listaNumeros)


a = randint(0, len(listaNumeros)-1)
print(listaNumeros[a]) 

