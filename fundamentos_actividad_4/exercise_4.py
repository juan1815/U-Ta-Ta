import random

numeros_secreto = random.randint(1, 11)
intentos_restantes = 10

for intento in range(1, 11):
    try:
        numero_usuario = int(input(f"\nIntento {intento}: Introduce tu numero: "))

        if numero_usuario < 1 or numero_usuario > 100:
            print("Por favor, introduce un numero entre 1 y 100")
            continue
        if numero_usuario == numeros_secreto:
            print(f"¡Felicidades! Adivinaste el número secreto ({numeros1_secreto}) en el intento {intento}.")
            break
        elif numero_usuario < numeros_secreto:
            print("El numero secreto es mayor")
        else:
            print("El numero secreto es menor")
        
        intentos_restantes -= 1
        print(f"Te quedan {intentos_restantes} intento(s).")

    except ValueError:
        print("Por favor, introduce un numero valido")

else:
    print(f"\n Lo siento, no hay mas intentos. El numero {numeros_secreto}")
