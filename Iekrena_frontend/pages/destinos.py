import reflex as rx
from Iekrena_frontend.components.navbar import navbar
from Iekrena_frontend.components.footer import footer


class DestinosState(rx.State):
    busqueda: str = ""

    def cargar_busqueda(self):
         self.busqueda = self.router.page.params.get("destino", "")

def destino_card(nombre, pais, precio, rating, imagen):
    return rx.box(
        rx.vstack(
            # Imagen con badge encima
            rx.box(
                rx.image(
                    src=imagen,
                    width="100%",
                    height="210px",
                    object_fit="cover",
                ),
                rx.box(
                    rx.hstack(
                        rx.box(width="8px", height="8px", border_radius="999px", background="#0077B6"),
                        rx.text(nombre, font_size="12px", font_weight="700", color="#001D3D"),
                        spacing="1",
                        align="center",
                    ),
                    position="absolute",
                    top="12px",
                    left="12px",
                    background="rgba(255,255,255,0.93)",
                    padding="5px 12px",
                    border_radius="999px",
                    box_shadow="0 2px 8px rgba(0,0,0,0.12)",
                ),
                # Rating badge top right
                rx.box(
                    rx.hstack(
                        rx.text("★", color="#FFB703", font_size="13px"),
                        rx.text(rating, font_size="12px", font_weight="700", color="#001D3D"),
                        spacing="1",
                        align="center",
                    ),
                    position="absolute",
                    top="12px",
                    right="12px",
                    background="rgba(255,255,255,0.93)",
                    padding="5px 10px",
                    border_radius="999px",
                    box_shadow="0 2px 8px rgba(0,0,0,0.12)",
                ),
                position="relative",
                width="100%",
                overflow="hidden",
            ),

            # Cuerpo de la card
            rx.vstack(
                rx.heading(nombre, size="5", color="#001D3D", font_weight="800"),
                rx.hstack(
                    rx.text("📍", font_size="13px"),
                    rx.text(pais, color="#6B7280", font_size="14px"),
                    spacing="1",
                    align="center",
                ),
                rx.box(height="1px", background="#E5E7EB", width="100%"),
                rx.hstack(
                    rx.vstack(
                        rx.text("Desde", color="#9CA3AF", font_size="12px"),
                        rx.hstack(
                            rx.text(precio, color="#0077B6", font_size="24px", font_weight="900"),
                            rx.text("USD", color="#0077B6", font_size="12px", font_weight="700", padding_top="6px"),
                            spacing="1",
                            align="end",
                        ),
                        spacing="0",
                        align="start",
                    ),
                    rx.spacer(),
                    rx.link(
                    rx.button(
                    "Ver detalles",
                background="#0077B6",
                color="white",
                 border_radius="12px",
                padding="10px 20px",
                font_size="14px",
                font_weight="700",
                border="none",
                cursor="pointer",
                _hover={"background": "#005F8E", "transform": "translateY(-1px)"},
                transition="all 0.2s ease",
                 ),
                href=f"/detalles?destino={nombre.replace('&', 'and')}",
                text_decoration="none",
),
                    width="100%",
                    align="center",
                ),
                spacing="3",
                padding="18px",
                align="start",
                width="100%",
            ),

            spacing="0",
        ),
        background="white",
        border_radius="22px",
        overflow="hidden",
        box_shadow="0 8px 30px rgba(0,0,0,0.10)",
        _hover={"box_shadow": "0 16px 48px rgba(0,0,0,0.16)", "transform": "translateY(-4px)"},
        transition="all 0.25s ease",
    )


def destinos():
    return rx.box(
    navbar("destinos"),

        # — HERO DESTINOS —
        rx.box(
            rx.vstack(
                rx.box(
                    rx.text(
                        "🌍 Explora el Caribe",
                        color="#001D3D",
                        font_size="14px",
                        font_weight="700",
                    ),
                    background="#FFB703",
                    padding="8px 20px",
                    border_radius="999px",
                    box_shadow="0 4px 16px rgba(255,183,3,0.40)",
                ),
                rx.heading(
                    "DESTINOS",
                    color="white",
                    font_size=["42px", "58px", "72px"],
                    font_weight="900",
                    line_height="1",
                    text_shadow="0 4px 24px rgba(0,0,0,0.50)",
                    text_align="center",
                ),
                rx.text(
                    "Explora los destinos más increíbles del Caribe",
                    color="rgba(255,255,255,0.90)",
                    font_size=["16px", "18px", "22px"],
                    font_weight="500",
                    text_align="center",
                    max_width="600px",
                    line_height="1.6",
                ),
                spacing="4",
                align="center",
                gap="16px",
            ),
            height="55vh",
            min_height="400px",
            background="""
            linear-gradient(rgba(0,20,35,0.35), rgba(0,20,35,0.58)),
            url('/hero.png')
            """,
            background_size="cover",
            background_position="center",
            display="flex",
            align_items="center",
            justify_content="center",
            padding_top="160px",
            padding_x="24px",
        ),

        # — GRID DE DESTINOS —
        rx.vstack(
            # Encabezado de seccion
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
                    "Destinos populares",
                    size="8",
                    color="#001D3D",
                    font_weight="900",
                    text_align="center",
                ),
                rx.text(
    DestinosState.busqueda,
    color="red",
    font_weight="900",
),
                rx.text(
                    "Descubre los lugares más visitados del Caribe",
                    color="#6B7280",
                    font_size="17px",
                    text_align="center",
                ),
                spacing="2",
                align="center",
            ),

            rx.grid(

    rx.cond(
        (DestinosState.busqueda == "") | (DestinosState.busqueda.lower() == "punta cana"),
        destino_card("Punta Cana", "República Dominicana", "$299", "4.9", "/puntacana.jpg"),
        rx.box(),
    ),

    rx.cond(
        (DestinosState.busqueda == "") | (DestinosState.busqueda.lower() == "samaná") | (DestinosState.busqueda.lower() == "samana"),
        destino_card("Samaná", "República Dominicana", "$279", "4.8", "/samana.jpg"),
        rx.box(),
    ),

    rx.cond(
        (DestinosState.busqueda == "") | (DestinosState.busqueda.lower() == "aruba"),
        destino_card("Aruba", "Aruba", "$349", "4.7", "/aruba.jpg"),
        rx.box(),
    ),

    rx.cond(
        (DestinosState.busqueda == "") | (DestinosState.busqueda.lower() == "jamaica"),
        destino_card("Jamaica", "Jamaica", "$309", "4.6", "/jamaica.jpg"),
        rx.box(),
    ),

    rx.cond(
        (DestinosState.busqueda == "") | (DestinosState.busqueda.lower() == "cartagena"),
        destino_card("Cartagena", "Colombia", "$269", "4.9", "/cartagena.jpg"),
        rx.box(),
    ),

    rx.cond(
        (DestinosState.busqueda == "") | (DestinosState.busqueda.lower() == "san juan"),
        destino_card("San Juan", "Puerto Rico", "$289", "4.8", "/sanjuan.jpg"),
        rx.box(),
    ),

    rx.cond(
        (DestinosState.busqueda == "") | (DestinosState.busqueda.lower() == "cancún") | (DestinosState.busqueda.lower() == "cancun"),
        destino_card("Cancún", "México", "$329", "4.8", "/Cancun.jpg"),
        rx.box(),
    ),

    rx.cond(
        (DestinosState.busqueda == "") | (DestinosState.busqueda.lower() == "bahamas"),
        destino_card("Bahamas", "Bahamas", "$499", "4.9", "/bahamas.jpg"),
        rx.box(),
    ),

   rx.cond(
    (DestinosState.busqueda == "") |
    (DestinosState.busqueda.lower() == "turks & caicos") |
    (DestinosState.busqueda.lower() == "turks and caicos") |
    (DestinosState.busqueda.lower() == "turks caicos"),
    destino_card("Turks & Caicos", "Caribe", "$599", "5.0", "/turksandcaicos.jpg"),
    rx.box(),
),

    rx.cond(
        (DestinosState.busqueda == "") | (DestinosState.busqueda.lower() == "bora bora"),
        destino_card("Bora Bora", "Polinesia Francesa", "$899", "5.0", "/borabora.jpg"),
        rx.box(),
    ),

    rx.cond(
        (DestinosState.busqueda == "") | (DestinosState.busqueda.lower() == "maldivas"),
        destino_card("Maldivas", "Maldivas", "$999", "5.0", "/maldivas.jpg"),
        rx.box(),
    ),

    rx.cond(
        (DestinosState.busqueda == "") | (DestinosState.busqueda.lower() == "puerto rico"),
        destino_card("Puerto Rico", "Puerto Rico", "$289", "4.8", "/puertorico.jpg"),
        rx.box(),
    ),

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

        footer(),

       
    )