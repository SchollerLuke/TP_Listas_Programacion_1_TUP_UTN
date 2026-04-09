estudiantes=["Lucas", "Samuel", "Elías", "David", "Daniel", "Mateo", "Juan", "Ezequiel", "Ana", "Candela"]

# Se crea la lista de los 10 estudiantes

print("\nBuscador de estudiantes")
while True:
    nombre=input(f"Ingrese el nombre del estudiante: ").title()
    if nombre.isalpha(): break
    else: print("Error: nombre de estudiante inválido.")

    # Se le pide al usuario ingresar el nombre de alguno de ellos
    # Comprueba si el nombre ingresado es válido

if nombre in estudiantes:
    print(f"{nombre} se encuentra en la lista en la posición {estudiantes.index(nombre)+1}")
else: print(f"{nombre} no se encuentra en la lista")

# Si el estudiante se encuentra muestra su posición
# Si no se encuentra, se lo indica al usuario