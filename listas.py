lista=[]
n=int(input("Ingrese la cantidad de elementos que desea agregar a la lista: "))
while n!=0:
    if n not in lista:
        lista.append(n)
    else:
        print("El numero ya se encuentra en la lista")
    n=int(input("Ingrese la cantidad de elementos que desea agregar a la lista: "))
print(lista)
