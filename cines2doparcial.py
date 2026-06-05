import re
from functools import reduce

# =========================
# DATOS PRINCIPALES
# =========================

peliculas = []
clientes = []
funciones = []
compras = []

# Conjunto: no permite repetidos
dnis_registrados = set()

# Diccionario de combos
combos = {
    "0": {"nombre": "Sin combo", "precio": 0},
    "1": {"nombre": "Combo chico", "precio": 2500},
    "2": {"nombre": "Combo grande", "precio": 4000}
}

# Conjuntos para ejemplo de stock
productos_sistema = {"coca", "pochoclos chicos", "pochoclos grandes"}
productos_stock = {"coca", "pochoclos chicos", "pochoclos grandes"}

admin_usuario = "admin"
admin_clave = "1234"


# =========================
# VALIDACIONES REGEX
# =========================

def validar_dni(dni):
    """Valida DNI de 8 números."""
    return re.match(r"^\d{8}$", dni)


def validar_telefono(telefono):
    """Valida teléfono de 10 u 11 números."""
    return re.match(r"^\d{10,11}$", telefono)


# =========================
# FUNCIONES BASICAS
# =========================

def crear_sala(filas, columnas):
    """Crea una matriz de butacas."""
    sala = []

    i = 0
    while i < filas:
        fila = []
        j = 0

        while j < columnas:
            fila.append(0)
            j += 1

        sala.append(fila)
        i += 1

    return sala


def mostrar_sala(sala):
    """Muestra la sala."""
    print("\n--- SALA ---")

    i = 0
    while i < len(sala):
        j = 0

        while j < len(sala[i]):
            print(sala[i][j], end=" ")
            j += 1

        print()
        i += 1

    print("0 = libre | 1 = ocupado")


def buscar_cliente_por_dni(dni):
    """Busca cliente por DNI."""
    i = 0

    while i < len(clientes):
        if clientes[i]["dni"] == dni:
            return i
        i += 1

    return -1


# =========================
# PROCESAMIENTO
# =========================

def calcular_precio_final(precio):
    """Usa map para aumentar y aplicar descuento."""
    precios = [precio]

    aumentados = list(map(lambda x: x * 1.10, precios))
    finales = list(map(lambda x: x * 0.95 if x > 3000 else x, aumentados))

    return round(finales[0], 2)


def calcular_total_con_findall(entrada, combo):
    """Usa findall para extraer importes y sumarlos."""
    texto = "Entrada: " + str(entrada) + " Combo: " + str(combo)

    numeros = re.findall(r"\d+\.?\d*", texto)

    total = 0
    i = 0
    while i < len(numeros):
        total += float(numeros[i])
        i += 1

    return round(total, 2)


def obtener_recaudacion_total():
    """Usa map y reduce para sumar compras."""
    if len(compras) == 0:
        return 0

    totales = list(map(lambda c: c["total"], compras))
    total = reduce(lambda a, b: a + b, totales)

    return round(total, 2)


def mostrar_compras_mayores():
    """Usa filter para mostrar compras mayores a $5000."""
    print("\n--- COMPRAS MAYORES A $5000 ---")

    compras_filtradas = list(filter(lambda c: c["total"] > 5000, compras))

    if len(compras_filtradas) == 0:
        print("No hay compras mayores a $5000")
        return

    i = 0
    while i < len(compras_filtradas):
        print(i + 1, "-", compras_filtradas[i])
        i += 1


# =========================
# CLIENTES
# =========================

def registrar_cliente():
    """El cliente se registra solo."""
    print("\n--- REGISTRO CLIENTE ---")

    nombre = input("Nombre: ")
    dni = input("DNI: ")
    telefono = input("Telefono: ")

    if len(nombre) < 2:
        print("Nombre invalido")
        return

    if not validar_dni(dni):
        print("DNI invalido")
        return

    if not validar_telefono(telefono):
        print("Telefono invalido")
        return

    if dni in dnis_registrados:
        print("El cliente ya existe")
        return

    cliente = {
        "nombre": nombre,
        "dni": dni,
        "telefono": telefono
    }

    clientes.append(cliente)
    dnis_registrados.add(dni)

    print("Registro exitoso")


def cargar_cliente():
    """Admin carga cliente."""
    registrar_cliente()


def mostrar_clientes():
    """Muestra clientes."""
    print("\n--- CLIENTES ---")

    if len(clientes) == 0:
        print("No hay clientes")
        return

    i = 0
    while i < len(clientes):
        c = clientes[i]
        print(i + 1, "-", c["nombre"], "| DNI:", c["dni"], "| Tel:", c["telefono"])
        i += 1


# =========================
# PELICULAS
# =========================

def cargar_pelicula():
    """Carga película como diccionario."""
    print("\n--- CARGAR PELICULA ---")

    titulo = input("Titulo: ")
    genero = input("Genero: ")
    duracion = input("Duracion: ")
    clasificacion = input("Clasificacion: ")

    if len(titulo) < 2:
        print("Titulo invalido")
        return

    if not duracion.isdigit():
        print("Duracion invalida")
        return

    pelicula = {
        "titulo": titulo,
        "genero": genero,
        "duracion": int(duracion),
        "clasificacion": clasificacion
    }

    peliculas.append(pelicula)
    print("Pelicula cargada")


def mostrar_peliculas():
    """Muestra películas."""
    print("\n--- PELICULAS ---")

    if len(peliculas) == 0:
        print("No hay peliculas")
        return

    i = 0
    while i < len(peliculas):
        p = peliculas[i]
        print(i + 1, "-", p["titulo"], "|", p["genero"], "|", p["duracion"], "min |", p["clasificacion"])
        i += 1


# =========================
# FUNCIONES
# =========================

def cargar_funcion():
    """Carga función como diccionario."""
    print("\n--- CARGAR FUNCION ---")

    if len(peliculas) == 0:
        print("Primero cargue peliculas")
        return

    mostrar_peliculas()

    opcion = input("Elegir pelicula: ")

    if not opcion.isdigit():
        print("Opcion invalida")
        return

    indice = int(opcion) - 1

    if indice < 0 or indice >= len(peliculas):
        print("Pelicula incorrecta")
        return

    horario = input("Horario: ")
    sala_num = input("Sala: ")
    precio = input("Precio base: ")

    if not sala_num.isdigit():
        print("Sala invalida")
        return

    if not precio.isdigit():
        print("Precio invalido")
        return

    funcion = {
        "pelicula": peliculas[indice]["titulo"],
        "horario": horario,
        "sala_num": int(sala_num),
        "precio_base": int(precio),
        "sala": crear_sala(5, 5)
    }

    funciones.append(funcion)
    print("Funcion cargada")


def mostrar_funciones():
    """Muestra funciones."""
    print("\n--- FUNCIONES ---")

    if len(funciones) == 0:
        print("No hay funciones")
        return

    i = 0
    while i < len(funciones):
        f = funciones[i]
        precio_final = calcular_precio_final(f["precio_base"])

        print(i + 1, "-", f["pelicula"],
              "| Horario:", f["horario"],
              "| Sala:", f["sala_num"],
              "| Precio final:", precio_final)
        i += 1


def ver_sala_de_funcion():
    """Muestra sala de una función."""
    print("\n--- VER SALA ---")

    if len(funciones) == 0:
        print("No hay funciones")
        return

    mostrar_funciones()

    opcion = input("Elegir funcion: ")

    if not opcion.isdigit():
        print("Opcion invalida")
        return

    indice = int(opcion) - 1

    if indice < 0 or indice >= len(funciones):
        print("Funcion incorrecta")
        return

    mostrar_sala(funciones[indice]["sala"])


# =========================
# COMBOS Y STOCK
# =========================

def elegir_combo():
    """Elige combo usando diccionario."""
    print("\n--- COMBOS ---")
    print("0. Sin combo - $0")
    print("1. Combo chico - $2500")
    print("2. Combo grande - $4000")

    opcion = input("Opcion: ")

    if opcion in combos:
        return combos[opcion]

    print("Opcion invalida. Se asigna sin combo")
    return combos["0"]


def mostrar_productos_faltantes():
    """Usa diferencia de conjuntos."""
    print("\n--- PRODUCTOS FALTANTES ---")

    faltantes = productos_sistema - productos_stock

    if len(faltantes) == 0:
        print("No faltan productos")
    else:
        print("Faltan:", faltantes)


# =========================
# COMPRAS
# =========================

def comprar_entrada_cliente(dni):
    """Compra entrada y guarda datos con diccionario y tupla."""
    print("\n--- COMPRA DE ENTRADA ---")

    if len(funciones) == 0:
        print("No hay funciones")
        return

    mostrar_funciones()

    opcion = input("Elegir funcion: ")

    if not opcion.isdigit():
        print("Opcion invalida")
        return

    indice = int(opcion) - 1

    if indice < 0 or indice >= len(funciones):
        print("Funcion incorrecta")
        return

    funcion = funciones[indice]
    sala = funcion["sala"]

    mostrar_sala(sala)

    fila = input("Fila: ")
    columna = input("Columna: ")

    if not fila.isdigit():
        print("Fila invalida")
        return

    if not columna.isdigit():
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

    # Tupla: dato fijo de butaca
    butaca = (fila, columna)

    precio_entrada = calcular_precio_final(funcion["precio_base"])
    combo = elegir_combo()

    total = calcular_total_con_findall(precio_entrada, combo["precio"])

    # Tupla resumen: no debería cambiar luego de comprar
    resumen_compra = (dni, funcion["pelicula"], funcion["horario"], butaca, total)

    compra = {
        "dni": dni,
        "pelicula": funcion["pelicula"],
        "horario": funcion["horario"],
        "butaca": butaca,
        "entrada": precio_entrada,
        "combo": combo["nombre"],
        "precio_combo": combo["precio"],
        "total": total,
        "resumen": resumen_compra
    }

    compras.append(compra)

    print("\nCompra realizada")
    print("Pelicula:", compra["pelicula"])
    print("Horario:", compra["horario"])
    print("Butaca:", compra["butaca"])
    print("Entrada:", compra["entrada"])
    print("Combo:", compra["combo"])
    print("Total:", compra["total"])


def mostrar_compras():
    """Muestra compras realizadas."""
    print("\n--- COMPRAS ---")

    if len(compras) == 0:
        print("No hay compras")
        return

    i = 0
    while i < len(compras):
        c = compras[i]
        print(i + 1,
              "| DNI:", c["dni"],
              "| Pelicula:", c["pelicula"],
              "| Butaca:", c["butaca"],
              "| Combo:", c["combo"],
              "| Total:", c["total"])
        i += 1


def ver_recaudacion_total():
    """Muestra recaudación total."""
    print("\n--- RECAUDACION TOTAL ---")
    print("Total recaudado:", obtener_recaudacion_total())


# =========================
# LOGIN
# =========================

def login_admin():
    """Login admin."""
    print("\n--- LOGIN ADMIN ---")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == admin_usuario and clave == admin_clave:
        menu_admin()
    else:
        print("Usuario o clave incorrectos")


def login_cliente():
    """Login cliente."""
    print("\n--- LOGIN CLIENTE ---")

    dni = input("DNI: ")
    pos = buscar_cliente_por_dni(dni)

    if pos == -1:
        print("Cliente no encontrado")
    else:
        print("Bienvenido", clientes[pos]["nombre"])
        menu_cliente(dni)


# =========================
# MENUS
# =========================

def menu_admin():
    """Menu administrador."""
    op = ""

    while op != "0":
        print("\n--- MENU ADMIN ---")
        print("1. Cargar cliente")
        print("2. Mostrar clientes")
        print("3. Cargar pelicula")
        print("4. Mostrar peliculas")
        print("5. Cargar funcion")
        print("6. Mostrar funciones")
        print("7. Ver sala")
        print("8. Ver compras")
        print("9. Ver recaudacion")
        print("10. Ver compras mayores a $5000")
        print("11. Ver productos faltantes")
        print("0. Volver")

        op = input("Opcion: ")

        if op == "1":
            cargar_cliente()
        if op == "2":
            mostrar_clientes()
        if op == "3":
            cargar_pelicula()
        if op == "4":
            mostrar_peliculas()
        if op == "5":
            cargar_funcion()
        if op == "6":
            mostrar_funciones()
        if op == "7":
            ver_sala_de_funcion()
        if op == "8":
            mostrar_compras()
        if op == "9":
            ver_recaudacion_total()
        if op == "10":
            mostrar_compras_mayores()
        if op == "11":
            mostrar_productos_faltantes()


def menu_cliente(dni):
    """Menu cliente."""
    op = ""

    while op != "0":
        print("\n--- MENU CLIENTE ---")
        print("1. Ver peliculas")
        print("2. Ver funciones")
        print("3. Ver sala")
        print("4. Comprar entrada")
        print("0. Volver")

        op = input("Opcion: ")

        if op == "1":
            mostrar_peliculas()
        if op == "2":
            mostrar_funciones()
        if op == "3":
            ver_sala_de_funcion()
        if op == "4":
            comprar_entrada_cliente(dni)


def menu_principal():
    """Menu principal."""
    op = ""

    while op != "0":
        print("\n=== SISTEMA DE GESTION DE CINES ===")
        print("1. Ingresar como cliente")
        print("2. Registrarse")
        print("3. Ingresar como administrador")
        print("0. Salir")

        op = input("Opcion: ")

        if op == "1":
            login_cliente()
        if op == "2":
            registrar_cliente()
        if op == "3":
            login_admin()


# =========================
# MAIN
# =========================

def main():
    menu_principal()


main()