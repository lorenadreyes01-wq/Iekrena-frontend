import reflex as rx
from Iekrena_frontend.components.navbar import navbar


def detalles():
    return rx.box(
        navbar(),
        rx.center(
            rx.heading("Detalles del viaje", size="8"),
            padding_top="140px",
        ),
    )