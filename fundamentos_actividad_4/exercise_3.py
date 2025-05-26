temperaturas = []

# Recolectamos datos para 5 dias
for i in range(1, 6):
    print(f"\nDia {i}: ")
    t_min = float(input(" Temperatura minima: "))
    t_max = float(input(" Temperatura maxima: "))
    temperaturas.append({'dia': i, 'min': t_min, 'max': t_max})

# Mostramo la temperatura media de cada dia
print("\nTemperatura media de cada dia: ")
for t in temperaturas:
    media = (t['min'] + t['max']) / 2
    print(f" Dia {t['dia']}: {media:.2f}°C")

# Buscamos la menos temperatura minima registrada
min_temp_total = min(t['min'] for t in temperaturas)

#Mostramos los dias con la menor temperatura minima
print("\nDia(s) con la temperatura minima mas baja: ")
for t in temperaturas:
    if t['min'] == min_temp_total:
        print(f" Dia{t['dia']} con {t['min']}°C")

# Pedimos una temperatura extra al usuario
temp_extra = float(input("\nIntroduce una temperatura para buscar coincidencias en maximas: "))

if dias_coincidentes:
    print("Dia cuya temperatra maxima coincide con la ingresada: ")
    for dia in dias_coincidentes:
        print(f" Dia {dia}")
else:
    print("Ningun dia tuvo esa temperatura maxima ") 