# =========================
# DATOS PRINCIPALES
# =========================

peliculas = []
clientes = []
funciones = []
compras = []

admin_usuario = "admin"
admin_clave = "1234"

# =========================
# FUNCIONES BASICAS
# =========================

def crear_sala(filas, columnas):
    sala = []

    i = 0
    while i < filas:
        fila = []

        j = 0
        while j < columnas:
            fila.append(0)
            j = j + 1

        sala.append(fila)
        i = i + 1

    return sala


def mostrar_sala(sala):
    print("\n--- SALA ---")

    i = 0
    while i < len(sala):
        j = 0

        while j < len(sala[i]):
            print(sala[i][j], end=" ")
            j = j + 1

        print()
        i = i + 1

    print("0 = disponible | 1 = ocupado")


def buscar_cliente_por_dni(dni):
    i = 0

    while i < len(clientes):
        if clientes[i][1] == dni:
            return i
        i = i + 1

    return -1


# =========================
# CLIENTES
# =========================

def cargar_cliente():
    print("\n--- CARGAR CLIENTE ---")

    nombre = input("Nombre: ")
    dni = input("DNI: ")
    telefono = input("Telefono: ")

    if len(nombre) < 2:
        print("Nombre invalido")
        return

    if dni.isdigit() == False:
        print("DNI invalido")
        return

    if telefono.isdigit() == False:
        print("Telefono invalido")
        return

    posicion = buscar_cliente_por_dni(dni)

    if posicion != -1:
        print("El cliente ya existe")
        return

    cliente = [nombre, dni, telefono]
    clientes.append(cliente)

    print("Cliente cargado correctamente")


def mostrar_clientes():
    print("\n--- CLIENTES ---")

    if len(clientes) == 0:
        print("No hay clientes cargados")
        return

    i = 0
    while i < len(clientes):
        c = clientes[i]
        print(i + 1, "-", c[0], "| DNI:", c[1], "| Tel:", c[2])
        i = i + 1


# =========================
# PELICULAS
# =========================

def cargar_pelicula():
    print("\n--- CARGAR PELICULA ---")

    titulo = input("Titulo: ")
    genero = input("Genero: ")
    duracion = input("Duracion en minutos: ")
    clasificacion = input("Clasificacion: ")

    if len(titulo) < 2:
        print("Titulo invalido")
        return

    if duracion.isdigit() == False:
        print("Duracion invalida")
        return

    pelicula = [titulo, genero, int(duracion), clasificacion]
    peliculas.append(pelicula)

    print("Pelicula cargada correctamente")


def mostrar_peliculas():
    print("\n--- PELICULAS ---")

    if len(peliculas) == 0:
        print("No hay peliculas cargadas")
        return

    i = 0
    while i < len(peliculas):
        p = peliculas[i]
        print(i + 1, "-", p[0], "|", p[1], "|", p[2], "min |", p[3])
        i = i + 1


# =========================
# FUNCIONES
# =========================

def cargar_funcion():
    print("\n--- CARGAR FUNCION ---")

    if len(peliculas) == 0:
        print("Primero cargue peliculas")
        return

    mostrar_peliculas()

    opcion = input("Elegir numero de pelicula: ")

    if opcion.isdigit() == False:
        print("Opcion invalida")
        return

    indice = int(opcion) - 1

    if indice < 0 or indice >= len(peliculas):
        print("Pelicula incorrecta")
        return

    horario = input("Horario: ")
    sala_num = input("Numero de sala: ")
    precio = input("Precio: ")

    if sala_num.isdigit() == False:
        print("Sala invalida")
        return

    if precio.isdigit() == False:
        print("Precio invalido")
        return

    sala = crear_sala(5, 5)

    funcion = [
        peliculas[indice][0],
        horario,
        int(sala_num),
        int(precio),
        sala
    ]

    funciones.append(funcion)

    print("Funcion cargada correctamente")


def mostrar_funciones():
    print("\n--- FUNCIONES ---")

    if len(funciones) == 0:
        print("No hay funciones cargadas")
        return

    i = 0
    while i < len(funciones):
        f = funciones[i]
        print(i + 1, "-", f[0], "| Horario:", f[1], "| Sala:", f[2], "| Precio:", f[3])
        i = i + 1


def ver_sala_de_funcion():
    print("\n--- VER SALA ---")

    if len(funciones) == 0:
        print("No hay funciones")
        return

    mostrar_funciones()

    opcion = input("Elegir funcion: ")

    if opcion.isdigit() == False:
        print("Opcion invalida")
        return

    indice = int(opcion) - 1

    if indice < 0 or indice >= len(funciones):
        print("Funcion incorrecta")
        return

    sala = funciones[indice][4]
    mostrar_sala(sala)


# =========================
# COMPRAS
# =========================

def mostrar_compras():
    print("\n--- COMPRAS ---")

    if len(compras) == 0:
        print("No hay compras")
        return

    i = 0
    while i < len(compras):
        c = compras[i]
        print(i + 1, "-", c)
        i = i + 1


def comprar_entrada_cliente(dni_cliente):
    print("\n--- COMPRA DE ENTRADA ---")

    if len(funciones) == 0:
        print("No hay funciones")
        return

    mostrar_funciones()

    opcion = input("Elegir funcion: ")

    if opcion.isdigit() == False:
        print("Opcion invalida")
        return

    indice = int(opcion) - 1

    if indice < 0 or indice >= len(funciones):
        print("Funcion incorrecta")
        return

    funcion = funciones[indice]
    sala = funcion[4]

    mostrar_sala(sala)

    fila = input("Fila: ")
    columna = input("Columna: ")

    if fila.isdigit() == False:
        print("Fila invalida")
        return

    if columna.isdigit() == False:
        print("Columna invalida")
        return

    fila = int(fila)
    columna = int(columna)

    if fila < 0 or fila >= len(sala):
        print("Fila fuera de rango")
        return

    if columna < 0 or columna >= len(sala[0]):
        print("Columna fuera de rango")
        return

    if sala[fila][columna] == 1:
        print("Butaca ocupada")
        return

    sala[fila][columna] = 1

    compra = [dni_cliente, funcion[0], funcion[1], fila, columna, funcion[3]]
    compras.append(compra)

    print("\nEntrada comprada correctamente")
    print("Pelicula:", funcion[0])
    print("Horario:", funcion[1])
    print("Sala:", funcion[2])
    print("Butaca:", fila, columna)
    print("Precio:", funcion[3])


# =========================
# LOGIN
# =========================

def login_admin():
    print("\n--- LOGIN ADMIN ---")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == admin_usuario and clave == admin_clave:
        print("Ingreso correcto")
        menu_admin()
    else:
        print("Usuario o clave incorrectos")


def login_cliente():
    print("\n--- LOGIN CLIENTE ---")

    dni = input("Ingrese su DNI: ")

    posicion = buscar_cliente_por_dni(dni)

    if posicion == -1:
        print("Cliente no encontrado")
    else:
        print("Bienvenido", clientes[posicion][0])
        menu_cliente(dni)


# =========================
# MENUS
# =========================

def menu_admin():
    opcion = ""

    while opcion != "0":
        print("\n--- MENU ADMIN ---")
        print("1. Cargar cliente")
        print("2. Mostrar clientes")
        print("3. Cargar pelicula")
        print("4. Mostrar peliculas")
        print("5. Cargar funcion")
        print("6. Mostrar funciones")
        print("7. Ver sala de una funcion")
        print("8. Ver compras")
        print("0. Volver")

        opcion = input("Elegir opcion: ")

        if opcion == "1":
            cargar_cliente()

        if opcion == "2":
            mostrar_clientes()

        if opcion == "3":
            cargar_pelicula()

        if opcion == "4":
            mostrar_peliculas()

        if opcion == "5":
            cargar_funcion()

        if opcion == "6":
            mostrar_funciones()

        if opcion == "7":
            ver_sala_de_funcion()

        if opcion == "8":
            mostrar_compras()


def menu_cliente(dni_cliente):
    opcion = ""

    while opcion != "0":
        print("\n--- MENU CLIENTE ---")
        print("1. Ver peliculas")
        print("2. Ver funciones")
        print("3. Ver sala de una funcion")
        print("4. Comprar entrada")
        print("0. Volver")

        opcion = input("Elegir opcion: ")

        if opcion == "1":
            mostrar_peliculas()

        if opcion == "2":
            mostrar_funciones()

        if opcion == "3":
            ver_sala_de_funcion()

        if opcion == "4":
            comprar_entrada_cliente(dni_cliente)


def menu_principal():
    opcion = ""

    while opcion != "0":
        print("\n=== SISTEMA DE GESTION DE CINES ===")
        print("1. Ingresar como cliente")
        print("2. Ingresar como administrador")
        print("0. Salir")

        opcion = input("Elegir opcion: ")

        if opcion == "1":
            login_cliente()

        if opcion == "2":
            login_admin()


# =========================
# MAIN
# =========================

def main():
    menu_principal()


main()