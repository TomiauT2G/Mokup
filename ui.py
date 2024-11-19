import flet as ft
from credenciales import leer_credenciales, escribir_credenciales, aprobar_usuario, desaprobar_usuario
from tickets import leer_tickets, escribir_ticket, actualizar_ticket, filtrar_tickets

def inicio(page: ft.Page):
    page.title = "Mockup"
    page.version = "0.1"
    page.author = "TomiauT2G"
    usuario_logueado = None

    def volver_atras(e):
        nonlocal usuario_logueado
        usuario_logueado = None
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Image(src="logo.png", width=100, height=100),
                    ft.Text("Iniciar sesión en Mockup", size=24, weight="bold"),
                    correo_field,
                    contrasena_field,
                    b,
                    registrar_boton
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        page.update()

    def mostrar_pagina_principal(e):
        page.clean()
        nuevo_ticket_boton = ft.OutlinedButton("Nuevo Ticket", on_click=mostrar_nuevo_ticket, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
        ver_tickets_boton = ft.OutlinedButton("Ver Tickets", on_click=mostrar_tickets, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
        page.add(ft.Row([nuevo_ticket_boton, ver_tickets_boton], alignment=ft.MainAxisAlignment.SPACE_BETWEEN))
        page.add(ft.OutlinedButton("Volver", on_click=volver_atras, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
        page.update()

    def mostrar_tickets(e):
        page.clean()
        tickets = leer_tickets()
        headers = ["Nombre del Cliente", "Tipo de Tique", "Criticidad", "Detalles"]
        table = ft.DataTable(
            columns=[ft.DataColumn(ft.Text(header)) for header in headers],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(t[0])),  # Nombre del Cliente
                        ft.DataCell(ft.Text(t[4])),  # Tipo de Tique
                        ft.DataCell(ft.Text(t[5])),  # Criticidad
                        ft.DataCell(ft.OutlinedButton("Ver Detalles",
                                                      on_click=lambda e, index=i: mostrar_detalles_ticket(e, index)))
                        # Botón para ver detalles
                    ]
                )
                for i, t in enumerate(tickets)
            ]
        )
        scrollable_container = ft.ListView(
            controls=[table],
            expand=True
        )
        page.add(scrollable_container)
        page.add(ft.OutlinedButton("Volver", on_click=mostrar_pagina_principal,
                                   style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
        page.update()

    def mostrar_nuevo_ticket(e):
        page.clean()
        nombre_cliente_field = ft.TextField(label="Nombre del Cliente", hint_text="Nombre del Cliente")
        rut_cliente_field = ft.TextField(label="RUT del Cliente", hint_text="RUT del Cliente")
        telefono_field = ft.TextField(label="Teléfono", hint_text="Teléfono")
        correo_field = ft.TextField(label="Correo", hint_text="Correo")
        tipo_tique_field = ft.Dropdown(
            label="Tipo de Tique",
            options=[
                ft.dropdown.Option("Felicitación"),
                ft.dropdown.Option("Consulta"),
                ft.dropdown.Option("Reclamo"),
                ft.dropdown.Option("Problema")
            ]
        )
        criticidad_field = ft.Dropdown(
            label="Criticidad",
            options=[
                ft.dropdown.Option("Baja"),
                ft.dropdown.Option("Media"),
                ft.dropdown.Option("Alta")
            ]
        )
        detalle_servicio_field = ft.TextField(label="Detalle del Servicio", hint_text="Detalle del Servicio", multiline=True)
        detalle_problema_field = ft.TextField(label="Detalle del Problema", hint_text="Detalle del Problema", multiline=True)
        area_derivar_field = ft.TextField(label="Área para Derivar", hint_text="Área para Derivar")

        def enviar_ticket(e):
            escribir_ticket(
                nombre_cliente_field.value,
                rut_cliente_field.value,
                telefono_field.value,
                correo_field.value,
                tipo_tique_field.value,
                criticidad_field.value,
                detalle_servicio_field.value,
                detalle_problema_field.value,
                area_derivar_field.value,
                usuario_logueado[0],
                observacion=""
            )
            page.add(ft.Text("Ticket enviado", color="green"))
            page.update()

        enviar_boton = ft.OutlinedButton("Enviar Ticket", on_click=enviar_ticket, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
        page.add(ft.Column([
            ft.Text("Nuevo Ticket", size=20, weight="bold"),
            nombre_cliente_field,
            rut_cliente_field,
            telefono_field,
            correo_field,
            tipo_tique_field,
            criticidad_field,
            detalle_servicio_field,
            detalle_problema_field,
            area_derivar_field,
            enviar_boton
        ]))
        page.add(ft.OutlinedButton("Volver", on_click=mostrar_pagina_principal, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
        page.update()

    def mostrar_detalles_ticket(e, index):
        page.clean()
        tickets = leer_tickets()
        nombre_cliente, rut_cliente, telefono, correo, tipo_tique, criticidad, detalle_servicio, detalle_problema, area_derivar, ejecutivo_abre, estado, observacion = \
        tickets[index]
        nombre_cliente_field = ft.TextField(label="Nombre del Cliente", value=nombre_cliente)
        rut_cliente_field = ft.TextField(label="RUT del Cliente", value=rut_cliente)
        telefono_field = ft.TextField(label="Teléfono", value=telefono)
        correo_field = ft.TextField(label="Correo", value=correo)
        tipo_tique_field = ft.Dropdown(
            label="Tipo de Tique",
            value=tipo_tique,
            options=[
                ft.dropdown.Option("Felicitación"),
                ft.dropdown.Option("Consulta"),
                ft.dropdown.Option("Reclamo"),
                ft.dropdown.Option("Problema")
            ]
        )
        criticidad_field = ft.Dropdown(
            label="Criticidad",
            value=criticidad,
            options=[
                ft.dropdown.Option("Baja"),
                ft.dropdown.Option("Media"),
                ft.dropdown.Option("Alta")
            ]
        )
        detalle_servicio_field = ft.TextField(label="Detalle del Servicio", value=detalle_servicio, multiline=True)
        detalle_problema_field = ft.TextField(label="Detalle del Problema", value=detalle_problema, multiline=True)
        area_derivar_field = ft.TextField(label="Área para Derivar", value=area_derivar)
        estado_field = ft.Dropdown(
            label="Estado",
            value=estado,
            options=[
                ft.dropdown.Option("A resolución"),
                ft.dropdown.Option("Resuelto"),
                ft.dropdown.Option("No aplicable")
            ]
        )
        observacion_field = ft.TextField(label="Observación", value=observacion, multiline=True)

        def actualizar(e):
            actualizar_ticket(
                index,
                nombre_cliente_field.value,
                rut_cliente_field.value,
                telefono_field.value,
                correo_field.value,
                tipo_tique_field.value,
                criticidad_field.value,
                detalle_servicio_field.value,
                detalle_problema_field.value,
                area_derivar_field.value,
                ejecutivo_abre,
                estado_field.value,
                observacion_field.value
            )
            page.add(ft.Text("Ticket actualizado", color="green"))
            page.update()

        actualizar_boton = ft.OutlinedButton("Actualizar Ticket", on_click=actualizar,
                                             style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
        page.add(ft.Column([
            ft.Text("Detalles del Ticket", size=20, weight="bold"),
            nombre_cliente_field,
            rut_cliente_field,
            telefono_field,
            correo_field,
            tipo_tique_field,
            criticidad_field,
            detalle_servicio_field,
            detalle_problema_field,
            area_derivar_field,
            estado_field,
            observacion_field,
            actualizar_boton
        ]))
        page.add(ft.OutlinedButton("Volver", on_click=mostrar_tickets,
                                   style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
        page.update()

    def button_clicked(e):
        nonlocal usuario_logueado
        correo = correo_field.value
        contrasena = contrasena_field.value
        credenciales = leer_credenciales()
        if correo in credenciales and contrasena == credenciales[correo][0]:
            tipo_usuario = credenciales[correo][1]
            aprobado = credenciales[correo][2]
            if aprobado == "True":
                usuario_logueado = (correo, tipo_usuario)
                page.clean()
                if tipo_usuario == "Centro de Ayuda":
                    mostrar_pagina_principal(e)
                elif tipo_usuario == "Ejecutivo de Área":
                    page.add(ft.Row([
                        ft.Column([
                            ft.Text("Panel de Control", size=20, weight="bold"),
                            ft.Text("Dashboard"),
                            ft.Text("Configuración"),
                            ft.Text("Usuarios"),
                            ft.Text("Reportes"),
                        ], width=200),
                        ft.Column([
                            ft.Text("Estadísticas", size=20, weight="bold"),
                            ft.Text("Estadística 1"),
                            ft.Text("Estadística 2"),
                            ft.Text("Estadística 3"),
                        ], expand=True),
                        ft.Column([
                            ft.Text("Notificaciones", size=20, weight="bold"),
                            ft.Text("Notificación 1"),
                            ft.Text("Notificación 2"),
                            ft.Text("Notificación 3"),
                        ], width=200),
                    ]))
                    page.add(ft.OutlinedButton("Volver", on_click=volver_atras, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
                elif tipo_usuario == "Jefe Sucursal":
                    page.add(ft.OutlinedButton("Aprobar/Desaprobar Usuarios", on_click=mostrar_aprobacion_usuarios, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
                    page.add(ft.OutlinedButton("Filtrar Tickets", on_click=mostrar_filtro_tickets, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
                    page.add(ft.OutlinedButton("Volver", on_click=volver_atras, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
                else:
                    page.add(ft.Text("Tipo de usuario no soportado", color="red"))
            else:
                page.add(ft.Text("Usuario no aprobado", color="red"))
        else:
            page.add(ft.Text("Credenciales incorrectas", color="red"))
        page.update()

    def mostrar_aprobacion_usuarios(e):
        page.clean()
        credenciales = leer_credenciales()
        usuario_list = ft.Column(
            [
                ft.Row([
                    ft.Text(f"Correo: {correo}"),
                    ft.Text(f"Tipo de Usuario: {tipo_usuario}"),
                    ft.Text(f"Aprobado: {aprobado}"),
                    ft.OutlinedButton("Aprobar", on_click=lambda e, c=correo: aprobar_usuario(c), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),
                    ft.OutlinedButton("Desaprobar", on_click=lambda e, c=correo: desaprobar_usuario(c), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
                ])
                for correo, (contrasena, tipo_usuario, aprobado) in credenciales.items()
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        page.add(usuario_list)
        page.add(ft.OutlinedButton("Volver", on_click=volver_atras, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
        page.update()

    def mostrar_registro(e):
        page.clean()
        correo_registro = ft.TextField(label="Correo", hint_text="Correo")
        contrasena_registro = ft.TextField(
            label="Contraseña", password=True, can_reveal_password=True
        )
        tipo_usuario_registro = ft.Dropdown(
            label="Tipo de Usuario",
            options=[
                ft.dropdown.Option("Centro de Ayuda"),
                ft.dropdown.Option("Ejecutivo de Área"),
                ft.dropdown.Option("Jefe Sucursal")
            ]
        )
        def registrar_clicked(e):
            escribir_credenciales(correo_registro.value, contrasena_registro.value, tipo_usuario_registro.value)
            volver_atras(e)
        registrar_boton = ft.OutlinedButton("Registrar", on_click=registrar_clicked, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
        page.add(ft.Column([correo_registro, contrasena_registro, tipo_usuario_registro, registrar_boton]))
        page.add(ft.OutlinedButton("Volver", on_click=volver_atras, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
        page.update()

    def mostrar_filtro_tickets(e):
        page.clean()
        fecha_field = ft.TextField(label="Fecha (YYYY-MM-DD)", hint_text="Fecha")
        criticidad_field = ft.Dropdown(
            label="Criticidad",
            options=[
                ft.dropdown.Option("Baja"),
                ft.dropdown.Option("Media"),
                ft.dropdown.Option("Alta")
            ]
        )
        tipo_field = ft.Dropdown(
            label="Tipo de Tique",
            options=[
                ft.dropdown.Option("Felicitación"),
                ft.dropdown.Option("Consulta"),
                ft.dropdown.Option("Reclamo"),
                ft.dropdown.Option("Problema")
            ]
        )
        ejecutivo_abre_field = ft.TextField(label="Ejecutivo que Abre", hint_text="Ejecutivo que Abre")
        ejecutivo_cierra_field = ft.TextField(label="Ejecutivo que Cierra", hint_text="Ejecutivo que Cierra")
        area_field = ft.TextField(label="Área", hint_text="Área")

        def aplicar_filtro(e):
            tickets_filtrados = filtrar_tickets(
                fecha=fecha_field.value,
                criticidad=criticidad_field.value,
                tipo=tipo_field.value,
                ejecutivo_abre=ejecutivo_abre_field.value,
                ejecutivo_cierra=ejecutivo_cierra_field.value,
                area=area_field.value
            )
            mostrar_tickets_filtrados(tickets_filtrados)

        aplicar_filtro_boton = ft.OutlinedButton("Aplicar Filtro", on_click=aplicar_filtro, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
        page.add(ft.Column([
            ft.Text("Filtrar Tickets", size=20, weight="bold"),
            fecha_field,
            criticidad_field,
            tipo_field,
            ejecutivo_abre_field,
            ejecutivo_cierra_field,
            area_field,
            aplicar_filtro_boton
        ]))
        page.add(ft.OutlinedButton("Volver", on_click=mostrar_pagina_principal, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
        page.update()

    def mostrar_tickets_filtrados(tickets):
        page.clean()
        headers = ["Nombre del Ejecutivo", "Fecha de Creación", "Tipo de Tique", "Criticidad", "Área de Destino",
                   "Estado", "Detalles"]
        table = ft.DataTable(
            columns=[ft.DataColumn(ft.Text(header)) for header in headers],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(t[9])),  # Nombre del Ejecutivo
                        ft.DataCell(ft.Text(t[11])),  # Fecha de Creación (asumido en observación)
                        ft.DataCell(ft.Text(t[4])),  # Tipo de Tique
                        ft.DataCell(ft.Text(t[5])),  # Criticidad
                        ft.DataCell(ft.Text(t[8])),  # Área de Destino
                        ft.DataCell(ft.Text(t[10])),  # Estado
                        ft.DataCell(ft.OutlinedButton("Ver Detalles",
                                                      on_click=lambda e, index=i: mostrar_detalles_ticket(e, index)))
                        # Botón para ver detalles
                    ]
                )
                for i, t in enumerate(tickets)
            ]
        )
        scrollable_container = ft.ListView(
            controls=[table],
            expand=True
        )
        page.add(scrollable_container)
        page.add(ft.OutlinedButton("Volver", on_click=mostrar_filtro_tickets,
                                   style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))))
        page.update()

    correo_field = ft.TextField(label="Correo", hint_text="Correo", width=300)
    contrasena_field = ft.TextField(
        label="Contraseña", password=True, can_reveal_password=True, width=300
    )
    b = ft.OutlinedButton("Ingresar", on_click=button_clicked)
    registrar_boton = ft.OutlinedButton("Registrar", on_click=mostrar_registro)

    page.add(
        ft.Column(
            [
                ft.Image(src="logo.png", width=100, height=100),
                ft.Text("Iniciar sesión en Mockup", size=24, weight="bold"),
                correo_field,
                contrasena_field,
                b,
                registrar_boton
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
    page.update()