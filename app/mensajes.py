import flet as ft
#importamos todos los estilos que vamos a ocupar en los componentes
from app.styles.estilos import Buttons, Card, Colors, Inputs, Textos_estilos
#importamos los tipos de mensajes que vamos a mostrar
from app.components.popup import show_popup, show_popup_auto_close, show_snackbar

def main(page: ft.Page):
    #Crea el texto para el título
    title = ft.Text("Mi app Flet", style=Textos_estilos.H4, text_align=ft.TextAlign.CENTER)
    #Crea el texto para el subtítulo
    subtitle = ft.Text("Sistema de estilos centralizado", style=Textos_estilos.H5)
    #Crea la caja de texto para pedir el nombre
    name = ft.TextField(label="Nombre", **Inputs.INPUT_PRIMARY)