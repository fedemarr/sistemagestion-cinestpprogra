""" desarrollar una funcion que reiba tres numeros 
enteros y devuelva el mayor de los tres. devolder -1 en caso de existir igualdad
"""
def mayor(a,b,c):
    if a==b or a==c or b==c:
        return -1
    elif a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(mayor(1,2,3))
def main():
    a=int(input("Ingrese el primer numero: "))
    b=int(input("Ingrese el segundo numero: "))
    c=int(input("Ingrese el tercer numero: "))
    print("el numero mayor es:", mayor(a,b,c))
main()

