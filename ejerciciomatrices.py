"""llenar una matriz con numero del 1 al 9 """
"""
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Valor [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)
"""
"""realizar una matriz que se carga la cantidad de filas y columnas 
y que se llena con numeros aleatorios del 1 al 0 y realizar la suma de la matriz"""
"""
import random
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))
matriz = []
suma = 0 
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = random.randint(1, 9)
        fila.append(valor)
        suma += valor
    matriz.append(fila) 
print("Matriz:")
for fila in matriz:
    print(fila)
print(f"Suma de la matriz: {suma}")
"""
"""quiero que se multiplique una matriz que sea 3x3 y que se multiplique todo por un numero random
"""
import random
filas = 3
columnas = 3
matriz = []
multiplicador = random.randint(1, 9)
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = random.randint(1, 9)
        fila.append(valor)
    matriz.append(fila)
print("Matriz original:")
for fila in matriz:
    print(fila)
print(f"Multiplicador: {multiplicador}")
matriz_multiplicada = []
for i in range(filas):
    fila_multiplicada = []
    for j in range(columnas):
        valor_multiplicado = matriz[i][j] * multiplicador
        fila_multiplicada.append(valor_multiplicado)
    matriz_multiplicada.append(fila_multiplicada)
print("Matriz multiplicada:")
for fila in matriz_multiplicada:
    print(fila)