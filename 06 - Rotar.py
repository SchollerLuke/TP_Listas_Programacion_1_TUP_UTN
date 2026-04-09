lista=list(range(1,8))

# Se crea la lista con 7 números

print("\nLista de números:")
for i in range(len(lista)):
    print(f"{lista[i]}", end="")
    if i+1 < len(lista): print(end=", ")

    # Se imprime la lista

lista.insert(0, lista[-1])
lista.pop()

# Se inserta el último número en el primer lugar y esto mueve todos los demás elementos una posición a la derecha
# Se utiliza pop() sin argumento y esto elimina el último número de la lista

print("\n\nLista final actualizada:")
for i in range(len(lista)):
    print(f"{lista[i]}", end="")
    if i+1 < len(lista): print(end=", ")

    # Finalmente se imprime la lista actualizada