import flet as ft
import random

def main(page: ft.Page):
    page.title = "Prediciendo el futuro: by Melll the best"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    respuestas = [
        ("Obviooo, como dudas eso!", "green"),
        ("Baja de esa nube, no hay posibilidad de eso", "red"),
        ("mmmm puede ser que si, puede ser que no", "orange"),
        ("Buenooo, que te digoo hahah", "blue"),
        ("Mmm no see, creo que si", "green"),
        ("No creo amigo/a", "red"),
        ("No quiero responder HAHAHA", "purple"),
        ("Ya, seguimos ahorita", "blue"),
        ("Pero claro que siii", "green"),
        ("HAHAHA yo espero que eso sea un chiste", "red"),
        ("No vas a entender..", "gray"),
        ("No entiendo tu pregunta la vdd, o tal vez solo no quiero responder HAHAH", "blue")
    ]


    escribir_pregunta = ft.TextField(
        label="Dime, cual es tu pregunta?",
        width=300,
        hint_text="Un ejemplo: Mell es la mejor? (si)"
    )

    respuesta_text = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)

    def el_click(e):
        pregunta = escribir_pregunta.value.strip()
        if pregunta == "":
            respuesta_text.value = "Si quieres una respuesta, escribe la pregunta porfa y gracias."
            respuesta_text.color = "black"
        else:
            respuesta, color = random.choice(respuestas)
            respuesta_text.value = respuesta
            respuesta_text.color = color
        page.update()

    ask_button = ft.ElevatedButton(text="Pregunta a la 8-Ball", on_click=el_click)

    page.add(
        ft.Column(
            controls=[
                escribir_pregunta,
                ask_button,
                respuesta_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)
