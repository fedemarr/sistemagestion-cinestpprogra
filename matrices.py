filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))
matriz = []


for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Valor [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)