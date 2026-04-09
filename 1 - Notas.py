notas=[10, 9, 9, 3, 6, 7, 8, 5, 4, 9]
suma=0
mayor=0
menor=0

# Creo la lista con las notas de los estudiantes
# Creo la variable suma para las notas del promedio
# Creo las variables mayor y menor para obtener la nota más alta y más baja

print("\nNotas de Estudiantes:")
for i in range(len(notas)):
    # Utilizo el for con el tamaño de la lista
    print(f"{notas[i]} ", end="")
    suma+=notas[i]
    # Imprimo las notas una por una y las sumo
    if notas[i] > notas[mayor]:
        mayor=i
    if notas[i] < notas[menor]:
        menor=i
    # Compruebo si una es mayor o menor y reemplaza las variables por el índice correspondiente

print(f"\n\nPromedio total: {suma/len(notas):.2f}")
print(f"La nota más alta es: {notas[mayor]}")
print(f"La nota más baja es: {notas[menor]}")
# Muestra todo lo pedido en pantalla