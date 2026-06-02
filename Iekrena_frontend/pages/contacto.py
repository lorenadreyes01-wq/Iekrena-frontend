import reflex as rx
from Iekrena_frontend.components.navbar import navbar


def contacto():
    return rx.box(
        navbar(),
        rx.center(
            rx.heading("Contacto", size="8"),
            padding_top="140px",
        ),
    )