puntajes=[450, 1200, 875, 990, 300, 1500, 640]
puntajes.sort()
puntajes.reverse()

# Crea la lista con los puntajes asignados
# Ordena la lista de menor a mayor y la coloca en reversa

print("\nRanking de puntajes:")
for i in range(len(puntajes)):
    print(f"{i+1}º Puesto: {puntajes[i]}")

    # Muestra el ranking de los puntajes

print(f"\nPuntaje más alto: {puntajes[0]}")
print(f"Puntaje más bajo: {puntajes[-1]}")
print(f"\nEl puntaje 990 se encuentra en la {puntajes.index(990)+1}º posición")

# Muestra el puntaje más alto y más bajo
# Muestra la posición del puntaje 990