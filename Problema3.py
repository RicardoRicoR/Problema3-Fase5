# Nombre del estudiante: Ricardo Ernesto Rico Ramírez
# Grupo: 213022_856
# Programa: Ingeniería de electronica
# Código Fuente: Autoría propia


# Cada fila contiene:
# [Código, Nombre, Stock Actual, Stock Mínimo]

inventario = [
    ["A01", "Mouse", 3, 10],
    ["A02", "Teclado", 15, 10],
    ["A03", "Monitor", 2, 5],
    ["A04", "Impresora", 8, 8],
    ["A05", "Audifonos", 1, 6]
]


# Funcion que calcula la cantidad 
# Si el stock actual es menor al minimo:
# se calcula la diferencia.
# En caso contrario, la cantidad sera 0.

def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad

# Titulo

print("\n Sistema de restablecimiento\n")

# Recorre la matriz del inventario
# El ciclo for permite analizar cada artículo

for articulo in inventario:

    # Se obtienen los datos de cada producto

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Se calcula la cantidad necesaria a pedir

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    # Mostrar los resultados

    print("\nCódigo del artículo:", codigo)
    print("Nombre del artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)

# Mensaje final del programa

print("\nFin del reporte")

