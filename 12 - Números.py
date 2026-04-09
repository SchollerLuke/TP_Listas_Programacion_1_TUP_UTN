numeros=[0]*8

# Crea una lista de 8 números

print("\nEn este programa podrá ingresar 8 números enteros y serán ordenados de menor a mayor y viceversa")
for i in range(len(numeros)):
    while True:
        numeros[i]=input(f"Ingrese el {i+1}º número: ")
        if numeros[i].isdigit() or (numeros[i][0] == "-" and numeros[i][1:].isdigit()): break
        else: print("Error: valor inválido.")
    numeros[i]=int(numeros[i])

    # Pide al usuario ingresar los 8 números (en este caso también permite negativos)
    # Comprueba que sean válidos y los convierte en int

print("\nLista de números original:")
for i in range(len(numeros)):
    print(f"{numeros[i]} ",end="")

    # Muestra la lista original

numeros.sort()
print("\nLista de números ordenada de menor a mayor:")
for i in range(len(numeros)):
    print(f"{numeros[i]} ",end="")

    # Muestra la lista ordenada de menor a mayor

numeros.reverse()
print("\nLista de números ordenada de mayor a menor:")
for i in range(len(numeros)):
    print(f"{numeros[i]} ",end="")

    # Muestra la lista ordenada de mayor a menor