datos=[1, 3, 5, 3, 7, 1, 9, 5, 3]
nueva=[]

# Se crean la lista dada y la lista nueva

for i in range(len(datos)):
    if datos[i] in nueva: continue
    else: nueva.append(datos[i])

    # Se agregan los valores a la lista nueva, si ya existe no se agrega

print("\nLista dada con repetidos: ", end="")
for i in range(len(datos)):
    print(f"{datos[i]}", end="")
    if i+1 < len(datos): print(end=", ")

    # Se muestran todos los valores de la lista original

print("\n\nLista nueva sin repetidos: ", end="")
for i in range(len(nueva)):
    print(f"{nueva[i]}", end="")
    if i+1 < len(nueva): print(end=", ")

    # Se muestran todos los valores de la lista nueva sin repeticiones