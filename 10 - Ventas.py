import random
ventas=[[0]*7 for temp in range(4)]
productos=["Arroz", "Chocolate", "Fideos", "Pan"]
total=[0]*4
dia=[0]*7
mas_vendido=0
mejor_dia=0

# Importa el módulo "random"
# Crea la matriz "ventas" y la lista "productos"
# Crea las listas de las ventas por producto y por día
# Crea las variables del producto más vendido y del día con más ventas

for i in range(len(productos)):
    for j in range(len(ventas)):
        ventas[i][j]=random.randint(1,26)
        total[i]+=ventas[i][j]   
    if total[i] > mas_vendido:
        mas_vendido=total[i]

    # Asigna valores aleatorios a las ventas entre 1 y 25
    # Calula las ventas totales del producto y comprueba el más vendido

for i in range(len(ventas)):
    for j in range(len(productos)):
        dia[i]+=ventas[j][i]
    if dia[i] > mejor_dia:
        mejor_dia=dia[i]

    # Calcula las ventas totales por día y comprueba el día que más se vendió

print("\nProductos vendidos:")
for i in range(len(productos)):
    print(f" - {productos[i]}: {total[i]}")
print(f"\nDía con mayor cantidad de ventas: {dia.index(mejor_dia)}º")
print(f"Producto más vendido: {productos[total.index(mas_vendido)]}")

# Muestra la lista de productos, el día con mayor cantidad de ventas y el producto más vendido