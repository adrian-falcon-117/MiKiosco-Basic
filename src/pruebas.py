# Lista de productos con sus precios
productos = {"producto1": 100, "producto2": 150, "producto3": 200, "producto4": 250}

# Definición de combos (productos que forman un combo y el descuento asociado)
combos = {
    "combo1": {
        "productos": ["producto1", "producto2"],
        "descuento": 0.10,
    },  # 10% de descuento
    "combo2": {
        "productos": ["producto3", "producto4"],
        "descuento": 0.15,
    },  # 15% de descuento
}


# Función para calcular el total con descuento
def calcular_total_con_descuento(carrito):
    total = 0
    combos_aplicados = []

    # Calcular el total inicial suma todo el carrito
    for producto in carrito:
        total += productos.get(producto, 0)

    # print(combos.items())

    # Detectar y aplicar descuentos por combos
    for combo, detalles in combos.items():
        print(combo,"#")

        if all(item in carrito for item in detalles["productos"]):

            descuento = (
                sum(productos[item] for item in detalles["productos"])
                * detalles["descuento"]
            )
            total -= descuento
            
            combos_aplicados.append(combo)

            print(combo)

    return total, combos_aplicados


# Ejemplo de carrito de compras
carrito = ["producto1", "producto2", "producto1", "producto4"]

# Calcular el total con descuento
total, combos_aplicados = calcular_total_con_descuento(carrito)

# Mostrar resultados
print(f"Total con descuento: ${total:.2f}")
if combos_aplicados:
    print(f"Combos aplicados: {', '.join(combos_aplicados)}")
else:
    print("No se aplicaron combos.")
