import reflex as rx
from Iekrena_frontend.components.navbar import navbar
from Iekrena_frontend.components.footer import footer


def reservas():
    return rx.box(
        navbar("reservas"),

        rx.box(
            rx.vstack(
                rx.heading(
                    "RESERVA TU VIAJE",
                    color="white",
                    font_size="64px",
                    font_weight="900",
                ),

                rx.text(
                    "Completa el formulario y comienza tu próxima aventura.",
                    color="white",
                    font_size="20px",
                ),

                spacing="3",
                align="center",
            ),

            height="50vh",
            background="""
            linear-gradient(rgba(0,20,35,.55), rgba(0,20,35,.55)),
            url('/hero.png')
            """,
            background_size="cover",
            background_position="center",
            display="flex",
            align_items="center",
            justify_content="center",
            padding_top="120px",
        ),

        rx.box(
            rx.vstack(

                rx.heading(
                    "Formulario de Reserva",
                    color="#001D3D",
                    size="7",
                ),

                rx.input(
                    placeholder="Nombre completo",
                    width="100%",
                ),

                rx.input(
                    placeholder="Correo electrónico",
                    width="100%",
                ),

                rx.select(
                    [
                        "Punta Cana",
                        "Samaná",
                        "Aruba",
                        "Jamaica",
                        "Bahamas",
                        "Cancún",
                    ],
                    placeholder="Selecciona un destino",
                    width="100%",
                ),

                rx.input(
                    placeholder="Fecha del viaje",
                    width="100%",
                ),

                rx.input(
                    placeholder="Cantidad de personas",
                    width="100%",
                ),

                rx.text_area(
                    placeholder="Información adicional",
                    width="100%",
                ),

                rx.button(
                    "Reservar ahora",
                    background="#FFB703",
                    color="#001D3D",
                    width="100%",
                    height="50px",
                    font_weight="900",
                    border_radius="14px",
                ),

                spacing="4",
                width="600px",
                max_width="95%",
            ),

            display="flex",
            justify_content="center",
            padding="80px 20px",
            background="#F8FAFC",
        ),

        footer(),
    )