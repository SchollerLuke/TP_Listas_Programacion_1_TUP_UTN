productos=[0]*5

# Crea la lista con 5 variables

print("\nRealize su pedido de productos\n")

for i in range(len(productos)):
    while True:
        productos[i]=input(f"Ingrese el nombre del {i+1}º producto: ").title()
        if productos[i].isalpha(): break
        else: print("Error: nombre de producto inválido.")

# Con un for pide los 5 productos solicitados y comprueba que sean válidos
    
productos.sort()
# Ordena los productos alfabéticamente
print("\nProductos: ", end="")
for i in range(len(productos)):
    print(f"{productos[i]}", end="")
    if i+1 < len(productos): print(end=", ")

    # Con un for muestra todos los productos y coloca comas en todos menos en el último

while True:
    eliminar=input("\nIngrese que producto desea eliminar: ")
    if eliminar.title() in productos: 
        productos.remove(eliminar.title())
        break
    else: print("Error: ese producto no se encuentra.")

    # Pide al usuario el producto a eliminar y comprueba que exista para hacerlo

print("\nProductos: ", end="")
for i in range(len(productos)):
    print(f"{productos[i]}", end="")
    if i+1 < len(productos): print(end=", ")

    # Con un for muestra todos los productos finales y coloca comas en todos menos en el último