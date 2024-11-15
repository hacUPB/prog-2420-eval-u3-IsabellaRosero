#SISTEMA DE RESERVAS DEL HOTEL 
# Definimos la estructura de datos para manejar las habitaciones disponibles y sus precios.
habitaciones = {
    "Sencilla": {"cantidad": 10, "precio": 160000},  # 10 habitaciones sencillas disponibles
    "Doble": {"cantidad": 10, "precio": 200000},    # 10 habitaciones dobles disponibles
    "VIP": {"cantidad": 10, "precio": 340000},      # 10 habitaciones VIP disponibles
    "Suite": {"cantidad": 10, "precio": 425000}     # 10 habitaciones Suite disponibles
}

# Estructura para los servicios adicionales disponibles y sus precios.
servicios_adicionales = {
    "Todas las comidas": 60000,          # Costo por incluir todas las comidas
    "Gimnasio": 20000,                   # Costo por usar el gimnasio
    "Servicio a la habitación": 50000,  # Costo por servicio a la habitación
    "Parking": 4000,                     # Costo por estacionamiento
    "Piscina y SPA": 30000               # Costo por acceso a la piscina y SPA
}

# Función para mostrar un mensaje de bienvenida al usuario.
def mostrar_bienvenida():
    print("**********************************")
    print("   ¡Bienvenido al Hotel Sandoná!   ")
    print("*********************************\n")

# Función que lista los tipos de habitaciones, cantidad disponible y precios.
def mostrar_habitaciones():
    print("Tipos de habitaciones disponibles:")
    for tipo, datos in habitaciones.items():
        print(f"- {tipo}: {datos['cantidad']} disponibles | Precio: {datos['precio']}")
    print()

# Función que lista los servicios adicionales y sus precios.
def mostrar_servicios_adicionales():
    print("Servicios adicionales disponibles:")
    for servicio, precio in servicios_adicionales.items():
        print(f"- {servicio}: {precio}")
    print()

# Función que pide datos personales del cliente y devuelve un diccionario con ellos.
def solicitar_datos_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    fecha_entrada = input("Fecha de entrada (DD/MM/AAAA): ")
    fecha_salida = input("Fecha de salida (DD/MM/AAAA): ")
    adultos = int(input("Número de adultos: "))
    niños = int(input("Número de niños: "))
    mascotas = input("¿Viaja con mascotas? (sí/no): ").strip().lower()
    return {
        "nombre": nombre,
        "apellido": apellido,
        "fecha_entrada": fecha_entrada,
        "fecha_salida": fecha_salida,
        "adultos": adultos,
        "niños": niños,
        "mascotas": mascotas == "sí"  # True si viaja con mascotas, False si no.
    }

# Función que permite seleccionar un tipo y cantidad de habitaciones.
def seleccionar_habitacion():
    while True:
        tipo = input("Seleccione el tipo de habitación (Sencilla, Doble, VIP, Suite): ").strip().capitalize()
        if tipo in habitaciones and habitaciones[tipo]["cantidad"] > 0:
            cantidad = int(input(f"¿Cuántas habitaciones {tipo} desea reservar? "))
            if cantidad <= habitaciones[tipo]["cantidad"]:
                habitaciones[tipo]["cantidad"] -= cantidad  # Reducimos las habitaciones disponibles
                return tipo, cantidad
            else:
                print("No hay suficientes habitaciones disponibles.")
        else:
            print("Opción no válida o habitaciones agotadas. Intente nuevamente.")

# Función para que el cliente elija servicios adicionales.
def agregar_servicios():
    servicios_seleccionados = []
    mostrar_servicios_adicionales()  # Mostramos los servicios disponibles
    while True:
        servicio = input("Ingrese el servicio adicional que desea agregar (o 'ninguno' para continuar): ").strip()
        if servicio.lower() == "ninguno":  # Salimos si el usuario no quiere más servicios
            break
        if servicio in servicios_adicionales:
            servicios_seleccionados.append(servicio)  # Agregamos el servicio seleccionado
        else:
            print("Servicio no válido. Intente nuevamente.")
    return servicios_seleccionados

# Función que calcula el costo total de la reserva.
def calcular_costo_total(tipo_habitacion, cantidad_habitaciones, servicios):
    costo_habitacion = habitaciones[tipo_habitacion]["precio"] * cantidad_habitaciones
    costo_servicios = sum(servicios_adicionales[servicio] for servicio in servicios)
    return costo_habitacion + costo_servicios  # Total = costo de habitaciones + costo de servicios

# Función principal del programa.
def main():
    mostrar_bienvenida()  # Mostramos la bienvenida
    cliente = solicitar_datos_cliente()  # Pedimos datos personales del cliente
    mostrar_habitaciones()  # Mostramos las habitaciones disponibles
    tipo_habitacion, cantidad_habitaciones = seleccionar_habitacion()  # Selección de habitación
    servicios = agregar_servicios()  # Selección de servicios adicionales
    total = calcular_costo_total(tipo_habitacion, cantidad_habitaciones, servicios)  # Calculamos el total
    
    # Mostramos un resumen de la reserva al usuario
    print("\n--- Resumen de la reserva ---")
    print(f"Cliente: {cliente['nombre']} {cliente['apellido']}")
    print(f"Fecha de entrada: {cliente['fecha_entrada']} | Fecha de salida: {cliente['fecha_salida']}")
    print(f"Habitación: {tipo_habitacion} (Cantidad: {cantidad_habitaciones})")
    if servicios:
        print(f"Servicios adicionales: {', '.join(servicios)}")
    else:
        print("Servicios adicionales: Ninguno")
    print(f"Total a pagar: ${total}")
    print("\n¡Gracias por elegir el Hotel Sandoná! Que tenga una excelente estadía.\n")

if __name__ == "__main__":
    main()
