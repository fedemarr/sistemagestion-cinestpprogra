""" leer un conjunto de numeros enteros, calcular su promedio e imprimir aquellos que superen el 
el promedio"""
"""
numeros=[]
n=int(input("Ingrese un numero entero (0 para finalizar): "))
while n!=0:
    numeros.append(n)
    n=int(input("Ingrese un numero entero (0 para finalizar): "))
print("El promedio es:", sum(numeros)/len(numeros))
print("Los numeros que ingrese son:", numeros)
if numeros:
    for numero in numeros:
        if numero > sum(numeros)/len(numeros):
            print("los numeros que superan el promedio son:",numero)
else:
    print("No se ingresaron numeros")

"""

lista1=[]
lista2=[]
suma=0
n=int(input("Ingrese un numero entero (0 para finalizar): "))
while n!=0:
    lista1.append(n)
    n=int(input("Ingrese un numero entero (0 para finalizar): "))
for i in range(len(lista1)):
    suma+=lista1[i]

promedio=suma/len(lista1)
for i in range(len(lista1)):
    if lista1[i]>promedio:
        lista2.append(lista1[i])
print("El promedio es:", promedio)
print("Los numeros que superan el promedio son:", lista2)