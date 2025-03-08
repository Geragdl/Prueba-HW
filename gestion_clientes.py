import os

# Diccionario que almacena clientes y sus archivos
clientes = {}

def cargar_clientes():
    """Carga los clientes desde un archivo si existe."""
    if os.path.exists("clientes.txt"):
        with open("clientes.txt", "r") as f:
            for linea in f:
                nombre, archivo = linea.strip().split(":")
                clientes[nombre] = archivo

def guardar_clientes():
    """Guarda los clientes en un archivo."""
    with open("clientes.txt", "w") as f:
        for nombre, archivo in clientes.items():
            f.write(f"{nombre}:{archivo}\n")

def agregar_cliente(nombre, info_servicio):
    """Crea un nuevo archivo para el cliente con la información del servicio."""
    if nombre in clientes:
        print("El cliente ya existe.")
    else:
        archivo = f"{nombre.replace(' ', '_')}.txt"
        clientes[nombre] = archivo
        with open(archivo, "w") as f:
            f.write(f"Cliente: {nombre}\n")
            f.write(f"Servicio: {info_servicio}\n")
        guardar_clientes()
        print(f"Cliente {nombre} agregado con éxito.")

def actualizar_cliente(nombre, nueva_info):
    """Añade información a un cliente existente."""
    if nombre in clientes:
        archivo = clientes[nombre]
        with open(archivo, "a") as f:
            f.write(f"Nueva solicitud: {nueva_info}\n")
        print(f"Información actualizada para {nombre}.")
    else:
        print("El cliente no existe.")

def consultar_cliente(nombre):
    """Muestra la información del cliente."""
    if nombre in clientes:
        archivo = clientes[nombre]
        with open(archivo, "r") as f:
            print(f.read())
    else:
        print("El cliente no existe.")

def eliminar_cliente(nombre):
    """Elimina un cliente y su archivo."""
    if nombre in clientes:
        archivo = clientes[nombre]
        os.remove(archivo)
        del clientes[nombre]
        guardar_clientes()
        print(f"Cliente {nombre} eliminado.")
    else:
        print("El cliente no existe.")

def mostrar_clientes():
    """Muestra la lista de clientes registrados."""
    if clientes:
        print("Clientes registrados:")
        for nombre in clientes:
            print(f"- {nombre}")
    else:
        print("No hay clientes registrados.")

# Cargar clientes al iniciar el programa
cargar_clientes()

# Simulación con dos usuarios ficticios
agregar_cliente("Juan Perez", "Servicio de Consultoría")
agregar_cliente("Maria Lopez", "Desarrollo de Software")
actualizar_cliente("Juan Perez", "Mantenimiento Mensual")
consultar_cliente("Juan Perez")
eliminar_cliente("Maria Lopez")
mostrar_clientes()
