# =========================
# ESTRUCTURAS
# =========================

peliculas = []
clientes = []
funciones = []

# =========================
# PELICULAS
# =========================

def cargar_pelicula():
    print("\n--- CARGAR PELICULA ---")

    titulo = input("Titulo: ")
    genero = input("Genero: ")
    duracion = input("Duracion (min): ")
    clasificacion = input("Clasificacion: ")

    if len(titulo) < 2:
        print("Titulo invalido")
        return

    if duracion.isdigit() == False:
        print("Duracion invalida")
        return

    pelicula = [titulo, genero, int(duracion), clasificacion]
    peliculas.append(pelicula)

    print("Pelicula cargada")

def mostrar_peliculas():
    print("\n--- PELICULAS ---")

    i = 0
    while i < len(peliculas):
        p = peliculas[i]
        print(i+1, "-", p[0], "|", p[1], "|", p[2], "min")
        i = i + 1

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

    cliente = [nombre, dni, telefono]
    clientes.append(cliente)

    print("Cliente cargado")

def mostrar_clientes():
    print("\n--- CLIENTES ---")

    i = 0
    while i < len(clientes):
        c = clientes[i]
        print(i+1, "-", c[0], "| DNI:", c[1])
        i = i + 1

# =========================
# MATRIZ (SALA)
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

    print("0 libre | 1 ocupada")

def ocupar_butaca(sala, fila, columna):

    if fila < 0 or fila >= len(sala):
        print("Fila invalida")
        return

    if columna < 0 or columna >= len(sala[0]):
        print("Columna invalida")
        return

    if sala[fila][columna] == 1:
        print("Ya esta ocupada")
        return

    sala[fila][columna] = 1
    print("Butaca ocupada")

# =========================
# FUNCIONES (CINE)
# =========================

def cargar_funcion():
    print("\n--- CARGAR FUNCION ---")

    if len(peliculas) == 0:
        print("Primero cargá una pelicula")
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
    sala_num = input("Sala: ")
    precio = input("Precio: ")

    if sala_num.isdigit() == False or precio.isdigit() == False:
        print("Datos invalidos")
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

    print("Funcion cargada")

# =========================
# MENU PRINCIPAL
# =========================

def menu():
    opcion = ""

    while opcion != "0":

        print("\n--- MENU ---")
        print("1. Cargar pelicula")
        print("2. Mostrar peliculas")
        print("3. Cargar cliente")
        print("4. Mostrar clientes")
        print("5. Cargar funcion")
        print("0. Salir")

        opcion = input("Elegir opcion: ")

        if opcion == "1":
            cargar_pelicula()

        if opcion == "2":
            mostrar_peliculas()

        if opcion == "3":
            cargar_cliente()

        if opcion == "4":
            mostrar_clientes()

        if opcion == "5":
            cargar_funcion()

# =========================
# INICIO
# =========================

menu()