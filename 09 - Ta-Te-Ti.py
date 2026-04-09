tateti=[[" ","A","B","C"],["1"],["2"],["3"]]
jugadores=[""]*2
simbolo=["X","O"]
ganador=""

# Crea la lista de las posiciones del tablero
# Crea las listas de los jugadores y los símbolos
# Crea la variable del ganador

for i in range(3):
    for j in range(3):
        tateti[i+1].append("-")

    # Coloca un guión en cada casilla del juego
    # (Esto se puede hacer manual pero decidí hacerlo así)

for i in range(2):
    while True:
        jugadores[i]=input(f"Ingrese el nombre del jugador {i+1}: ").title()
        if jugadores[i].isalpha(): break
        else: print("Error: nombre de jugador inválido.")

    # Pide los nombres de los jugadores
    # Comprueba que los nombres de los jugadores ingresados sean válidos

while ganador == "":
    for i in range(2):
        if ganador != "": break

        # Se crea bucle while con la condición de que "ganador" esté vacío
        # Se crea bucle for para los dos jugadores

        print("")
        for j in range(4):
            for k in range(4):
                print(f" {tateti[j][k]} ", end="")
            print("")

        # Muestra el tablero en la pantalla

        print(f"\nTurno de {jugadores[i]}:")
        while True:
            jugada=input(f"Ingrese la posición de jugada (ej:A1): ").upper()
            if len(jugada) == 2 and jugada[0] in tateti[0] and jugada[0] != " " and int(jugada[1]) in range(1,4):
                if tateti[int(jugada[1])][tateti[0].index(jugada[0])] != "-": print("Error: esa posición ya está ocupada")
                else: break
            else: print("Error: posición de jugada inválida.")

        # Pide al jugador ingresar una posición
        # Comprueba si la posición ingresada es válida
        # Comprueba si la casilla ingresada está ocupada

        tateti[int(jugada[1])][tateti[0].index(jugada[0])]=simbolo[i]

        # Cambia el símbolo de la posición correspondiente

        if tateti[int(jugada[1])].count(simbolo[i]) == 3:
            ganador=jugadores[i]
            break

        # Comprueba si en la misma fila jugada hay 3 símbolos iguales y asigna ganador
        # (No es necesario comprobar si son guiones porque si se jugó en esa fila, necesariamente no todos lo son)

        if tateti[1][tateti[0].index(jugada[0])] == tateti[2][tateti[0].index(jugada[0])] == tateti[3][tateti[0].index(jugada[0])]:
            ganador=jugadores[i]
            break

        # Comprueba si en la misma columna jugada hay 3 símbolos iguales y asigna ganador

        if tateti[1][1] == tateti[2][2] == tateti[3][3] != "-" or tateti[1][3] == tateti[2][2] == tateti[3][1] != "-": 
            ganador=jugadores[i]
            break

        # Comprueba si los símbolos de las diagonales son iguales y asigna ganador
        # (En este caso sí se comprueba si son guiones)

        if tateti[1].count("-") == 0 and tateti[2].count("-") == 0 and tateti[3].count("-") == 0:
            ganador=0

        # Comprueba si todas las posiciones están ocupadas contando los guiones
        # Si no hay guiones y no hay ganador, entonces la partida termina en empate

print("")
for j in range(4):
    for k in range(4):
        print(f" {tateti[j][k]} ", end="")
    print("")

    # Muestra el tablero final

if ganador == 0: print("\nLa partida ha terminado en empate")
else: print(f"\n{ganador} ha ganado la partida!!")

    # Indica el ganador o si es empate