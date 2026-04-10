from functools import reduce

def sumar (a,b):
    return a + b

lista =[1,2,3,4]
resultado = reduce(sumar,lista)
print(resultado)