lista_1 = []
lista_2 = []
lista_3 = []

print("Introduce 5 numeros para la lista_1: ")
for i in range(5):
    num = int(input(f"Numero {i+1} para lista_1: "))
    lista_1.append(num)

print("Introduce 5 numeros para la lista_2: ")
for i in range(5):
    num = int(input(f"Numero {i+1} para lista_2: "))
    lista_2.append(num)

for i in range(5):
    suma = lista_1[i] + lista_2[i]
    lista_3.append(suma)

print("Lista1: ", lista_1)
print("Lista_2: ", lista_2)
print("Lista_3 (suma): ", lista_3)
