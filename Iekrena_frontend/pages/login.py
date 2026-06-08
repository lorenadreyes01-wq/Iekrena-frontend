from Iekrena_frontend.auth_state import AuthState
import reflex as rx
from Iekrena_frontend.components.navbar import navbar
from Iekrena_frontend.components.footer import footer

class LoginState(rx.State):
    correo: str = ""
    password: str = ""
    error: str = ""

    def set_correo(self, value: str):
        self.correo = value

    def set_password(self, value: str):
        self.password = value

    def iniciar_sesion(self):
        if self.correo == "admin@iekrenatrips.com" and self.password == "admin123":
            self.error = ""
        else:
            self.error = "Correo o contraseña incorrectos"


def login():
    return rx.box(
        navbar(""),

        rx.box(
            rx.grid(
                # FORMULARIO
                rx.vstack(
                    rx.text(
                        "BIENVENIDA A IEKRENA TRIPS",
                        color="#FFB703",
                        font_weight="900",
                        letter_spacing="0.12em",
                    ),

                    rx.heading(
                        "Iniciar sesión",
                        color="#001D3D",
                        font_size="56px",
                        font_weight="900",
                    ),

                    rx.text(
                        "Accede con tu correo y contraseña para gestionar tus reservas.",
                        color="#6B7280",
                        font_size="17px",
                        line_height="1.7",
                    ),

                    rx.input(
                        placeholder="Correo electrónico",
                        width="100%",
                        height="56px",
                        border_radius="14px",
                        value=LoginState.correo,
                        on_change=LoginState.set_correo,
                    ),

                    rx.input(
                        placeholder="Contraseña",
                        type="password",
                        width="100%",
                        height="56px",
                        border_radius="14px",
                        value=LoginState.password,
                        on_change=LoginState.set_password,
                    ),

                 rx.link(
    rx.button(
        "Iniciar sesión",
        on_click=AuthState.iniciar,
        background="#FFB703",
        color="#001D3D",
        width="100%",
        height="56px",
        border_radius="14px",
        font_weight="900",
        font_size="16px",
        box_shadow="0 8px 24px rgba(255,183,3,0.35)",
        cursor="pointer",
    ),
    href="/admin",
    width="100%",
    text_decoration="none",
),

                    rx.box(
                        rx.text(
                            "Las cuentas con rol Administrador tendrán acceso al panel de administración.",
                            color="#001D3D",
                            font_size="14px",
                            font_weight="600",
                        ),
                        background="#E0F7FA",
                        border="1px solid #B2EBF2",
                        padding="16px",
                        border_radius="14px",
                        width="100%",
                    ),

                    spacing="5",
                    align="start",
                    width="100%",
                    padding="50px",
                ),

                # IMAGEN
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Administra tus viajes con seguridad",
                            color="white",
                            font_size="42px",
                            font_weight="900",
                            line_height="1.1",
                        ),

                        rx.text(
                            "Gestiona reservas, ofertas y visitantes desde un solo lugar.",
                            color="rgba(255,255,255,0.90)",
                            font_size="18px",
                            line_height="1.7",
                        ),

                        spacing="4",
                        align="start",
                    ),

                    background="""
                    linear-gradient(
                        rgba(0,29,61,.25),
                        rgba(0,29,61,.82)
                    ),
                    url('/login_hero.jpg')
                    """,

                    background_size="cover",
                    background_position="center",

                    min_height="650px",

                    padding="50px",

                    display="flex",
                    align_items="end",
                ),

                columns="2",
                spacing="0",

                width="100%",
                max_width="1250px",

                background="white",

                border_radius="32px",

                overflow="hidden",

                box_shadow="0 22px 60px rgba(0,0,0,0.18)",
            ),

            min_height="100vh",

            background="""
            linear-gradient(
                rgba(248,250,252,.95),
                rgba(248,250,252,.95)
            )
            """,

            display="flex",
            align_items="center",
            justify_content="center",

            padding="150px 40px 70px 40px",
        ),

        footer(),
    )