import random
numeros=[0]*15
pares=[]
impares=[]

# Importo el módulo random y creo las listas

for i in range(len(numeros)):
    numeros[i]=random.randrange(1, 101)
    if numeros[i] % 2 == 0: pares.append(numeros[i])
    else: impares.append(numeros[i])

    # Se asigna un valor aleatorio a cada variable de la lista principal
    # Se comprueban pares e impares y se agregan a su respectiva lista

print("\nLista de 15 números aleatorios: ")
for i in range(len(numeros)):
    print(f"{numeros[i]}", end="")
    if i+1 < len(numeros): print(end=", ")

    # Se imprimen todo los números de la lista principal

print(f"\n\nLa cantidad de números pares es: {len(pares)}")
print(f"La cantidad de números impares es: {len(impares)}")

# Se imprime la cantidad de pares e impares