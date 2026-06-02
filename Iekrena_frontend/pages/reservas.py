import reflex as rx
from Iekrena_frontend.components.navbar import navbar


def reservas():
    return rx.box(
        navbar(),
        rx.center(
            rx.heading("Página de Reservas", size="8"),
            padding_top="140px",
        ),
    )