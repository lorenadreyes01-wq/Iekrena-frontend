import reflex as rx
from Iekrena_frontend.components.navbar import navbar
from Iekrena_frontend.components.footer import footer


EXPERIENCIAS_POR_DESTINO: dict[str, list[str]] = {
    "Punta Cana":    ["Playa Bávaro", "Paseo en catamarán", "Snorkeling", "Cena frente al mar", "Fiesta en resort"],
    "Samaná":        ["Salto El Limón", "Cayo Levantado", "Avistamiento de ballenas", "Tour ecológico", "Paseo en bote"],
    "Aruba":         ["Flamingo Beach", "Eagle Beach", "Jeep Safari", "Snorkeling", "Atardecer en catamarán"],
    "Jamaica":       ["Dunn's River Falls", "Tour Reggae", "Blue Mountains", "Rafting en río", "Tour gastronómico"],
    "Cartagena":     ["Ciudad Amurallada", "Islas del Rosario", "Tour histórico", "Atardecer en murallas", "Paseo en barco"],
    "San Juan":      ["Viejo San Juan", "Castillo El Morro", "Vida nocturna", "Tour gastronómico", "Playa Condado"],
    "Cancún":        ["Xcaret", "Cenotes", "Chichén Itzá", "Catamarán Isla Mujeres", "Snorkeling"],
    "Bahamas":       ["Pig Beach", "Buceo", "Paseo en yate", "Tour de islas", "Snorkeling"],
    "Turks & Caicos":["Grace Bay", "Yate privado", "Buceo", "Paseo en kayak", "Tour premium"],
    "Bora Bora":     ["Lagoon Tour", "Villa sobre el agua", "Cena romántica", "Snorkeling premium", "Spa de lujo"],
    "Maldivas":      ["Water Villa", "Spa Maldives", "Cena privada", "Snorkeling", "Tour en lancha"],
    "Puerto Rico":   ["Viejo San Juan", "Bahía Bioluminiscente", "El Yunque", "Tour cultural", "Playa Flamenco"],
}

PRECIO_EXPERIENCIA: int = 50  # precio fijo por experiencia adicional


class ReservaState(rx.State):

    nombre_completo: str = ""
    email: str = ""
    telefono: str = ""

    destino: str = "Punta Cana"
    experiencias: list[str] = []
    personas: int = 1
    metodo_pago: str = "Tarjeta"

    # Tarjeta
    numero_tarjeta: str = ""
    nombre_tarjeta: str = ""
    vencimiento: str = ""
    cvv: str = ""

    # PayPal
    email_paypal: str = ""

    precios_destinos: dict[str, int] = {
        "Punta Cana": 299,
        "Samaná": 279,
        "Aruba": 349,
        "Jamaica": 309,
        "Cartagena": 269,
        "San Juan": 289,
        "Cancún": 329,
        "Bahamas": 499,
        "Turks & Caicos": 599,
        "Bora Bora": 899,
        "Maldivas": 999,
        "Puerto Rico": 289,
    }

    precios_experiencias: dict[str, int] = {}

    def set_destino(self, value: str):
        self.destino = value
        self.experiencias = []  # reset al cambiar destino

    def set_metodo_pago(self, value: str):
        self.metodo_pago = value
    
    def set_nombre_completo(self, value: str):
        self.nombre_completo = value

    def set_email(self, value: str):
        self.email = value

    def set_telefono(self, value: str):
        self.telefono = value
        

    def set_personas(self, value: str):
        try:
            self.personas = max(1, int(value))
        except:
            self.personas = 1

    def toggle_experiencia(self, exp: str):
        if exp in self.experiencias:
            self.experiencias = [e for e in self.experiencias if e != exp]
        else:
            self.experiencias = self.experiencias + [exp]

    def set_numero_tarjeta(self, v: str): self.numero_tarjeta = v
    def set_nombre_tarjeta(self, v: str): self.nombre_tarjeta = v
    def set_vencimiento(self, v: str): self.vencimiento = v
    def set_cvv(self, v: str): self.cvv = v
    def set_email_paypal(self, v: str): self.email_paypal = v

    @rx.var
    def experiencias_del_destino(self) -> list[str]:
        return EXPERIENCIAS_POR_DESTINO.get(self.destino, [])

    @rx.var
    def precio_total(self) -> str:
        base = self.precios_destinos.get(self.destino, 0)
        extras = len(self.experiencias) * PRECIO_EXPERIENCIA
        total = (base + extras) * self.personas
        return f"${total} USD"

    @rx.var
    def experiencias_texto(self) -> str:
        if not self.experiencias:
            return "Ninguna seleccionada"
        return ", ".join(self.experiencias)
    
    def confirmar_reserva(self):
        import requests

        datos = {
            "nombre_completo": self.nombre_completo,
            "email": self.email,
            "telefono": self.telefono,
            "pais": "República Dominicana",
            "destino": self.destino,
            "fecha_viaje": "2026-07-10",
            "cantidad_personas": self.personas,
            "metodo_pago": self.metodo_pago,
            "total": self.precio_total,
        }

        respuesta = requests.post(
            "http://127.0.0.1:8001/reservas",
            json=datos
        )

        if respuesta.status_code == 200:
            return rx.toast.success("Reserva guardada correctamente")
        else:
            return rx.toast.error("Error al guardar la reserva")
    

    
   


# ── Helpers ──────────────────────────────────────────────────────────────────

def campo(label: str, placeholder: str, on_change=None, tipo: str = "text", value=None):
    return rx.vstack(
        rx.text(label, color="#374151", font_size="13px", font_weight="700"),
        rx.el.input(
            placeholder=placeholder,
            type=tipo,
            on_change=on_change,
            value=value,
            style={
                "width": "100%",
                "height": "48px",
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


def exp_chip(nombre: str):
    selected = ReservaState.experiencias.contains(nombre)
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(nombre, font_size="14px", font_weight="700",
                        color=rx.cond(selected, "white", "#001D3D")),
                rx.text(f"+${PRECIO_EXPERIENCIA}", font_size="12px",
                        color=rx.cond(selected, "rgba(255,255,255,0.80)", "#0077B6")),
                spacing="0",
                align="start",
            ),
            rx.spacer(),
            rx.box(
                rx.cond(selected, rx.text("✓", color="white", font_size="13px", font_weight="900"), rx.text("")),
                width="22px",
                height="22px",
                border_radius="999px",
                background=rx.cond(selected, "#FFB703", "#E5E7EB"),
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            width="100%",
            align="center",
        ),
        background=rx.cond(selected, "#0077B6", "white"),
        border="2px solid",
        border_color=rx.cond(selected, "#0077B6", "#E5E7EB"),
        border_radius="14px",
        padding="14px 16px",
        cursor="pointer",
        on_click=ReservaState.toggle_experiencia(nombre),
        _hover={"border_color": "#0077B6", "box_shadow": "0 4px 12px rgba(0,119,182,0.15)"},
        transition="all 0.2s ease",
        width="100%",
    )


def pago_tarjeta():
    return rx.vstack(
        rx.grid(
            campo("Número de tarjeta", "1234 5678 9012 3456",
                  ReservaState.set_numero_tarjeta, value=ReservaState.numero_tarjeta),
            campo("Nombre en la tarjeta", "Como aparece en la tarjeta",
                  ReservaState.set_nombre_tarjeta, value=ReservaState.nombre_tarjeta),
            columns="1",
            spacing="3",
            width="100%",
        ),
        rx.grid(
            campo("Vencimiento", "MM/AA",
                  ReservaState.set_vencimiento, value=ReservaState.vencimiento),
            campo("CVV", "123",
                  ReservaState.set_cvv, value=ReservaState.cvv),
            columns="2",
            spacing="3",
            width="100%",
        ),
        spacing="3",
        width="100%",
    )


def pago_paypal():
    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.text("🔵", font_size="28px"),
                rx.vstack(
                    rx.text("Pagar con PayPal", font_weight="800", color="#003087", font_size="16px"),
                    rx.text("Serás redirigido a PayPal para completar el pago de forma segura.",
                            color="#6B7280", font_size="13px"),
                    spacing="1",
                    align="start",
                ),
                spacing="3",
                align="center",
            ),
            background="#F0F4FF",
            border="1.5px solid #C7D7F5",
            border_radius="14px",
            padding="16px",
            width="100%",
        ),
        campo("Correo de PayPal", "correo@paypal.com",
              ReservaState.set_email_paypal, value=ReservaState.email_paypal),
        spacing="3",
        width="100%",
    )


def pago_oficina():
    return rx.box(
        rx.hstack(
            rx.text("🏢", font_size="28px"),
            rx.vstack(
                rx.text("Pago en oficina", font_weight="800", color="#001D3D", font_size="16px"),
                rx.text("Visítanos en Santo Domingo, RD. Recibirás un correo con los detalles de tu reserva para finalizar el pago presencialmente.",
                        color="#6B7280", font_size="13px", line_height="1.6"),
                spacing="1",
                align="start",
            ),
            spacing="3",
            align="start",
        ),
        background="#FFFBEB",
        border="1.5px solid #FDE68A",
        border_radius="14px",
        padding="16px",
        width="100%",
    )


# ── Page ─────────────────────────────────────────────────────────────────────

def reservas():
    return rx.box(
        navbar("reservas"),

        # HERO
        rx.box(
            rx.vstack(
                rx.box(
                    rx.text("✈️  Planifica tu aventura", color="#001D3D", font_size="14px", font_weight="700"),
                    background="#FFB703",
                    padding="8px 20px",
                    border_radius="999px",
                    box_shadow="0 4px 16px rgba(255,183,3,0.40)",
                ),
                rx.heading(
                    "Reserva tu viaje",
                    color="white",
                    font_size=["40px", "56px", "68px"],
                    font_weight="900",
                    text_align="center",
                    text_shadow="0 4px 24px rgba(0,0,0,0.50)",
                    line_height="1",
                ),
                rx.text(
                    "Elige destino, experiencias y método de pago para tu reserva.",
                    color="rgba(255,255,255,0.88)",
                    font_size=["15px", "18px", "21px"],
                    text_align="center",
                    max_width="580px",
                    line_height="1.6",
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

        # FORMULARIO
        rx.box(
            rx.grid(

                # ── COLUMNA IZQUIERDA: formulario ────────────────────────────
                rx.vstack(

                    # Sección 1: Datos de contacto
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.box(
                                    rx.text("1", color="white", font_weight="900", font_size="14px"),
                                    width="30px", height="30px", border_radius="999px",
                                    background="#0077B6",
                                    display="flex", align_items="center", justify_content="center",
                                ),
                                rx.heading("Datos de contacto", color="#001D3D", size="6"),
                                spacing="3", align="center",
                            ),
                           rx.grid(
    campo(
        "Nombre completo",
        "Tu nombre completo",
        ReservaState.set_nombre_completo,
        value=ReservaState.nombre_completo
    ),
    campo(
        "Correo electrónico",
        "correo@ejemplo.com",
        ReservaState.set_email,
        tipo="email",
        value=ReservaState.email
    ),
    columns="2",
    spacing="3",
    width="100%",
),
                            campo(
    "Teléfono",
    "+1 (809) 000-0000",
    ReservaState.set_telefono,
    tipo="tel",
    value=ReservaState.telefono
),
                            spacing="4",
                            align="start",
                            width="100%",
                        ),
                        background="white",
                        padding="28px",
                        border_radius="22px",
                        box_shadow="0 8px 30px rgba(0,0,0,0.08)",
                        width="100%",
                    ),

                    # Sección 2: Detalles del viaje
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.box(
                                    rx.text("2", color="white", font_weight="900", font_size="14px"),
                                    width="30px", height="30px", border_radius="999px",
                                    background="#0077B6",
                                    display="flex", align_items="center", justify_content="center",
                                ),
                                rx.heading("Detalles del viaje", color="#001D3D", size="6"),
                                spacing="3", align="center",
                            ),
                            rx.vstack(
                                rx.text("Destino", color="#374151", font_size="13px", font_weight="700"),
                                rx.select(
                                    ["Punta Cana", "Samaná", "Aruba", "Jamaica", "Cartagena",
                                     "San Juan", "Cancún", "Bahamas", "Turks & Caicos",
                                     "Bora Bora", "Maldivas", "Puerto Rico"],
                                    value=ReservaState.destino,
                                    on_change=ReservaState.set_destino,
                                    width="100%",
                                ),
                                spacing="1", align="start", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Cantidad de personas", color="#374151", font_size="13px", font_weight="700"),
                                rx.el.input(
                                    type="number",
                                    value=ReservaState.personas,
                                    on_change=ReservaState.set_personas,
                                    style={
                                        "width": "100%", "height": "48px",
                                        "border": "1.5px solid #E5E7EB",
                                        "border_radius": "12px", "padding": "0 16px",
                                        "font_size": "15px", "color": "#111827",
                                        "background": "#F9FAFB", "outline": "none",
                                    },
                                ),
                                spacing="1", align="start", width="100%",
                            ),
                            spacing="4", align="start", width="100%",
                        ),
                        background="white",
                        padding="28px",
                        border_radius="22px",
                        box_shadow="0 8px 30px rgba(0,0,0,0.08)",
                        width="100%",
                    ),

                    # Sección 3: Experiencias (multi-select chips)
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.box(
                                    rx.text("3", color="white", font_weight="900", font_size="14px"),
                                    width="30px", height="30px", border_radius="999px",
                                    background="#0077B6",
                                    display="flex", align_items="center", justify_content="center",
                                ),
                                rx.heading("Experiencias adicionales", color="#001D3D", size="6"),
                                spacing="3", align="center",
                            ),
                            rx.text(
                                "Selecciona una o más experiencias para tu viaje (opcional)",
                                color="#6B7280", font_size="13px",
                            ),
                            rx.grid(
                                rx.foreach(
                                    ReservaState.experiencias_del_destino,
                                    lambda exp: exp_chip(exp),
                                ),
                                columns="2",
                                spacing="3",
                                width="100%",
                            ),
                            spacing="4", align="start", width="100%",
                        ),
                        background="white",
                        padding="28px",
                        border_radius="22px",
                        box_shadow="0 8px 30px rgba(0,0,0,0.08)",
                        width="100%",
                    ),

                    # Sección 4: Pago
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.box(
                                    rx.text("4", color="white", font_weight="900", font_size="14px"),
                                    width="30px", height="30px", border_radius="999px",
                                    background="#0077B6",
                                    display="flex", align_items="center", justify_content="center",
                                ),
                                rx.heading("Método de pago", color="#001D3D", size="6"),
                                spacing="3", align="center",
                            ),

                            # Botones de selección de método
                            rx.hstack(
                                rx.box(
                                    rx.vstack(
                                        rx.text("💳", font_size="22px"),
                                        rx.text("Tarjeta", font_size="13px", font_weight="700",
                                                color=rx.cond(ReservaState.metodo_pago == "Tarjeta", "#0077B6", "#374151")),
                                        spacing="1", align="center",
                                    ),
                                    flex="1",
                                    padding="14px",
                                    border_radius="14px",
                                    border="2px solid",
                                    border_color=rx.cond(ReservaState.metodo_pago == "Tarjeta", "#0077B6", "#E5E7EB"),
                                    background=rx.cond(ReservaState.metodo_pago == "Tarjeta", "#EFF8FF", "white"),
                                    cursor="pointer",
                                    on_click=lambda: ReservaState.set_metodo_pago("Tarjeta"),
                                    text_align="center",
                                    display="flex",
                                    align_items="center",
                                    justify_content="center",
                                    transition="all 0.2s",
                                ),
                                rx.box(
                                    rx.vstack(
                                        rx.text("🔵", font_size="22px"),
                                        rx.text("PayPal", font_size="13px", font_weight="700",
                                                color=rx.cond(ReservaState.metodo_pago == "PayPal", "#0077B6", "#374151")),
                                        spacing="1", align="center",
                                    ),
                                    flex="1",
                                    padding="14px",
                                    border_radius="14px",
                                    border="2px solid",
                                    border_color=rx.cond(ReservaState.metodo_pago == "PayPal", "#0077B6", "#E5E7EB"),
                                    background=rx.cond(ReservaState.metodo_pago == "PayPal", "#EFF8FF", "white"),
                                    cursor="pointer",
                                    on_click=lambda: ReservaState.set_metodo_pago("PayPal"),
                                    text_align="center",
                                    display="flex",
                                    align_items="center",
                                    justify_content="center",
                                    transition="all 0.2s",
                                ),
                                rx.box(
                                    rx.vstack(
                                        rx.text("🏢", font_size="22px"),
                                        rx.text("Oficina", font_size="13px", font_weight="700",
                                                color=rx.cond(ReservaState.metodo_pago == "Pago en oficina", "#0077B6", "#374151")),
                                        spacing="1", align="center",
                                    ),
                                    flex="1",
                                    padding="14px",
                                    border_radius="14px",
                                    border="2px solid",
                                    border_color=rx.cond(ReservaState.metodo_pago == "Pago en oficina", "#0077B6", "#E5E7EB"),
                                    background=rx.cond(ReservaState.metodo_pago == "Pago en oficina", "#EFF8FF", "white"),
                                    cursor="pointer",
                                    on_click=lambda: ReservaState.set_metodo_pago("Pago en oficina"),
                                    text_align="center",
                                    display="flex",
                                    align_items="center",
                                    justify_content="center",
                                    transition="all 0.2s",
                                ),
                                spacing="3",
                                width="100%",
                            ),

                            # Campos según método
                            rx.cond(ReservaState.metodo_pago == "Tarjeta", pago_tarjeta(), rx.box()),
                            rx.cond(ReservaState.metodo_pago == "PayPal", pago_paypal(), rx.box()),
                            rx.cond(ReservaState.metodo_pago == "Pago en oficina", pago_oficina(), rx.box()),

                            spacing="4", align="start", width="100%",
                        ),
                        background="white",
                        padding="28px",
                        border_radius="22px",
                        box_shadow="0 8px 30px rgba(0,0,0,0.08)",
                        width="100%",
                    ),

                    # Notas y botón confirmar
                    rx.box(
                        rx.vstack(
                            rx.text("Notas adicionales", color="#374151", font_size="13px", font_weight="700"),
                            rx.text_area(
                                placeholder="Solicitudes especiales, alergias, preferencias...",
                                width="100%",
                                height="110px",
                                border_radius="12px",
                                border="1.5px solid #E5E7EB",
                                background="#F9FAFB",
                                color="#111827",
                                font_size="15px",
                                padding="12px 16px",
                            ),
                            rx.button(
                                rx.hstack(
                                    rx.text("✈️", font_size="18px"),
                                    rx.text("Confirmar reserva", font_size="16px", font_weight="900"),
                                    spacing="2", align="center",
                                ),
                                on_click=ReservaState.confirmar_reserva,
                                background="linear-gradient(135deg, #FFD166, #FFB703)",
                                color="#001D3D",
                                width="100%",
                                height="56px",
                                border_radius="16px",
                                border="none",
                                cursor="pointer",
                                box_shadow="0 6px 20px rgba(255,183,3,0.40)",
                                _hover={"transform": "translateY(-2px)", "box_shadow": "0 10px 28px rgba(255,183,3,0.55)"},
                                transition="all 0.2s",
                            ),
                            spacing="3", align="start", width="100%",
                        ),
                        background="white",
                        padding="28px",
                        border_radius="22px",
                        box_shadow="0 8px 30px rgba(0,0,0,0.08)",
                        width="100%",
                    ),

                    spacing="5",
                    align="start",
                    width="100%",
                ),

                # ── COLUMNA DERECHA: resumen ─────────────────────────────────
                rx.vstack(
                    # Resumen del viaje
                    rx.box(
                        rx.vstack(
                            rx.heading("Resumen del viaje", color="white", size="6"),
                            rx.box(height="1px", background="rgba(255,255,255,0.18)", width="100%"),

                            rx.vstack(
                                rx.text("Destino", color="rgba(255,255,255,0.65)", font_size="12px", font_weight="700", letter_spacing="0.08em"),
                                rx.heading(ReservaState.destino, color="#FFB703", size="6"),
                                spacing="0", align="start",
                            ),

                            rx.vstack(
                                rx.text("Experiencias", color="rgba(255,255,255,0.65)", font_size="12px", font_weight="700", letter_spacing="0.08em"),
                                rx.text(ReservaState.experiencias_texto, color="white", font_size="15px", font_weight="600", line_height="1.5"),
                                spacing="0", align="start",
                            ),

                            rx.grid(
                                rx.vstack(
                                    rx.text("Personas", color="rgba(255,255,255,0.65)", font_size="12px", font_weight="700", letter_spacing="0.08em"),
                                    rx.heading(ReservaState.personas, color="white", size="5"),
                                    spacing="0", align="start",
                                ),
                                rx.vstack(
                                    rx.text("Pago", color="rgba(255,255,255,0.65)", font_size="12px", font_weight="700", letter_spacing="0.08em"),
                                    rx.heading(ReservaState.metodo_pago, color="white", size="5"),
                                    spacing="0", align="start",
                                ),
                                columns="2", spacing="4", width="100%",
                            ),

                            rx.box(height="1px", background="rgba(255,255,255,0.18)", width="100%"),

                            rx.vstack(
                                rx.text("TOTAL ESTIMADO", color="rgba(255,255,255,0.65)", font_size="12px", font_weight="700", letter_spacing="0.10em"),
                                rx.heading(ReservaState.precio_total, color="#FFB703", font_size="52px", font_weight="900", line_height="1"),
                                rx.text("Impuestos y tasas incluidos", color="rgba(255,255,255,0.50)", font_size="12px"),
                                spacing="1", align="start",
                            ),

                            spacing="5",
                            align="start",
                            width="100%",
                        ),
                        background="linear-gradient(135deg, rgba(0,29,61,0.92), rgba(0,60,100,0.88)), url('/hero.png')",
                        background_size="cover",
                        background_position="center",
                        padding="32px",
                        border_radius="22px",
                        box_shadow="0 12px 40px rgba(0,0,0,0.20)",
                        width="100%",
                    ),

                    # Info experiencias disponibles
                    rx.box(
                        rx.vstack(
                            rx.heading("¿Qué incluye tu viaje?", color="#001D3D", size="5", font_weight="800"),
                            rx.text("Todas las reservas incluyen:", color="#6B7280", font_size="13px"),
                            rx.vstack(
                                *[
                                    rx.hstack(
                                        rx.box(width="6px", height="6px", border_radius="999px", background="#0077B6", flex_shrink="0"),
                                        rx.text(item, font_size="14px", color="#374151"),
                                        spacing="2", align="center",
                                    )
                                    for item in [
                                        "Traslado aeropuerto – hotel",
                                        "Seguro de viaje básico",
                                        "Atención 24/7 en destino",
                                        "Confirmación inmediata",
                                    ]
                                ],
                                spacing="2",
                                align="start",
                            ),
                            spacing="3",
                            align="start",
                            width="100%",
                        ),
                        background="white",
                        padding="26px",
                        border_radius="22px",
                        box_shadow="0 8px 30px rgba(0,0,0,0.08)",
                        width="100%",
                    ),

                    spacing="5",
                    align="start",
                    position="sticky",
                    top="100px",
                ),

                columns="2",
                spacing="7",
                width="100%",
                max_width="1200px",
            ),
            background="#F1F5F9",
            padding="70px 50px",
            display="flex",
            justify_content="center",
        ),

        footer(),
    )