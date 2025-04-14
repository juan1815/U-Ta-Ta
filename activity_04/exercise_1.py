numeros = []

while True:
    try:
        print("Introduce un numero si es negativo el programa finaliza")
        numero = int(input("Introduce un numero: "))

        if numero < 0:
            break
        
        numeros.append(numero)
    except ValueError:
        print("Por favor, introduce un numero valido. ")

print("Numeros introducidos: ", numeros)