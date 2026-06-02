import reflex as rx
from Iekrena_frontend.components.navbar import navbar
from Iekrena_frontend.components.footer import footer


def destino_card(nombre: str, pais: str, precio: str, rating: str, imagen: str):
    return rx.box(
        rx.vstack(
            rx.box(
                rx.image(
                    src=imagen,
                    width="100%",
                    height="220px",
                    object_fit="cover",
                    border_radius="18px",
                ),
                rx.box(
                    rx.hstack(
                        rx.box(
                            width="8px",
                            height="8px",
                            border_radius="999px",
                            background="#0077B6",
                        ),
                        rx.text(
                            nombre,
                            font_size="13px",
                            font_weight="700",
                            color="#001D3D",
                        ),
                        spacing="1",
                        align="center",
                    ),
                    position="absolute",
                    top="14px",
                    left="14px",
                    background="rgba(255,255,255,0.92)",
                    padding="6px 14px",
                    border_radius="999px",
                    box_shadow="0 2px 8px rgba(0,0,0,0.12)",
                ),
                position="relative",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text("⭐", font_size="14px"),
                    rx.text(rating, color="#888", font_size="13px", font_weight="600"),
                    spacing="1",
                    align="center",
                ),
                rx.heading(nombre, size="5", color="#001D3D", font_weight="800"),
                rx.text(pais, color="#888", font_size="14px"),
                rx.divider(border_color="#E8EDF2"),
                rx.hstack(
                    rx.vstack(
                        rx.text("Desde", color="#888", font_size="12px"),
                        rx.hstack(
                            rx.text(precio, color="#0077B6", font_weight="900", font_size="26px"),
                            rx.text("USD", color="#0077B6", font_size="13px", font_weight="700", padding_top="6px"),
                            spacing="1",
                            align="end",
                        ),
                        spacing="0",
                        align="start",
                    ),
                    rx.spacer(),
                    rx.button(
                        "Ver detalles",
                        background="#0077B6",
                        color="white",
                        border_radius="12px",
                        padding="10px 22px",
                        font_size="14px",
                        font_weight="700",
                        cursor="pointer",
                    ),
                    width="100%",
                    align="center",
                ),
                spacing="3",
                align="start",
                width="100%",
            ),
            spacing="3",
            align="start",
            width="100%",
        ),
        background="white",
        border_radius="24px",
        padding="16px",
        box_shadow="0 8px 32px rgba(0,0,0,0.10)",
        overflow="hidden",
    )


def experiencia_card(imagen: str, titulo: str, texto: str):
    return rx.vstack(
        rx.box(
            rx.image(src=imagen, width="70px", height="70px", object_fit="contain"),
            width="110px",
            height="110px",
            border_radius="999px",
            background="linear-gradient(135deg, #DFF7FB, #B3E5FC)",
            display="flex",
            align_items="center",
            justify_content="center",
            box_shadow="0 8px 24px rgba(0,119,182,0.16)",
        ),
        rx.heading(titulo, size="4", color="#001D3D", text_align="center", font_weight="800"),
        rx.text(texto, color="#6B7280", text_align="center", font_size="14px", line_height="1.6", max_width="200px"),
        spacing="3",
        align="center",
    )


def home():
    return rx.box(
        navbar("inicio"),

        # — HERO —
        rx.box(
            rx.vstack(
                # Badge
                rx.box(
                    rx.text(
                        "🌴 Plataforma Premium del Caribe",
                        color="#001D3D",
                        font_size="14px",
                        font_weight="700",
                    ),
                    background="#FFB703",
                    padding="8px 20px",
                    border_radius="999px",
                    box_shadow="0 4px 16px rgba(255,183,3,0.40)",
                ),

                # Titulo
                rx.heading(
                    "EXPLORA EL CARIBE",
                    color="white",
                    text_align="center",
                    font_size=["38px", "52px", "72px"],
                    font_weight="900",
                    line_height="1",
                    text_shadow="0 4px 24px rgba(0,0,0,0.50)",
                ),

                # Subtitulo italica
                rx.text(
                    "como nunca antes",
                    color="#FFB703",
                    font_size=["28px", "40px", "56px"],
                    font_weight="800",
                    text_align="center",
                    font_style="italic",
                    text_shadow="0 4px 18px rgba(0,0,0,0.40)",
                ),

                # Descripcion
                rx.text(
                    "Reserva playas paradisíacas, resorts de lujo y aventuras inolvidables.",
                    color="white",
                    font_size="20px",
                    font_weight="500",
                    text_align="center",
                    max_width="700px",
                    line_height="1.5",
                ),

                # Barra de busqueda
                rx.box(
                    rx.hstack(
                        rx.el.input(
                            placeholder="¿A dónde quieres viajar?",
                            style={
                                "border": "none",
                                "outline": "none",
                                "background": "transparent",
                                "box_shadow": "none",
                                "color": "#000000",
                                "width": "250px",
                                "font_size": "15px",
                                "padding": "0",
                            },
                        ),
                        rx.box(width="1px", height="35px", background="#D1D5DB"),
                        rx.el.input(
                            placeholder="Fecha",
                            style={
                                "border": "none",
                                "outline": "none",
                                "background": "transparent",
                                "box_shadow": "none",
                                "color": "#000000",
                                "width": "150px",
                                "font_size": "15px",
                                "padding": "0",
                            },
                        ),
                        rx.box(width="1px", height="35px", background="#D1D5DB"),
                        rx.el.input(
                            placeholder="Personas",
                            style={
                                "border": "none",
                                "outline": "none",
                                "background": "transparent",
                                "box_shadow": "none",
                                "color": "#000000",
                                "width": "130px",
                                "font_size": "15px",
                                "padding": "0",
                            },
                        ),
                        rx.button(
                            "Buscar",
                            background="#FFB703",
                            color="#001D3D",
                            font_weight="900",
                            border_radius="14px",
                            height="46px",
                            padding="0 28px",
                            border="none",
                            cursor="pointer",
                        ),
                        spacing="3",
                        align="center",
                        justify="center",
                    ),
                    background="rgba(255,255,255,0.96)",
                    padding="10px 16px",
                    border_radius="18px",
                    box_shadow="0 20px 60px rgba(0,0,0,0.25)",
                ),

                spacing="5",
                align="center",
            ),

            height="100vh",
            background="""
            linear-gradient(
                rgba(0,0,0,0.18),
                rgba(0,0,0,0.35)
            ),
            url('/hero.png')
            """,
            background_size="cover",
            background_position="center",
            display="flex",
            align_items="center",
            justify_content="center",
            padding_top="130px",
            padding_left="20px",
            padding_right="20px",
        ),

        # — DESTINOS DESTACADOS —
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    rx.text("✈️", font_size="18px"),
                    rx.text(
                        "LOS MEJORES LUGARES",
                        color="#0077B6",
                        font_weight="800",
                        font_size="13px",
                        letter_spacing="0.12em",
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.heading(
                    "Destinos destacados",
                    size="8",
                    color="#001D3D",
                    text_align="center",
                    font_weight="900",
                ),
                spacing="2",
                align="center",
            ),
            rx.grid(
                destino_card("Punta Cana", "República Dominicana", "$299", "4.9 (1200+)", "/puntacana.jpg"),
                destino_card("Aruba", "Caribe", "$450", "4.8 (980+)", "/aruba.jpg"),
                destino_card("Jamaica", "Caribe", "$399", "4.9 (1100+)", "/jamaica.jpg"),
                columns="3",
                spacing="6",
                width="100%",
            ),
            spacing="8",
            padding="70px 60px",
            background="#F8FAFC",
            width="100%",
            align="center",
        ),

        # — EXPERIENCIAS —
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    rx.text("✈️", font_size="18px"),
                    rx.text(
                        "VIVE EXPERIENCIAS ÚNICAS",
                        color="#0077B6",
                        font_weight="800",
                        font_size="13px",
                        letter_spacing="0.12em",
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.heading(
                    "Experiencias del Caribe",
                    size="8",
                    color="#001D3D",
                    text_align="center",
                    font_weight="900",
                ),
                spacing="2",
                align="center",
            ),
            rx.grid(
                experiencia_card("/beach_experience.png", "Playas paradisíacas", "Aguas cristalinas y arenas blancas en los mejores destinos."),
                experiencia_card("/cruise_experience.png", "Cruceros de lujo", "Navega en cruceros premium con todo incluido y vistas espectaculares."),
                experiencia_card("/resort_experience.png", "Resorts premium", "Hospedajes de lujo con servicios exclusivos frente al mar."),
                experiencia_card("/adventure_experience.png", "Aventuras y excursiones", "Vive experiencias únicas llenas de adrenalina y naturaleza."),
                columns="4",
                spacing="7",
                width="100%",
            ),
            spacing="8",
            padding="70px 60px",
            background="linear-gradient(180deg, #F8FAFC 0%, #E0F7FA 100%)",
            width="100%",
            align="center",
        ),

        footer(),
    )