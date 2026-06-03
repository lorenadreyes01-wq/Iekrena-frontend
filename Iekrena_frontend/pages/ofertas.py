import reflex as rx
from Iekrena_frontend.components.navbar import navbar
from Iekrena_frontend.components.footer import footer
 
 
def oferta_card(nombre, pais, imagen, antes, ahora, descuento):
    return rx.box(
        rx.vstack(
            rx.box(
                rx.image(
                    src=imagen,
                    width="100%",
                    height="210px",
                    object_fit="cover",
                ),
                rx.box(
                    descuento,
                    position="absolute",
                    top="14px",
                    left="14px",
                    background="#FFB703",
                    color="#001D3D",
                    padding="7px 14px",
                    border_radius="999px",
                    font_weight="900",
                ),
                position="relative",
                width="100%",
            ),
 
            rx.vstack(
                rx.heading(nombre, size="5", color="#001D3D", font_weight="900"),
                rx.text(pais, color="#6B7280"),
 
                rx.hstack(
                    rx.text(
                        antes,
                        color="#9CA3AF",
                        text_decoration="line-through",
                        font_size="18px",
                    ),
                    rx.text(
                        ahora,
                        color="#FFB703",
                        font_size="28px",
                        font_weight="900",
                    ),
                    rx.text("USD", color="#001D3D", font_weight="800"),
                    align="end",
                ),
 
                rx.link(
                    rx.button(
                        "Ver oferta",
                        background="transparent",
                        color="#0077B6",
                        border="1px solid #FFB703",
                        border_radius="999px",
                        width="100%",
                        height="42px",
                        font_weight="800",
                    ),
                    href="/detalles",
                    width="100%",
                ),
 
                spacing="3",
                padding="18px",
                align="start",
            ),
 
            spacing="0",
        ),
        background="white",
        border_radius="22px",
        overflow="hidden",
        box_shadow="0 12px 34px rgba(0,0,0,0.12)",
    )
 
 
def premium_card(nombre, texto, imagen, precio):
    return rx.box(
        rx.box(
            rx.image(
                src=imagen,
                width="100%",
                height="250px",
                object_fit="cover",
            ),
 
            rx.box(
                "LUXURY",
                position="absolute",
                top="16px",
                left="16px",
                background="rgba(0,0,0,0.75)",
                color="#FFB703",
                padding="8px 14px",
                border_radius="10px",
                font_weight="900",
            ),
 
            rx.vstack(
                rx.heading(nombre, color="white", size="5", font_weight="900"),
                rx.text(texto, color="rgba(255,255,255,0.85)"),
 
                rx.hstack(
                    rx.text("Desde", color="#FFB703"),
                    rx.text(
                        precio,
                        color="#FFB703",
                        font_size="26px",
                        font_weight="900",
                    ),
                    rx.text("USD", color="white"),
                    align="end",
                ),
 
                rx.link(
                    rx.button(
                        "Ver oferta",
                        background="transparent",
                        color="white",
                        border="1px solid #FFB703",
                        border_radius="999px",
                        width="100%",
                        height="40px",
                        font_weight="800",
                    ),
                    href="/detalles",
                    width="100%",
                ),
 
                spacing="2",
                align="start",
                position="absolute",
                bottom="18px",
                left="18px",
                right="18px",
            ),
 
            position="relative",
            border_radius="22px",
            overflow="hidden",
        ),
        box_shadow="0 12px 34px rgba(0,0,0,0.18)",
    )
 
 
def ofertas():
    return rx.box(
        navbar("ofertas"),
 
        # HERO
        rx.box(
            rx.vstack(
                rx.heading(
                    "OFERTAS",
                    color="white",
                    font_size="70px",
                    font_weight="900",
                    line_height="1",
                    text_shadow="0 5px 25px rgba(0,0,0,0.55)",
                ),
 
                rx.heading(
                    "EXCLUSIVAS",
                    color="#FFB703",
                    font_size="70px",
                    font_weight="900",
                    line_height="1",
                    text_shadow="0 5px 25px rgba(0,0,0,0.45)",
                ),
 
                rx.text(
                    "Hasta un 40% de descuento en los mejores destinos del Caribe.",
                    color="white",
                    font_size="22px",
                    max_width="560px",
                    line_height="1.5",
                ),
 
                rx.link(
                    rx.button(
                        "Ver ofertas",
                        background="#FFB703",
                        color="#001D3D",
                        border_radius="999px",
                        height="52px",
                        padding="0 34px",
                        font_weight="900",
                        box_shadow="0 8px 24px rgba(255,183,3,0.35)",
                    ),
                    href="/detalles",
                ),
 
                spacing="3",
                align="start",
                max_width="1200px",
                width="100%",
            ),
 
            min_height="78vh",
            background=(
                "linear-gradient(90deg, rgba(0,15,35,.78), rgba(0,15,35,.25)),"
                "url('/offer_hero.png')"
            ),
            background_size="cover",
            background_position="center",
            display="flex",
            align_items="center",
            justify_content="center",
            padding="160px 60px 80px 60px",
        ),
 
        # OFERTAS DESTACADAS
        rx.vstack(
            rx.heading(
                "OFERTAS DESTACADAS",
                size="8",
                color="#001D3D",
                font_weight="900",
            ),
 
            rx.text(
                "Descuentos por tiempo limitado",
                color="#6B7280",
            ),
 
            rx.grid(
                oferta_card("PUNTA CANA", "República Dominicana", "/puntacana.offer.png", "$499", "$299", "-40%"),
                oferta_card("ARUBA", "Aruba", "/aruba_offer.png", "$699", "$449", "-36%"),
                oferta_card("BAHAMAS", "Bahamas", "/bahamas_offer.jpg", "$899", "$599", "-33%"),
                oferta_card("CANCÚN", "México", "/cancun_offer.jpg", "$599", "$379", "-37%"),
                oferta_card("SAMANÁ", "República Dominicana", "/samana.jpg", "$549", "$385", "-30%"),
                oferta_card("JAMAICA", "Jamaica", "/jamaica.jpg", "$699", "$499", "-28%"),
                columns="3",
                spacing="6",
                width="100%",
            ),
 
            spacing="5",
            padding="70px 60px",
            background="#F8FAFC",
            align="center",
        ),
 
        # ULTIMAS PLAZAS
        rx.box(
            rx.hstack(
                rx.image(
                    src="/clock.png",
                    width="100px",
                    height="100px",
                    object_fit="contain",
                ),
 
                rx.vstack(
                    rx.heading("¡ÚLTIMAS PLAZAS!", color="white", size="6"),
                    rx.text(
                        "No te quedes sin tu viaje.",
                        color="rgba(255,255,255,0.80)",
                    ),
                    align="start",
                ),
 
                rx.spacer(),
 
                rx.hstack(
                    rx.vstack(
                        rx.heading("02", color="#FFB703", size="8"),
                        rx.text("DÍAS", color="white"),
                    ),
                    rx.vstack(
                        rx.heading("14", color="#FFB703", size="8"),
                        rx.text("HORAS", color="white"),
                    ),
                    rx.vstack(
                        rx.heading("37", color="#FFB703", size="8"),
                        rx.text("MINUTOS", color="white"),
                    ),
                    rx.vstack(
                        rx.heading("58", color="#FFB703", size="8"),
                        rx.text("SEGUNDOS", color="white"),
                    ),
                    spacing="8",
                ),
 
                max_width="1200px",
                width="100%",
                align="center",
            ),
 
            background="#001D3D",
            padding="35px 60px",
        ),
 
        # OFERTAS PREMIUM
        rx.vstack(
            rx.heading(
                "OFERTAS PREMIUM",
                size="8",
                color="#001D3D",
                font_weight="900",
            ),
 
            rx.text(
                "Destinos de lujo para experiencias inolvidables",
                color="#6B7280",
            ),
 
            rx.grid(
                premium_card("TURKS & CAICOS", "Paraíso exclusivo", "/turks_offer.jpg", "$1,299"),
                premium_card("MALDIVAS", "Lujo en su máxima expresión", "/maldives_offer.jpg", "$2,199"),
                premium_card("BORA BORA", "El sueño hecho realidad", "/borabora_offer.jpg", "$2,499"),
                columns="3",
                spacing="6",
                width="100%",
            ),
 
            spacing="5",
            padding="70px 60px",
            background="#F8FAFC",
            align="center",
        ),
 
        footer(),
    )