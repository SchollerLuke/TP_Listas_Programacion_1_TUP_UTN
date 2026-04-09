import random
temperatura=[[0]*7 for temp in range(2)]
rango=[8, 17, 10]
suma=[0, 0]
dia=[0]
max=0

# Se importa la librería random para las temperaturas
# Se crea la matriz "temperatura" con 2 filas y 7 columnas
# Se establece un rango de temperaturas de 8 a 16 y un incremento de 10 para las máximas (Esto permite modificar el programa fácilmente a gusto del programador)
# Se crea la lista suma para los promedios de las temperaturas
# Se inicia la variable max en 0 que toma en cuenta la amplitud máxima


for i in range(len(temperatura)):
    for j in range(len(temperatura[0])):
        temperatura[i][j]=random.randrange(rango[0]+rango[2]*i, rango[1]+rango[2]*i)
        suma[i]+=temperatura[i][j]

        # Se utilizan bucles for para establecer las diferentes temperaturas y sumar para el promedio
        # Notar que cuando establezco las máximas, el rango incrementa 10

for i in range(len(temperatura[0])):
    amplitud=temperatura[1][i]-temperatura[0][i]
    if amplitud == max:
        dia.append(i)
    if amplitud > max:
        max=amplitud
        dia.clear()
        dia.append(i)

    # Se mide la amplitud de cada día
    # Si es mayor a la máxima medida anteriormente, entonces se "limpia" la lista "dia" y se agrega el índice del nuevo máximo
    # Si es igual, entonces se agrega otro índice a la lista. Esto es en caso de haber más de un día con la misma amplitud máxima

print(f"El promedio de temperaturas mínimas es de: {suma[0]/len(temperatura[0]):.2f}ºC")
print(f"El promedio de temperaturas máximas es de: {suma[1]/len(temperatura[1]):.2f}ºC")
# Se calculan y muestran los promedios
if len(dia) == 1:
    print("El día con mayor amplitud térmica es:")
else:
    print("Hay varios días con la misma amplitud térmica:")
for i in range(len(dia)):
    print(f"El {dia[i]+1}º día con {max}ºC de diferencia")
    print(f"Mínima de {temperatura[0][dia[i]]}ºC y máxima de {temperatura[1][dia[i]]}ºC")
    # Se muestra la amplitud de el día o los días que tengan la mayor y sus temperaturas máximas y mínimas