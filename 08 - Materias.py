import random
estudiantes=["Candela", "David", "Daniel", "Lucas", "Monica"]
materias=["Matemática", "Lengua", "Geografía"]
notas=[[0]*5 for temp in range(3)]
suma_estudiantes=[0]*5
suma_materias=[0]*3

# Se importa el módulo random
# Se crean las listas con los estudiantes y las materias
# Se crea la matriz de las notas
# Se crean las listas para las sumas de los promedios

for i in range(len(notas)):
    for j in range(len(notas[0])):
        notas[i][j]=random.randrange(4, 11)
        suma_estudiantes[j]+=notas[i][j]
        suma_materias[i]+=notas[i][j]

        # Se asignan notas aleatorias entre 4 y 10
        # Se suman para calcular el promedio

print("\nPromedio de estudiantes:")
for i in range(len(estudiantes)):
    print(f"{estudiantes[i]}: {suma_estudiantes[i]/len(materias):.2f}")

    # Se muestra el promedio de cada estudiante

print("\nPromedio de materias:")
for i in range(len(materias)):
    print(f"{materias[i]}: {suma_materias[i]/len(estudiantes):.2f}")

    # Se muestra el promedio de cada materia