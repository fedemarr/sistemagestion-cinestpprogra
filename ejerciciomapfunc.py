"""Un sistema solicita al usuario cargar una lista de precios de productos.

Se pide:

Ingresar los precios por teclado
Aplicar un aumento del 12% a todos los productos
Aplicar un descuento adicional del 5% SOLO a los productos que superen los $50.000
Filtrar los productos cuyo precio final sea mayor a $40.000
Calcular el total a pagar

Condiciones:

La carga de datos debe hacerse en el main
Crear una función que procese la lista y retorne el resultado
Usar map, filter, reduce y lambda """
from functools import reduce
def procesar_precios(precios):
    # Aplicar aumento del 12%
    precios_con_aumento = map(lambda x: x * 1.12, precios)

    # Aplicar descuento del 5% a productos que superen los $50.000
    precios_con_descuento = map(lambda x: x * 0.95 if x > 50000 else x, precios_con_aumento)

    # Filtrar productos con precio final mayor a $40.000
    precios_filtrados = filter(lambda x: x > 40000, precios_con_descuento)

    # Calcular el total a pagar
    total_a_pagar = reduce(lambda acc, x: acc + x, precios_filtrados, 0)

    return total_a_pagar
introducir_precios = input("Ingrese los precios de los productos separados por comas: ")
precios = list(map(float, introducir_precios.split(",")))
total = procesar_precios(precios)
print("El total a pagar es: $", total)
filtrados = filter(lambda x: x > 40000, map(lambda x: x * 0.95 if x * 1.12 > 50000 else x * 1.12, map(lambda x: x * 1.12, precios)))
print("Los productos con precio final mayor a $40.000 son: ", list(filtrados))
reducciones=reduce(lambda acc, x: acc + x, filter(lambda x: x > 40000, map(lambda x: x * 0.95 if x * 1.12 > 50000 else x * 1.12, map(lambda x: x * 1.12, precios))), 0)
print("El total a pagar es: $", reducciones)

