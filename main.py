import sys


def parsear_linea(linea):
    """
    Recibe una línea de texto del CSV.
    Regresa (producto, cantidad, precio) si es válida, o None si está mal.
    """
    lista = linea.strip().split(',')

    # Si no tiene exactamente 4 columnas, la ignoramos
    if len(lista) != 4:
        return None

    producto = lista[1]

    # try/except para ignorar líneas con letras en vez de números
    try:
        cantidad = int(lista[2])
        precio = float(lista[3])
    except ValueError:
        return None


    return (producto, cantidad, precio)



def agrupar_dic(lineas):
    """
    Recibe todas las líneas del CSV (sin el encabezado).
    Regresa un diccionario con los totales de cada producto.
    """
    productos = {}

    for linea in lineas:
        resultado = parsear_linea(linea)

        if resultado is None:
            continue

        producto = resultado[0]
        cantidad = resultado[1]
        precio = resultado[2]

        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }

        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

    return productos

def calcular_promedios(productos):
    """
    Recibe el diccionario de productos y agrega el precio promedio a cada uno.
    """
    for prod in productos:
        unidades = productos[prod]["unidades"]
        ingreso = productos[prod]["ingreso"]
        productos[prod]["promedio"] = ingreso / unidades if unidades > 0 else 0.0

def ordenar_por_ingreso(productos):
    """
    Recibe el diccionario de productos.
    Regresa una lista ordenada de mayor a menor ingreso.
    """
    return sorted(
        productos.items(),
        key=lambda x: x[1]["ingreso"],
        reverse=True
    )


def imprimir_reporte(productos_ordenados):
    """
    Recibe la lista ordenada e imprime el CSV de salida.
    """
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")

    for nombre, datos in productos_ordenados:
        print(
            f"{nombre},"
            f"{datos['unidades']},"
            f"{datos['ingreso']:.2f},"
            f"{datos['promedio']:.2f}"
        )


def main():
    """
    Función principal. Orquesta todo el flujo del programa.
    """
    lineas = sys.stdin.readlines()
    lineas_datos = lineas[1:]  # Saltamos el encabezado

    productos = agrupar_dic(lineas_datos)
    calcular_promedios(productos)
    productos_ordenados = ordenar_por_ingreso(productos)
    imprimir_reporte(productos_ordenados)


if __name__ == "__main__":
    main()
