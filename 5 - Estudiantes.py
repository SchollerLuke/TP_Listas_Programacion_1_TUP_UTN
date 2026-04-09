estudiantes=["Lucas", "Samuel", "Elías", "David", "Daniel", "Mateo", "Juan", "Ezequiel"]
estudiantes.sort()
limite=3

# Se crea la lista con los nombres de los estudiantes y se ordena alfabéticamente
# Se establece una constante para el límite del menú

print("\nLista de estudiantes:")
for i in range(len(estudiantes)):
    print(f"{estudiantes[i]}", end="")
    if i+1 < len(estudiantes): print(end=", ")

    # Se muestra la lista actual de estudiantes

while True:
    print("\nMenú:")
    print("1) Agregar Estudiante  2) Eliminar Estudiante  3) Salir")
    while True:
        opcion=input("Opcion: ")
        if opcion.isdigit() and int(opcion) >= 1 and int(opcion) <= limite: break
        else: print("Error: la opción ingresada no es válida")
    opcion=int(opcion)

    # Se muestra el menú y se le pide al usuario elegir una opción
    # Se comprueba que la opción sea válida

    if opcion == 3: break
    while True:
        nombre=input("\nIngrese Nombre de Estudiante: ").title()
        if nombre.isalpha(): break
        else: print("Error: el nombre ingresado no es válido")

        # Si la opción es 3 se rompe el bucle saliendo del menú
        # Si no se le pide el nombre del estudiante al usuario

    if opcion == 1:
        estudiantes.append(nombre)
        estudiantes.sort()
        print("Estudiante agregado exitosamene.")
    elif opcion == 2:
        if nombre in estudiantes:
            estudiantes.remove(nombre)
            print("Estudiante eliminado exitosamente.")
        else: print("Error: ese estudiante no existe.")

        # De acuerdo a la opción elegida, el estudiante se agrega o se quita de la lista
        # En caso de agregarse, la lista se vuelve a ordenar
        # En caso de quitarse, se comprueba que el estudiante exista y se elimina

print("\nLista final actualizada:")
for i in range(len(estudiantes)):
    print(f"{estudiantes[i]}", end="")
    if i+1 < len(estudiantes): print(end=", ")

    # Finalmente se imprime la lista completa actualizada