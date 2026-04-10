"""
def operar(a,b):
    suma=lambda x,y: x+y
    return suma(a,b)
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

resultado=operar(num1,num2)

print("El resultado de la suma es: ",resultado)


numero=[1,2,3,4,5]
resultados=map(lambda x: x**2, numero)
print(list(resultados))
"""
"""
map
def duplicar(x):
    return x*2
numeros=[1,2,3,4,5]
resultados=map(duplicar, numeros)
print(list(resultados))
"""
"filter"
"""
numeros=[1,2,3,4,5]
resultados=filter(lambda x: x%2==0, numeros)
print(list(resultados))

def filtrar_pares(lista):
    return filter(lambda x: x%2==0, lista)
numeros=[1,2,3,4,5]
resultados=filtrar_pares(numeros)
print(list(resultados))
"""
"reduce"
from functools import reduce
def sumar(x,y):
    return x+y
numeros=[1,2,3,4,5]
resultado=reduce(sumar, numeros)
print(resultado)


