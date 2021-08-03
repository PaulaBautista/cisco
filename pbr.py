lista=["hola",7,3.5,True,9,"mundo",False,4.5]

print(lista)
print(lista[1])
print(lista)
print(lista[0:3])
print(lista[0:4])
print(lista[1:7])
print(lista[6:7])

lista.append("curso")
print(lista)

lista[4]=lista[7]
print(lista)

print(lista[0:9:1])
print(lista[0:9:2])