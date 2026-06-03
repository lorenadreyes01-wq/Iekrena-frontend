import reflex as rx
from Iekrena_frontend.components.navbar import navbar
from Iekrena_frontend.components.footer import footer


class ContactoState(rx.State):
    nombre: str = ""
    correo: str = ""
    asunto: str = ""
    mensaje: str = ""
    enviado: bool = False

    def set_nombre(self, v: str):  self.nombre = v
    def set_correo(self, v: str):  self.correo = v
    def set_asunto(self, v: str):  self.asunto = v
    def set_mensaje(self, v: str): self.mensaje = v

    def enviar(self):
        if self.nombre and self.correo and self.mensaje:
            # Aquí conectas tu API backend con POST /contacto
            self.enviado = True

    def resetear(self):
        self.nombre = ""
        self.correo = ""
        self.asunto = ""
        self.mensaje = ""
        self.enviado = False


# ── Helpers ──────────────────────────────────────────────────────────────────

def campo(label: str, placeholder: str, value, on_change, tipo: str = "text"):
    return rx.vstack(
        rx.text(label, color="#374151", font_size="13px", font_weight="700"),
        rx.el.input(
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            type=tipo,
            style={
                "width": "100%",
                "height": "50px",
                "border": "1.5px solid #E5E7EB",
                "border_radius": "12px",
                "padding": "0 16px",
                "font_size": "15px",
                "color": "#111827",
                "background": "#F9FAFB",
                "outline": "none",
                "transition": "border 0.2s",
            },
        ),
        spacing="1",
        align="start",
        width="100%",
    )


def info_card(emoji: str, titulo: str, linea1: str, linea2: str = ""):
    return rx.box(
        rx.vstack(
            rx.box(
                rx.text(emoji, font_size="26px"),
                width="60px",
                height="60px",
                border_radius="16px",
                background="linear-gradient(135deg, #E0F7FA, #B3E5FC)",
                display="flex",
                align_items="center",
                justify_content="center",
                box_shadow="0 6px 18px rgba(0,119,182,0.16)",
            ),
            rx.text(titulo, color="#9CA3AF", font_size="12px", font_weight="700", letter_spacing="0.08em"),
            rx.text(linea1, color="#001D3D", font_size="15px", font_weight="800"),
            rx.cond(
                linea2 != "",
                rx.text(linea2, color="#6B7280", font_size="13px"),
                rx.box(),
            ),
            spacing="1",
            align="start",
        ),
        background="white",
        padding="22px",
        border_radius="20px",
        box_shadow="0 4px 20px rgba(0,0,0,0.07)",
        _hover={"box_shadow": "0 8px 28px rgba(0,0,0,0.11)", "transform": "translateY(-2px)"},
        transition="all 0.2s",
        width="100%",
    )


def social_btn(emoji: str, nombre: str, color: str, href: str = "#"):
    return rx.link(
        rx.hstack(
            rx.text(emoji, font_size="18px"),
            rx.text(nombre, font_size="13px", font_weight="700", color="white"),
            spacing="2",
            align="center",
        ),
        href=href,
        display="flex",
        align_items="center",
        justify_content="center",
        background=color,
        border_radius="12px",
        padding="10px 16px",
        text_decoration="none",
        _hover={"opacity": "0.85", "transform": "translateY(-1px)"},
        transition="all 0.2s",
    )


# ── Page ─────────────────────────────────────────────────────────────────────

def contacto():
    return rx.box(
        navbar("contacto"),

        # HERO
        rx.box(
            rx.vstack(
                rx.box(
                    rx.text("💬  Estamos para ayudarte", color="#001D3D", font_size="14px", font_weight="700"),
                    background="#FFB703",
                    padding="8px 20px",
                    border_radius="999px",
                    box_shadow="0 4px 16px rgba(255,183,3,0.40)",
                ),
                rx.heading(
                    "Contáctanos",
                    color="white",
                    font_size=["42px", "58px", "72px"],
                    font_weight="900",
                    text_align="center",
                    text_shadow="0 4px 24px rgba(0,0,0,0.50)",
                    line_height="1",
                ),
                rx.text(
                    "¿Tienes dudas sobre destinos, reservas u ofertas? Escríbenos y te ayudamos.",
                    color="rgba(255,255,255,0.88)",
                    font_size=["15px", "18px", "20px"],
                    text_align="center",
                    max_width="620px",
                    line_height="1.65",
                ),
                spacing="4",
                align="center",
                gap="16px",
            ),
            height="52vh",
            min_height="380px",
            background="linear-gradient(rgba(0,20,35,0.45), rgba(0,20,35,0.62)), url('/hero.png')",
            background_size="cover",
            background_position="center",
            display="flex",
            align_items="center",
            justify_content="center",
            padding_top="120px",
            padding_x="24px",
        ),

        # CONTENIDO
        rx.vstack(

            # Info cards
            rx.grid(
                info_card("✉️", "CORREO", "info@iekrenatrips.com", "Respuesta en menos de 24h"),
                info_card("📞", "TELÉFONO", "+1 (809) 000-0000", "Lun–Vie 8AM–6PM"),
                info_card("📍", "UBICACIÓN", "Santo Domingo, RD", "República Dominicana"),
                info_card("🕐", "HORARIO", "Lun–Vie: 8AM – 6PM", "Sáb: 9AM – 2PM"),
                columns="4",
                spacing="4",
                width="100%",
            ),

            # Formulario + info lateral
            rx.grid(

                # Formulario
                rx.box(
                    rx.cond(
                        ContactoState.enviado,

                        # Estado éxito
                        rx.vstack(
                            rx.box(
                                rx.text("✅", font_size="48px"),
                                width="90px", height="90px",
                                border_radius="999px",
                                background="linear-gradient(135deg, #DCFCE7, #BBF7D0)",
                                display="flex", align_items="center", justify_content="center",
                                box_shadow="0 8px 24px rgba(22,163,74,0.20)",
                            ),
                            rx.heading("¡Mensaje enviado!", color="#001D3D", size="7", font_weight="900"),
                            rx.text(
                                "Gracias por escribirnos. Nuestro equipo te responderá pronto.",
                                color="#6B7280", text_align="center", font_size="16px", max_width="360px",
                                line_height="1.6",
                            ),
                            rx.button(
                                "Enviar otro mensaje",
                                on_click=ContactoState.resetear,
                                background="linear-gradient(135deg, #FFD166, #FFB703)",
                                color="#001D3D",
                                border_radius="12px",
                                height="48px",
                                padding="0 28px",
                                border="none",
                                cursor="pointer",
                                font_weight="800",
                                margin_top="8px",
                            ),
                            spacing="4",
                            align="center",
                            width="100%",
                            padding_y="40px",
                        ),

                        # Formulario normal
                        rx.vstack(
                            rx.vstack(
                                rx.text("ESCRÍBENOS", color="#0077B6", font_weight="900",
                                        font_size="12px", letter_spacing="0.10em"),
                                rx.heading("Envíanos un mensaje", color="#001D3D", size="6", font_weight="900"),
                                rx.text(
                                    "Completa el formulario y nuestro equipo te contactará.",
                                    color="#6B7280", font_size="14px",
                                ),
                                spacing="1", align="start",
                            ),
                            rx.grid(
                                campo("Nombre completo", "Tu nombre", ContactoState.nombre, ContactoState.set_nombre),
                                campo("Correo electrónico", "correo@ejemplo.com", ContactoState.correo, ContactoState.set_correo, "email"),
                                columns="2", spacing="3", width="100%",
                            ),
                            campo("Asunto", "¿Sobre qué quieres hablar?", ContactoState.asunto, ContactoState.set_asunto),
                            rx.vstack(
                                rx.text("Mensaje", color="#374151", font_size="13px", font_weight="700"),
                                rx.el.textarea(
                                    placeholder="Escribe tu mensaje aquí...",
                                    value=ContactoState.mensaje,
                                    on_change=ContactoState.set_mensaje,
                                    style={
                                        "width": "100%",
                                        "height": "140px",
                                        "border": "1.5px solid #E5E7EB",
                                        "border_radius": "12px",
                                        "padding": "12px 16px",
                                        "font_size": "15px",
                                        "color": "#111827",
                                        "background": "#F9FAFB",
                                        "outline": "none",
                                        "resize": "none",
                                        "font_family": "inherit",
                                    },
                                ),
                                spacing="1", align="start", width="100%",
                            ),
                            rx.button(
                                rx.hstack(
                                    rx.text("✉️", font_size="18px"),
                                    rx.text("Enviar mensaje", font_size="16px", font_weight="900"),
                                    spacing="2", align="center",
                                ),
                                on_click=ContactoState.enviar,
                                background="linear-gradient(135deg, #FFD166, #FFB703)",
                                color="#001D3D",
                                width="100%",
                                height="54px",
                                border_radius="14px",
                                border="none",
                                cursor="pointer",
                                box_shadow="0 6px 20px rgba(255,183,3,0.40)",
                                _hover={"transform": "translateY(-2px)", "box_shadow": "0 10px 28px rgba(255,183,3,0.55)"},
                                transition="all 0.2s",
                            ),
                            spacing="4", align="start", width="100%",
                        ),
                    ),
                    background="white",
                    padding="34px",
                    border_radius="24px",
                    box_shadow="0 8px 30px rgba(0,0,0,0.08)",
                    width="100%",
                ),

                # Panel lateral
                rx.vstack(
                    rx.box(
                        rx.vstack(
                            rx.heading("IEKRENA TRIPS", color="white", size="6", font_weight="900"),
                            rx.text(
                                "Tu próxima aventura comienza con una conversación. Estamos listos para ayudarte a planificar el viaje de tus sueños.",
                                color="rgba(255,255,255,0.85)",
                                font_size="15px",
                                line_height="1.75",
                            ),
                            rx.box(height="1px", background="rgba(255,255,255,0.18)", width="100%"),
                            rx.text("Síguenos en redes", color="#FFB703", font_weight="800", font_size="13px", letter_spacing="0.08em"),
                            rx.grid(
                                social_btn( "f",  "Facebook","https://facebook.com/iekrenatrips"),
                                social_btn( "📸", "Instagram", "https://instagram.com/iekrenatrips"),
                                social_btn( "💬", "WhatsApp", "https://wa.me/18090000000"),
                                social_btn( "▶️", "YouTube", "https://youtube.com/@iekrenatrips"),
                                columns="2",
                                spacing="2",
                                width="100%",
                            ),
                            rx.box(height="1px", background="rgba(255,255,255,0.18)", width="100%"),
                            rx.text("Atención al cliente", color="#FFB703", font_weight="800", font_size="13px", letter_spacing="0.08em"),
                            rx.vstack(
                                rx.hstack(
                                    rx.text("📞", font_size="14px"),
                                    rx.text("+1 (809) 000-0000", color="white", font_size="14px"),
                                    spacing="2", align="center",
                                ),
                                rx.hstack(
                                    rx.text("✉️", font_size="14px"),
                                    rx.text("info@iekrenatrips.com", color="white", font_size="14px"),
                                    spacing="2", align="center",
                                ),
                                rx.hstack(
                                    rx.text("📍", font_size="14px"),
                                    rx.text("Santo Domingo, RD", color="white", font_size="14px"),
                                    spacing="2", align="center",
                                ),
                                spacing="3", align="start",
                            ),
                            spacing="4", align="start", width="100%",
                        ),
                        background="linear-gradient(135deg, rgba(0,29,61,0.92), rgba(0,60,100,0.88)), url('/hero.png')",
                        background_size="cover",
                        background_position="center",
                        padding="32px",
                        border_radius="24px",
                        box_shadow="0 12px 40px rgba(0,0,0,0.18)",
                        width="100%",
                    ),
                    spacing="4",
                    align="start",
                    position="sticky",
                    top="100px",
                ),

                columns="2",
                spacing="7",
                width="100%",
            ),

            spacing="8",
            padding="70px 60px",
            background="#F1F5F9",
            width="100%",
            align="center",
        ),

        footer(),
    )