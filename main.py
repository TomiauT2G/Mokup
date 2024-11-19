import flet as ft
from credenciales import leer_credenciales, escribir_credenciales, aprobar_usuario, desaprobar_usuario
from tickets import leer_tickets, escribir_ticket, actualizar_ticket
from ui import inicio

ft.app(inicio)