def leer_tickets():
    tickets = []
    try:
        with open("tickets.txt", "r") as file:
            for line in file:
                valores = line.strip().split(",")
                if len(valores) == 12:
                    nombre_cliente, rut_cliente, telefono, correo, tipo_tique, criticidad, detalle_servicio, detalle_problema, area_derivar, ejecutivo_abre, estado, observacion = valores
                    tickets.append((nombre_cliente, rut_cliente, telefono, correo, tipo_tique, criticidad, detalle_servicio, detalle_problema, area_derivar, ejecutivo_abre, estado, observacion))
                else:
                    print(f"Línea con formato incorrecto: {line.strip()}")
    except FileNotFoundError:
        pass
    return tickets

def escribir_ticket(nombre_cliente, rut_cliente, telefono, correo, tipo_tique, criticidad, detalle_servicio, detalle_problema, area_derivar, ejecutivo_abre, estado="A resolución", observacion=""):
    with open("tickets.txt", "a") as file:
        file.write(f"{nombre_cliente},{rut_cliente},{telefono},{correo},{tipo_tique},{criticidad},{detalle_servicio},{detalle_problema},{area_derivar},{ejecutivo_abre},{estado},{observacion}\n")

def actualizar_ticket(index, nombre_cliente, rut_cliente, telefono, correo, tipo_tique, criticidad, detalle_servicio, detalle_problema, area_derivar, ejecutivo_abre, estado, observacion):
    tickets = leer_tickets()
    tickets[index] = (nombre_cliente, rut_cliente, telefono, correo, tipo_tique, criticidad, detalle_servicio, detalle_problema, area_derivar, ejecutivo_abre, estado, observacion)
    with open("tickets.txt", "w") as file:
        for t in tickets:
            file.write(f"{t[0]},{t[1]},{t[2]},{t[3]},{t[4]},{t[5]},{t[6]},{t[7]},{t[8]},{t[9]},{t[10]},{t[11]}\n")

def filtrar_tickets(fecha=None, criticidad=None, tipo=None, ejecutivo_abre=None, ejecutivo_cierra=None, area=None):
    tickets = leer_tickets()
    tickets_filtrados = []

    for ticket in tickets:
        nombre_cliente, rut_cliente, telefono, correo, tipo_tique, criticidad_tique, detalle_servicio, detalle_problema, area_derivar, ejecutivo_abre_tique, estado, observacion = ticket

        if fecha and fecha not in observacion:
            continue
        if criticidad and criticidad != criticidad_tique:
            continue
        if tipo and tipo != tipo_tique:
            continue
        if ejecutivo_abre and ejecutivo_abre != ejecutivo_abre_tique:
            continue
        if ejecutivo_cierra and ejecutivo_cierra not in observacion:
            continue
        if area and area != area_derivar:
            continue

        tickets_filtrados.append(ticket)

    return tickets_filtrados