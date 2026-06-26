import re
import json
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
# ARCHIVOS JSON
# Funciones para guardar y cargar datos con persistencia en archivos .json
# Se usa json.dump() para escribir y json.load() para leer
# indent=4 para que el archivo sea legible
# Si el archivo no existe, se captura FileNotFoundError y se devuelve lista vacía
# =========================

def guardar_clientes_json():
    """Guarda la lista de clientes en un archivo JSON."""
    # json.dump escribe la lista en el archivo con formato indentado
    try:
        with open("clientes.json", "w") as archivo:
            json.dump(clientes, archivo, indent=4)
    except Exception as e:
        print("Error al guardar clientes:", e)


def cargar_clientes_json():
    """Carga los clientes desde el archivo JSON al iniciar el programa."""
    global clientes, dnis_registrados
    # Si el archivo no existe, FileNotFoundError es capturado y se devuelve lista vacía
    try:
        with open("clientes.json", "r") as archivo:
            clientes = json.load(archivo)
            # Reconstruir el conjunto de DNIs desde los datos cargados
            for c in clientes:
                dnis_registrados.add(c["dni"])
    except FileNotFoundError:
        clientes = []
    except Exception as e:
        print("Error al cargar clientes:", e)
        clientes = []


def guardar_peliculas_json():
    """Guarda la lista de películas en un archivo JSON."""
    try:
        with open("peliculas.json", "w") as archivo:
            json.dump(peliculas, archivo, indent=4)
    except Exception as e:
        print("Error al guardar peliculas:", e)


def cargar_peliculas_json():
    """Carga las películas desde el archivo JSON al iniciar el programa."""
    global peliculas
    try:
        with open("peliculas.json", "r") as archivo:
            peliculas = json.load(archivo)
    except FileNotFoundError:
        peliculas = []
    except Exception as e:
        print("Error al cargar peliculas:", e)
        peliculas = []


def guardar_compras_json():
    """Guarda la lista de compras en un archivo JSON."""
    try:
        # Las tuplas se convierten a listas al serializar en JSON
        compras_serializables = []
        for c in compras:
            compra_copia = c.copy()
            # Convertir tupla butaca a lista para que JSON pueda guardarla
            compra_copia["butaca"] = list(c["butaca"])
            # Convertir tupla resumen a lista
            compra_copia["resumen"] = list(c["resumen"])
            compras_serializables.append(compra_copia)
        with open("compras.json", "w") as archivo:
            json.dump(compras_serializables, archivo, indent=4)
    except Exception as e:
        print("Error al guardar compras:", e)


def cargar_compras_json():
    """Carga las compras desde el archivo JSON al iniciar el programa."""
    global compras
    try:
        with open("compras.json", "r") as archivo:
            datos = json.load(archivo)
            # Restaurar tuplas desde listas al cargar
            for c in datos:
                c["butaca"] = tuple(c["butaca"])
                c["resumen"] = tuple(c["resumen"])
            compras = datos
    except FileNotFoundError:
        compras = []
    except Exception as e:
        print("Error al cargar compras:", e)
        compras = []


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

    # Guardar automáticamente al registrar un cliente nuevo
    guardar_clientes_json()

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

    # Excepción: se captura ValueError si la duración no es un número entero válido
    try:
        duracion_int = int(duracion)
    except ValueError:
        print("Duracion invalida")
        return

    pelicula = {
        "titulo": titulo,
        "genero": genero,
        "duracion": duracion_int,
        "clasificacion": clasificacion
    }

    peliculas.append(pelicula)

    # Guardar automáticamente al cargar una película nueva
    guardar_peliculas_json()

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

    # Excepción: captura ValueError si la opción no es un número
    try:
        indice = int(opcion) - 1
    except ValueError:
        print("Opcion invalida")
        return

    if indice < 0 or indice >= len(peliculas):
        print("Pelicula incorrecta")
        return

    horario = input("Horario: ")
    sala_num = input("Sala: ")
    precio = input("Precio base: ")

    # Excepción: captura ValueError en sala y precio
    try:
        sala_num_int = int(sala_num)
    except ValueError:
        print("Sala invalida")
        return

    try:
        precio_int = int(precio)
    except ValueError:
        print("Precio invalido")
        return

    funcion = {
        "pelicula": peliculas[indice]["titulo"],
        "horario": horario,
        "sala_num": sala_num_int,
        "precio_base": precio_int,
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

    # Excepción: captura ValueError si la opción no es un número
    try:
        indice = int(opcion) - 1
    except ValueError:
        print("Opcion invalida")
        return

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

    # Excepción: captura ValueError si la opción no es un número
    try:
        indice = int(opcion) - 1
    except ValueError:
        print("Opcion invalida")
        return

    if indice < 0 or indice >= len(funciones):
        print("Funcion incorrecta")
        return

    funcion = funciones[indice]
    sala = funcion["sala"]

    mostrar_sala(sala)

    fila = input("Fila: ")
    columna = input("Columna: ")

    # Excepción: captura ValueError en fila y columna
    try:
        fila = int(fila)
    except ValueError:
        print("Fila invalida")
        return

    try:
        columna = int(columna)
    except ValueError:
        print("Columna invalida")
        return

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

    # Guardar automáticamente al realizar una compra nueva
    guardar_compras_json()

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
# PRUEBAS UNITARIAS
# Cada prueba llama a una función, guarda el resultado y lo compara con el esperado.
# Si el resultado es correcto se imprime "Prueba correcta", si no "Error en la prueba".
# Permite detectar errores en funciones clave antes de usar el sistema.
# =========================

def prueba_validar_dni_valido():
    """Prueba: DNI de 8 dígitos debe ser válido."""
    resultado = validar_dni("28806009")

    if resultado:
        print("Prueba correcta - DNI valido reconocido")
    else:
        print("Error en la prueba - DNI valido no reconocido")


def prueba_validar_dni_invalido():
    """Prueba: DNI de menos de 8 dígitos debe ser inválido."""
    resultado = validar_dni("123")

    if not resultado:
        print("Prueba correcta - DNI invalido rechazado")
    else:
        print("Error en la prueba - DNI invalido aceptado incorrectamente")


def prueba_validar_telefono_valido():
    """Prueba: teléfono de 10 dígitos debe ser válido."""
    resultado = validar_telefono("1122334455")

    if resultado:
        print("Prueba correcta - Telefono valido reconocido")
    else:
        print("Error en la prueba - Telefono valido no reconocido")


def prueba_validar_telefono_invalido():
    """Prueba: teléfono de menos de 10 dígitos debe ser inválido."""
    resultado = validar_telefono("123456789")

    if not resultado:
        print("Prueba correcta - Telefono invalido rechazado")
    else:
        print("Error en la prueba - Telefono invalido aceptado incorrectamente")


def prueba_calcular_precio_sin_descuento():
    """Prueba: precio 1000 -> aumento 10% -> 1100, no supera 3000 -> sin descuento."""
    resultado = calcular_precio_final(1000)

    if resultado == 1100.0:
        print("Prueba correcta - Precio sin descuento calculado bien")
    else:
        print("Error en la prueba - Precio sin descuento incorrecto:", resultado)


def prueba_calcular_precio_con_descuento():
    """Prueba: precio 3000 -> aumento 10% -> 3300, supera 3000 -> descuento 5% -> 3135."""
    resultado = calcular_precio_final(3000)

    if resultado == 3135.0:
        print("Prueba correcta - Precio con descuento calculado bien")
    else:
        print("Error en la prueba - Precio con descuento incorrecto:", resultado)


def ejecutar_pruebas():
    """Ejecuta todas las pruebas unitarias."""
    print("\n--- EJECUTANDO PRUEBAS UNITARIAS ---")

    # Pruebas de validar_dni
    prueba_validar_dni_valido()
    prueba_validar_dni_invalido()

    # Pruebas de validar_telefono
    prueba_validar_telefono_valido()
    prueba_validar_telefono_invalido()

    # Pruebas de calcular_precio_final
    prueba_calcular_precio_sin_descuento()
    prueba_calcular_precio_con_descuento()

    print("--- FIN DE PRUEBAS ---")


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
        # Nueva opción: ejecutar pruebas unitarias
        print("12. Ejecutar pruebas")
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
        # Ejecutar pruebas unitarias desde el menú admin
        if op == "12":
            ejecutar_pruebas()


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
# Los datos se cargan automáticamente al iniciar el programa desde los archivos JSON.
# Si los archivos no existen, se usan listas vacías (manejado con FileNotFoundError).
# =========================

def main():
    # Carga automática de datos persistidos al arrancar
    cargar_clientes_json()
    cargar_peliculas_json()
    cargar_compras_json()

    menu_principal()


main()
