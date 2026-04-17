from functools import reduce

# =========================
# DATOS PRINCIPALES
# =========================

peliculas = []   # [titulo, genero, duracion, clasificacion]
clientes = []    # [nombre, dni, telefono, usuario, clave]
funciones = []   # [pelicula, horario, sala_num, precio, matriz_butacas]
compras = []     # [cliente, dni, usuario, pelicula, horario, fila, columna, precio]

admin_usuario = "admin"
admin_clave = "1234"

# =========================
# FUNCIONES BASICAS
# =========================

def crear_sala(filas, columnas):
    # crea una matriz con 0 = libre
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
    # muestra la matriz de butacas
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


def buscar_cliente_por_usuario(usuario):
    # busca cliente por usuario
    i = 0

    while i < len(clientes):
        if clientes[i][3] == usuario:
            return i
        i = i + 1

    return -1


def buscar_cliente_por_dni(dni):
    # busca cliente por dni
    i = 0

    while i < len(clientes):
        if clientes[i][1] == dni:
            return i
        i = i + 1

    return -1


# =========================
# CLIENTES
# =========================

def registrar_cliente():
    # registra un nuevo cliente
    print("\n--- REGISTRO DE CLIENTE ---")

    nombre = input("Nombre: ")
    dni = input("DNI: ")
    telefono = input("Telefono: ")
    usuario = input("Crear usuario: ")
    clave = input("Crear clave: ")

    if len(nombre) < 2:
        print("Nombre invalido")
        return

    if dni.isdigit() == False:
        print("DNI invalido")
        return

    if telefono.isdigit() == False:
        print("Telefono invalido")
        return

    if len(usuario) < 3:
        print("Usuario invalido")
        return

    if len(clave) < 3:
        print("Clave invalida")
        return

    if buscar_cliente_por_dni(dni) != -1:
        print("Ya existe un cliente con ese DNI")
        return

    if buscar_cliente_por_usuario(usuario) != -1:
        print("Ese usuario ya existe")
        return

    cliente = [nombre, dni, telefono, usuario, clave]
    clientes.append(cliente)

    print("Cliente registrado correctamente")


def mostrar_clientes():
    # muestra todos los clientes
    print("\n--- CLIENTES REGISTRADOS ---")

    if len(clientes) == 0:
        print("No hay clientes registrados")
        return

    i = 0
    while i < len(clientes):
        c = clientes[i]
        print(i + 1, "-", c[0], "| DNI:", c[1], "| Tel:", c[2], "| Usuario:", c[3])
        i = i + 1


def login_cliente():
    # login de cliente
    print("\n--- LOGIN CLIENTE ---")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    i = 0
    while i < len(clientes):
        if clientes[i][3] == usuario and clientes[i][4] == clave:
            print("Bienvenido", clientes[i][0])
            menu_cliente(clientes[i])
            return
        i = i + 1

    print("Usuario o clave incorrectos")


# =========================
# ADMIN
# =========================

def login_admin():
    # login del administrador
    print("\n--- LOGIN ADMINISTRADOR ---")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == admin_usuario and clave == admin_clave:
        print("Ingreso correcto")
        menu_admin()
    else:
        print("Usuario o clave incorrectos")


# =========================
# PELICULAS
# =========================

def cargar_pelicula():
    # carga una pelicula
    print("\n--- CARGAR PELICULA ---")

    titulo = input("Titulo: ")
    genero = input("Genero: ")
    duracion = input("Duracion en minutos: ")
    clasificacion = input("Clasificacion: ")

    if len(titulo) < 2:
        print("Titulo invalido")
        return

    if len(genero) < 2:
        print("Genero invalido")
        return

    if duracion.isdigit() == False:
        print("Duracion invalida")
        return

    pelicula = [titulo, genero, int(duracion), clasificacion]
    peliculas.append(pelicula)

    print("Pelicula cargada correctamente")


def mostrar_peliculas():
    # muestra todas las peliculas
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
    # carga una funcion asociada a una pelicula
    print("\n--- CARGAR FUNCION ---")

    if len(peliculas) == 0:
        print("Primero debe cargar peliculas")
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
        print("Numero de sala invalido")
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
    # muestra todas las funciones
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
    # permite ver la sala de una funcion
    print("\n--- VER SALA DE FUNCION ---")

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
# COMPRAS / RESERVAS
# =========================

def comprar_entrada(cliente):
    # permite comprar una entrada
    print("\n--- COMPRA DE ENTRADA ---")

    if len(funciones) == 0:
        print("No hay funciones disponibles")
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
        print("La butaca ya esta ocupada")
        return

    sala[fila][columna] = 1

    compra = [
        cliente[0],
        cliente[1],
        cliente[3],
        funcion[0],
        funcion[1],
        fila,
        columna,
        funcion[3]
    ]

    compras.append(compra)

    print("\nEntrada comprada correctamente")
    print("Cliente:", cliente[0])
    print("Pelicula:", funcion[0])
    print("Horario:", funcion[1])
    print("Sala:", funcion[2])
    print("Butaca:", fila, columna)
    print("Precio:", funcion[3])


def mostrar_compras():
    # muestra todas las compras hechas
    print("\n--- RESERVAS / COMPRAS ---")

    if len(compras) == 0:
        print("No hay compras registradas")
        return

    i = 0
    while i < len(compras):
        c = compras[i]
        print(
            i + 1, "-",
            "Cliente:", c[0],
            "| DNI:", c[1],
            "| Usuario:", c[2],
            "| Pelicula:", c[3],
            "| Horario:", c[4],
            "| Butaca:", c[5], c[6],
            "| Precio:", c[7]
        )
        i = i + 1


# =========================
# MAP / FILTER / REDUCE
# =========================

def peliculas_en_mayusculas():
    # map transforma los titulos a mayusculas
    lista = list(map(lambda p: p[0].upper(), peliculas))

    print("\n--- TITULOS EN MAYUSCULAS ---")
    print(lista)


def funciones_baratas():
    # filter muestra funciones con precio menor a 3000
    lista = list(filter(lambda f: f[3] < 3000, funciones))

    print("\n--- FUNCIONES BARATAS ---")

    if len(lista) == 0:
        print("No hay funciones baratas")
        return

    i = 0
    while i < len(lista):
        f = lista[i]
        print(i + 1, "-", f[0], "| Horario:", f[1], "| Sala:", f[2], "| Precio:", f[3])
        i = i + 1


def total_recaudado():
    # reduce suma todos los precios de las compras
    total = reduce(lambda acumulador, compra: acumulador + compra[7], compras, 0)

    print("\n--- TOTAL RECAUDADO ---")
    print("Total:", total)


# =========================
# MENUS
# =========================

def menu_admin():
    # menu del administrador
    opcion = ""

    while opcion != "0":
        print("\n=== MENU ADMINISTRADOR ===")
        print("1. Cargar pelicula")
        print("2. Mostrar peliculas")
        print("3. Cargar funcion")
        print("4. Mostrar funciones")
        print("5. Ver sala de una funcion")
        print("6. Ver reservas / compras")
        print("7. Ver clientes")
        print("8. Peliculas en mayusculas (map)")
        print("9. Funciones baratas (filter)")
        print("10. Total recaudado (reduce)")
        print("0. Volver")

        opcion = input("Elegir opcion: ")

        if opcion == "1":
            cargar_pelicula()

        if opcion == "2":
            mostrar_peliculas()

        if opcion == "3":
            cargar_funcion()

        if opcion == "4":
            mostrar_funciones()

        if opcion == "5":
            ver_sala_de_funcion()

        if opcion == "6":
            mostrar_compras()

        if opcion == "7":
            mostrar_clientes()

        if opcion == "8":
            peliculas_en_mayusculas()

        if opcion == "9":
            funciones_baratas()

        if opcion == "10":
            total_recaudado()


def menu_cliente(cliente):
    # menu del cliente
    opcion = ""

    while opcion != "0":
        print("\n=== MENU CLIENTE ===")
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
            comprar_entrada(cliente)


def menu_principal():
    # menu principal del sistema
    opcion = ""

    while opcion != "0":
        print("\n=== SISTEMA DE GESTION DE CINES ===")
        print("1. Registrarse como cliente")
        print("2. Iniciar sesion cliente")
        print("3. Iniciar sesion administrador")
        print("0. Salir")

        opcion = input("Elegir opcion: ")

        if opcion == "1":
            registrar_cliente()

        if opcion == "2":
            login_cliente()

        if opcion == "3":
            login_admin()


# =========================
# MAIN
# =========================

def main():
    # inicia el programa
    menu_principal()


main()