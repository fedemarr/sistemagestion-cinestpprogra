from functools import reduce
# Importamos reduce desde functools porque en Python 3 no viene incluido directamente.
# reduce sirve para tomar una lista y "reducirla" a un solo valor.
# En este TP lo usamos para calcular la recaudación total sumando los importes de las compras.


# =========================
# DATOS PRINCIPALES
# =========================

# Lista donde se guardan las películas cargadas en el sistema.
# Cada película se guarda como una lista con:
# [titulo, genero, duracion, clasificacion]
peliculas = []

# Lista donde se guardan los clientes registrados.
# Cada cliente se guarda como una lista con:
# [nombre, dni, telefono]
clientes = []

# Lista donde se guardan las funciones del cine.
# Cada función se guarda como una lista con:
# [titulo_pelicula, horario, numero_sala, precio_base, matriz_sala]
funciones = []

# Lista donde se guardan las compras realizadas.
# Cada compra se guarda como una lista con:
# [dni_cliente, pelicula, horario, fila, columna, precio_final]
compras = []

# Usuario y clave fijos para el administrador del sistema.
admin_usuario = "admin"
admin_clave = "1234"


# =========================
# FUNCIONES BASICAS
# =========================

def crear_sala(filas, columnas):
    """
    Esta función crea una matriz de butacas.

    Parámetros:
    - filas: cantidad de filas de la sala
    - columnas: cantidad de columnas de la sala

    Funcionamiento:
    - Crea una lista de listas.
    - Cada posición empieza en 0.
    - El 0 representa una butaca disponible.
    - El 1 representa una butaca ocupada.

    Retorna:
    - La matriz completa de la sala.
    """
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
    """
    Esta función muestra en pantalla la matriz de la sala.

    Parámetro:
    - sala: matriz que contiene los estados de las butacas

    Funcionamiento:
    - Recorre la matriz fila por fila y columna por columna.
    - Imprime cada posición.
    - Muestra una referencia final:
      0 = disponible
      1 = ocupado
    """
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
    """
    Esta función busca un cliente dentro de la lista de clientes usando el DNI.

    Parámetro:
    - dni: DNI ingresado por el usuario

    Funcionamiento:
    - Recorre la lista de clientes.
    - Compara el DNI de cada cliente con el DNI buscado.
    - Si lo encuentra, devuelve la posición.
    - Si no lo encuentra, devuelve -1.

    Retorna:
    - Índice del cliente si existe
    - -1 si no existe
    """
    i = 0

    while i < len(clientes):
        if clientes[i][1] == dni:
            return i
        i = i + 1

    return -1


# =========================
# FUNCIONES NUEVAS DE PROCESAMIENTO
# =========================

def calcular_precio_final(precio_base):
    """
    Esta función calcula el precio final de una entrada usando map y lambda.

    Parámetro:
    - precio_base: precio original de la función

    Funcionamiento:
    1. Se crea una lista con el precio base.
    2. Se aplica un aumento general del 10% usando map.
    3. Luego se aplica un descuento del 5% si el precio aumentado supera 3000.
    4. Se devuelve el precio final redondeado a 2 decimales.

    Acá se implementa lo visto en clase:
    - lambda: para hacer operaciones rápidas
    - map: para transformar valores
    """
    precios = [precio_base]

    # Aumento general del 10%
    aumentados = list(map(lambda x: x * 1.10, precios))

    # Descuento del 5% si el precio supera 3000
    finales = list(map(lambda x: x * 0.95 if x > 3000 else x, aumentados))

    return round(finales[0], 2)


def obtener_recaudacion_total():
    """
    Esta función calcula la recaudación total del cine.

    Funcionamiento:
    1. Si no hay compras, devuelve 0.
    2. Usa map para extraer solamente los precios de cada compra.
    3. Usa reduce para sumar todos esos importes.
    4. Devuelve el total redondeado.

    Acá se aplica:
    - map: para obtener solo el precio de cada compra
    - reduce: para sumar todos los precios
    """
    if len(compras) == 0:
        return 0

    precios = list(map(lambda c: c[5], compras))
    total = reduce(lambda a, b: a + b, precios)

    return round(total, 2)


def mostrar_compras_caras():
    """
    Esta función muestra solo las compras cuyo precio final sea mayor a 3000.

    Funcionamiento:
    1. Verifica si hay compras registradas.
    2. Usa filter para quedarse únicamente con las compras caras.
    3. Si no encuentra ninguna, informa eso.
    4. Si encuentra, las muestra una por una.

    Acá se aplica:
    - filter: para filtrar solamente ciertos elementos de la lista
    """
    print("\n--- COMPRAS MAYORES A $3000 ---")

    if len(compras) == 0:
        print("No hay compras")
        return

    compras_caras = list(filter(lambda c: c[5] > 3000, compras))

    if len(compras_caras) == 0:
        print("No hay compras mayores a $3000")
        return

    i = 0
    while i < len(compras_caras):
        c = compras_caras[i]
        print(i + 1, "-", c)
        i = i + 1


def mostrar_funciones_caras():
    """
    Esta función muestra únicamente las funciones cuyo precio base supera 3000.

    Funcionamiento:
    1. Verifica si hay funciones cargadas.
    2. Usa filter para seleccionar solo las más caras.
    3. Si no hay ninguna, lo informa.
    4. Si hay, las muestra con sus datos.

    Acá se aplica:
    - filter: para quedarse con ciertos elementos según una condición
    """
    print("\n--- FUNCIONES CON PRECIO MAYOR A $3000 ---")

    if len(funciones) == 0:
        print("No hay funciones cargadas")
        return

    funciones_caras = list(filter(lambda f: f[3] > 3000, funciones))

    if len(funciones_caras) == 0:
        print("No hay funciones con precio mayor a $3000")
        return

    i = 0
    while i < len(funciones_caras):
        f = funciones_caras[i]
        print(i + 1, "-", f[0], "| Horario:", f[1], "| Sala:", f[2], "| Precio:", f[3])
        i = i + 1


def mostrar_peliculas_largas():
    """
    Esta función muestra solo las películas cuya duración sea mayor a 120 minutos.

    Funcionamiento:
    1. Verifica si existen películas cargadas.
    2. Usa filter para seleccionar solo las películas largas.
    3. Si no encuentra ninguna, lo informa.
    4. Si encuentra, las muestra.

    Acá se aplica:
    - filter: para elegir elementos que cumplen una condición
    """
    print("\n--- PELICULAS DE MAS DE 120 MINUTOS ---")

    if len(peliculas) == 0:
        print("No hay peliculas cargadas")
        return

    peliculas_largas = list(filter(lambda p: p[2] > 120, peliculas))

    if len(peliculas_largas) == 0:
        print("No hay peliculas largas")
        return

    i = 0
    while i < len(peliculas_largas):
        p = peliculas_largas[i]
        print(i + 1, "-", p[0], "|", p[1], "|", p[2], "min |", p[3])
        i = i + 1


# =========================
# CLIENTES
# =========================

def cargar_cliente():
    """
    Esta función permite cargar un cliente al sistema.

    Funcionamiento:
    1. Pide nombre, DNI y teléfono.
    2. Valida que:
       - el nombre tenga al menos 2 caracteres
       - el DNI sea numérico
       - el teléfono sea numérico
    3. Busca si ya existe un cliente con ese DNI.
    4. Si no existe, lo agrega a la lista clientes.

    Objetivo:
    - Registrar clientes para que luego puedan iniciar sesión y comprar entradas.
    """
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
    """
    Esta función muestra todos los clientes cargados.

    Funcionamiento:
    - Si no hay clientes, lo informa.
    - Si hay, los recorre y muestra cada uno con sus datos.
    """
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
    """
    Esta función permite cargar una película al sistema.

    Funcionamiento:
    1. Pide título, género, duración y clasificación.
    2. Valida que:
       - el título tenga al menos 2 caracteres
       - la duración sea numérica
    3. Guarda la película en la lista peliculas.

    Cada película queda guardada como:
    [titulo, genero, duracion, clasificacion]
    """
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
    """
    Esta función muestra todas las películas cargadas en el sistema.

    Funcionamiento:
    - Si no hay películas, lo informa.
    - Si hay, las muestra una por una con sus datos.
    """
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
    """
    Esta función permite cargar una función de cine.

    Funcionamiento:
    1. Verifica que haya películas cargadas.
    2. Muestra las películas para elegir una.
    3. Pide horario, número de sala y precio base.
    4. Valida que la sala y el precio sean numéricos.
    5. Crea automáticamente una matriz de sala de 5x5.
    6. Guarda la función en la lista funciones.

    Cada función queda guardada como:
    [titulo_pelicula, horario, numero_sala, precio_base, sala]
    """
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
    precio = input("Precio base: ")

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
    """
    Esta función muestra todas las funciones disponibles.

    Funcionamiento:
    - Si no hay funciones, lo informa.
    - Si hay, recorre cada función.
    - Además calcula el precio final usando la función calcular_precio_final().
    - Muestra título, horario, sala, precio base y precio final.

    Esto permite que el usuario vea el precio actualizado automáticamente.
    """
    print("\n--- FUNCIONES ---")

    if len(funciones) == 0:
        print("No hay funciones cargadas")
        return

    i = 0
    while i < len(funciones):
        f = funciones[i]
        precio_final = calcular_precio_final(f[3])
        print(i + 1, "-", f[0], "| Horario:", f[1], "| Sala:", f[2], "| Precio base:", f[3], "| Precio final:", precio_final)
        i = i + 1


def ver_sala_de_funcion():
    """
    Esta función permite visualizar la sala de una función específica.

    Funcionamiento:
    1. Verifica si existen funciones cargadas.
    2. Muestra las funciones.
    3. El usuario elige una.
    4. Se valida que la opción sea correcta.
    5. Se obtiene la matriz sala de la función seleccionada.
    6. Se muestra la sala en pantalla.

    Esto sirve para ver qué butacas están libres y cuáles ocupadas.
    """
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
    """
    Esta función muestra todas las compras realizadas.

    Funcionamiento:
    - Si no hay compras, lo informa.
    - Si hay, las recorre y muestra una por una.

    Cada compra tiene:
    [dni_cliente, pelicula, horario, fila, columna, precio_final]
    """
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
    """
    Esta función permite que un cliente compre una entrada.

    Parámetro:
    - dni_cliente: identifica al cliente logueado que realiza la compra

    Funcionamiento:
    1. Verifica que existan funciones disponibles.
    2. Muestra las funciones y permite elegir una.
    3. Obtiene la sala de esa función.
    4. Muestra la sala para que el cliente vea las butacas.
    5. Pide fila y columna.
    6. Valida que los datos sean numéricos y estén dentro del rango.
    7. Verifica si la butaca ya está ocupada.
    8. Si está libre, la marca como ocupada.
    9. Calcula el precio final de la entrada.
    10. Guarda la compra en la lista compras.
    11. Muestra el resumen de la compra.

    Esta es una de las funciones más importantes del sistema,
    porque une cliente + función + sala + compra.
    """
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

    precio_final = calcular_precio_final(funcion[3])

    compra = [dni_cliente, funcion[0], funcion[1], fila, columna, precio_final]
    compras.append(compra)

    print("\nEntrada comprada correctamente")
    print("Pelicula:", funcion[0])
    print("Horario:", funcion[1])
    print("Sala:", funcion[2])
    print("Butaca:", fila, columna)
    print("Precio final:", precio_final)


def ver_recaudacion_total():
    """
    Esta función muestra en pantalla la recaudación total.

    Funcionamiento:
    - Llama a obtener_recaudacion_total()
    - Imprime el resultado final

    Su objetivo es darle al administrador una visión general
    del dinero recaudado por las ventas.
    """
    print("\n--- RECAUDACION TOTAL ---")
    total = obtener_recaudacion_total()
    print("Total recaudado: $", total)


# =========================
# LOGIN
# =========================

def login_admin():
    """
    Esta función controla el acceso del administrador.

    Funcionamiento:
    1. Pide usuario y clave.
    2. Compara con los datos del administrador.
    3. Si son correctos, entra al menú admin.
    4. Si no, muestra error.

    Esto sirve para separar permisos entre administrador y cliente.
    """
    print("\n--- LOGIN ADMIN ---")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == admin_usuario and clave == admin_clave:
        print("Ingreso correcto")
        menu_admin()
    else:
        print("Usuario o clave incorrectos")


def login_cliente():
    """
    Esta función controla el acceso del cliente.

    Funcionamiento:
    1. Pide el DNI.
    2. Busca ese DNI en la lista de clientes.
    3. Si no existe, informa que no fue encontrado.
    4. Si existe, da la bienvenida y abre el menú cliente.

    Esto permite que cada cliente entre con su identificación.
    """
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
    """
    Este es el menú del administrador.

    Funcionamiento:
    - Se repite hasta que el usuario elija 0.
    - Permite acceder a todas las funciones administrativas:
      cargar clientes, cargar películas, cargar funciones,
      ver compras, ver recaudación, ver reportes, etc.

    Es el centro de control del sistema para el administrador.
    """
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
        print("9. Ver recaudacion total")
        print("10. Ver compras mayores a $3000")
        print("11. Ver funciones caras")
        print("12. Ver peliculas largas")
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

        if opcion == "9":
            ver_recaudacion_total()

        if opcion == "10":
            mostrar_compras_caras()

        if opcion == "11":
            mostrar_funciones_caras()

        if opcion == "12":
            mostrar_peliculas_largas()


def menu_cliente(dni_cliente):
    """
    Este es el menú del cliente.

    Parámetro:
    - dni_cliente: identifica al cliente que inició sesión

    Funcionamiento:
    - Se repite hasta que el usuario elija 0.
    - Permite al cliente:
      ver películas,
      ver funciones,
      ver salas,
      comprar entradas.

    Es el menú principal de interacción para el cliente.
    """
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
    """
    Este es el menú principal del sistema.

    Funcionamiento:
    - Se repite hasta que se elija salir.
    - Permite elegir entre:
      1. Ingresar como cliente
      2. Ingresar como administrador
      0. Salir

    Desde acá arranca todo el programa.
    """
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
    """
    Función principal del programa.

    Funcionamiento:
    - Llama al menú principal.
    - Es el punto de entrada del sistema.

    En la mayoría de los programas, main sirve para arrancar la ejecución.
    """
    menu_principal()


# Llamada inicial al programa.
# Esto hace que el sistema comience a ejecutarse.
main()