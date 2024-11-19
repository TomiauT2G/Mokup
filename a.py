import random


def generar_ticket_falso():
    nombres_clientes = ["Juan Perez", "Maria Lopez", "Carlos Sanchez", "Ana Gomez","Tomas Bravo","Benjamin Saravia","Manuel Manue","Yolanda Rivera"]
    ruts_clientes = ["12345678-9", "98765432-1", "11223344-5", "55667788-0"]
    telefonos = ["123456789", "987654321", "112233445", "556677889"]
    correos = ["juan@example.com", "maria@example.com", "carlos@example.com", "ana@example.com"]
    tipos_tique = ["Felicitación", "Consulta", "Reclamo", "Problema"]
    criticidades = ["Baja", "Media", "Alta"]
    detalles_servicio = ["Servicio A", "Servicio B", "Servicio C", "Servicio D"]
    detalles_problema = ["Problema A", "Problema B", "Problema C", "Problema D"]
    areas_derivar = ["Área 1", "Área 2", "Área 3", "Área 4"]
    ejecutivos_abre = ["Ejecutivo 1", "Ejecutivo 2", "Ejecutivo 3", "Ejecutivo 4"]
    estados = ["A resolución", "Resuelto", "No aplicable"]
    observaciones = ["Observación A", "Observación B", "Observación C", "Observación D"]

    nombre_cliente = random.choice(nombres_clientes)
    rut_cliente = random.choice(ruts_clientes)
    telefono = random.choice(telefonos)
    correo = random.choice(correos)
    tipo_tique = random.choice(tipos_tique)
    criticidad = random.choice(criticidades)
    detalle_servicio = random.choice(detalles_servicio)
    detalle_problema = random.choice(detalles_problema)
    area_derivar = random.choice(areas_derivar)
    ejecutivo_abre = random.choice(ejecutivos_abre)
    estado = random.choice(estados)
    observacion = random.choice(observaciones)


    return f"{nombre_cliente},{rut_cliente},{telefono},{correo},{tipo_tique},{criticidad},{detalle_servicio},{detalle_problema},{area_derivar},{ejecutivo_abre},{estado},{observacion}\n"

def escribir_tickets_falsos(cantidad):
    with open("tickets.txt", "a") as file:
        for _ in range(cantidad):
            file.write(generar_ticket_falso())

# Generar 10 tickets falsos
escribir_tickets_falsos(10)