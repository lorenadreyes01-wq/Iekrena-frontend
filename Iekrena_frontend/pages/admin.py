import reflex as rx
import requests

from pydantic import BaseModel

class Oferta(BaseModel):
    id: int
    destino: str
    precio_original: str
    precio_oferta: str
    activa: bool


class AdminState(rx.State):
    reservas: list[dict] = []
    ofertas: list[Oferta] = [
        Oferta(id=1, destino="Punta Cana",    precio_original="499",  precio_oferta="299", activa=True),
        Oferta(id=2, destino="Aruba",          precio_original="699",  precio_oferta="449", activa=True),
        Oferta(id=3, destino="Bahamas",        precio_original="899",  precio_oferta="599", activa=True),
        Oferta(id=4, destino="Cancún",         precio_original="599",  precio_oferta="379", activa=True),
        Oferta(id=5, destino="Jamaica",        precio_original="509",  precio_oferta="309", activa=False),
        Oferta(id=6, destino="Bora Bora",      precio_original="1200", precio_oferta="899", activa=True),
        
    ]


    modal_abierto: bool = False
    editando_id: int = -1
    form_destino: str = ""
    form_precio_original: str = ""
    form_precio_oferta: str = ""

    def abrir_nueva(self):
        self.editando_id = -1
        self.form_destino = ""
        self.form_precio_original = ""
        self.form_precio_oferta = ""
        self.modal_abierto = True

    def abrir_editar(self, id: int):
        for o in self.ofertas:
            if o.id == id:
                self.editando_id = id
                self.form_destino = o.destino
                self.form_precio_original = o.precio_original
                self.form_precio_oferta = o.precio_oferta
                self.modal_abierto = True
                break

    def cerrar_modal(self):
        self.modal_abierto = False

    def set_form_destino(self, v: str):         self.form_destino = v
    def set_form_precio_original(self, v: str): self.form_precio_original = v
    def set_form_precio_oferta(self, v: str):   self.form_precio_oferta = v

    def guardar_oferta(self):
        if not self.form_destino or not self.form_precio_oferta:
            return
        if self.editando_id == -1:
            nuevo_id = max((o.id for o in self.ofertas), default=0) + 1
            self.ofertas = self.ofertas + [Oferta(
                id=nuevo_id,
                destino=self.form_destino,
                precio_original=str(self.form_precio_original),
                precio_oferta=str(self.form_precio_oferta),
                activa=True,
            )]
        else:
            self.ofertas = [
                Oferta(
                  id=o.id,
                  destino=self.form_destino,
                  precio_original=str(self.form_precio_original),
                  precio_oferta=str(self.form_precio_oferta),
                  activa=o.activa,
                ) if o.id == self.editando_id else o
                for o in self.ofertas
            ]
        self.modal_abierto = False

    def eliminar_oferta(self, id: int):
        self.ofertas = [o for o in self.ofertas if o.id != id]

    def toggle_activa(self, id: int):
        self.ofertas = [
            Oferta(id=o.id, destino=o.destino, precio_original=o.precio_original,
                   precio_oferta=o.precio_oferta, activa=not o.activa)
            if o.id == id else o
            for o in self.ofertas
        ]

    def cargar_reservas(self):
        try:
            respuesta = requests.get(
                "http://127.0.0.1:8001/reservas"
            )

            if respuesta.status_code == 200:
                self.reservas = respuesta.json()

        except Exception as e:
            print(e)

    @rx.var
    def total_ofertas(self) -> int:
        return len(self.ofertas)
    
    @rx.var
    def ofertas_activas(self) -> int:
        return sum(1 for o in self.ofertas if o.activa)
    
    @rx.var
    def ofertas_activas_lista(self) -> list[Oferta]:
        return [o for o in self.ofertas if o.activa]

    @rx.var
    def total_reservas(self) -> int:
        return len(self.reservas)
    
    @rx.var
    def total_ventas(self) -> str:
        return "$1,196"
        


# ── Helpers ──────────────────────────────────────────────────────────────────

def campo_modal(label: str, placeholder: str, value, on_change, tipo: str = "text"):
    return rx.vstack(
        rx.text(label, font_size="13px", font_weight="700", color="#374151"),
        rx.el.input(
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            type=tipo,
            style={
                "width": "100%", "height": "46px",
                "border": "1.5px solid #E5E7EB",
                "border_radius": "10px",
                "padding": "0 14px",
                "font_size": "15px",
                "color": "#111827",
                "background": "#F9FAFB",
                "outline": "none",
            },
        ),
        spacing="1", align="start", width="100%",
    )


def menu_item(icono: str, texto: str, activo: bool = False):
    return rx.box(
        rx.hstack(
            rx.icon(icono, size=18),
            rx.text(texto, font_weight="700", font_size="14px"),
            spacing="3", align="center",
        ),
        width="100%",
        padding="12px 16px",
        border_radius="12px",
        background="#0077B6" if activo else "transparent",
        color="white" if activo else "rgba(255,255,255,0.72)",
        _hover={"background": "rgba(255,255,255,0.09)", "color": "white"},
        transition="all 0.2s",
        cursor="pointer",
    )


def stat_card(icono: str, titulo: str, valor: str, detalle: str, color: str = "#0077B6"):
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icono, size=20, color=color),
                    width="44px", height="44px",
                    border_radius="12px",
                    background=f"color-mix(in srgb, {color} 12%, white)",
                    display="flex", align_items="center", justify_content="center",
                ),
                rx.spacer(),
                rx.text(detalle, color="#16A34A", font_size="12px", font_weight="700"),
                width="100%", align="center",
            ),
            rx.heading(valor, color="#001D3D", size="8", font_weight="900"),
            rx.text(titulo, color="#64748B", font_size="13px", font_weight="600"),
            spacing="2", align="start",
        ),
        background="white",
        padding="22px",
        border_radius="20px",
        box_shadow="0 4px 20px rgba(0,0,0,0.07)",
        _hover={"box_shadow": "0 8px 28px rgba(0,0,0,0.11)", "transform": "translateY(-2px)"},
        transition="all 0.2s",
    )


def oferta_row(oferta: Oferta):
    return rx.box(
        rx.hstack(
            # Destino
            rx.hstack(
                rx.box(
                    rx.text(oferta.destino[0], color="white", font_weight="900", font_size="14px"),
                    width="38px", height="38px", border_radius="10px",
                    background="#0077B6",
                    display="flex", align_items="center", justify_content="center",
                    flex_shrink="0",
                ),
                rx.text(oferta.destino, font_weight="800", color="#001D3D", font_size="15px"),
                spacing="3", align="center",
            ),
            rx.spacer(),
            # Precio tachado
            rx.text(
                "$" + oferta.precio_original,
                color="#9CA3AF",
                font_size="14px",
                text_decoration="line-through",
            ),
            # Precio oferta
            rx.box(
                rx.text("$" + oferta.precio_oferta + " USD", color="#0077B6", font_weight="900", font_size="15px"),
                background="#EFF8FF",
                padding="4px 12px",
                border_radius="999px",
            ),
            # Badge activa/inactiva
            rx.box(
                rx.text(
                    rx.cond(oferta.activa, "Activa", "Pausada"),
                    font_size="12px",
                    font_weight="700",
                    color=rx.cond(oferta.activa, "#16A34A", "#9CA3AF"),
                ),
                background=rx.cond(oferta.activa, "#DCFCE7", "#F3F4F6"),
                padding="4px 12px",
                border_radius="999px",
                cursor="pointer",
                on_click=AdminState.toggle_activa(oferta.id),
                _hover={"opacity": "0.8"},
            ),
            # Botones
            rx.hstack(
                rx.button(
                    rx.icon("pencil", size=14),
                    on_click=AdminState.abrir_editar(oferta.id),
                    background="#EFF8FF",
                    color="#0077B6",
                    border_radius="10px",
                    padding="8px 12px",
                    border="none",
                    cursor="pointer",
                    _hover={"background": "#0077B6", "color": "white"},
                    transition="all 0.2s",
                ),
                rx.button(
                    rx.icon("trash-2", size=14),
                    on_click=AdminState.eliminar_oferta(oferta.id),
                    background="#FEF2F2",
                    color="#D62828",
                    border_radius="10px",
                    padding="8px 12px",
                    border="none",
                    cursor="pointer",
                    _hover={"background": "#D62828", "color": "white"},
                    transition="all 0.2s",
                ),
                spacing="2",
            ),
            width="100%",
            align="center",
            gap="16px",
        ),
        padding="16px 20px",
        border_radius="14px",
        background="white",
        box_shadow="0 2px 8px rgba(0,0,0,0.05)",
        _hover={"box_shadow": "0 4px 16px rgba(0,0,0,0.09)"},
        transition="all 0.2s",
    )


def modal_oferta():
    return rx.cond(
        AdminState.modal_abierto,
        rx.box(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.heading(
                            rx.cond(AdminState.editando_id == -1, "Nueva oferta", "Editar oferta"),
                            color="#001D3D", size="6",
                        ),
                        rx.spacer(),
                        rx.button(
                            rx.icon("x", size=18),
                            on_click=AdminState.cerrar_modal,
                            background="transparent",
                            color="#6B7280",
                            border="none",
                            cursor="pointer",
                            padding="4px",
                        ),
                        width="100%", align="center",
                    ),
                    rx.box(height="1px", background="#E5E7EB", width="100%"),
                    campo_modal("Destino", "Ej: Punta Cana", AdminState.form_destino, AdminState.set_form_destino),
                    rx.grid(
                        campo_modal("Precio original ($)", "Ej: 499", AdminState.form_precio_original, AdminState.set_form_precio_original, "number"),
                        campo_modal("Precio oferta ($)", "Ej: 299", AdminState.form_precio_oferta, AdminState.set_form_precio_oferta, "number"),
                        columns="2", spacing="3", width="100%",
                    ),
                    rx.hstack(
                        rx.button(
                            "Cancelar",
                            on_click=AdminState.cerrar_modal,
                            background="#F1F5F9",
                            color="#374151",
                            border_radius="12px",
                            height="46px",
                            padding="0 24px",
                            border="none",
                            cursor="pointer",
                            font_weight="700",
                        ),
                        rx.button(
                            rx.hstack(
                                rx.icon("save", size=16),
                                rx.text("Guardar", font_weight="800"),
                                spacing="2", align="center",
                            ),
                            on_click=AdminState.guardar_oferta,
                            background="linear-gradient(135deg, #FFD166, #FFB703)",
                            color="#001D3D",
                            border_radius="12px",
                            height="46px",
                            padding="0 28px",
                            border="none",
                            cursor="pointer",
                            font_weight="900",
                        ),
                        spacing="3", justify="end", width="100%",
                    ),
                    spacing="4", align="start", width="100%",
                ),
                background="white",
                border_radius="24px",
                padding="32px",
                width="500px",
                box_shadow="0 24px 60px rgba(0,0,0,0.22)",
            ),
            position="fixed",
            top="0", left="0", right="0", bottom="0",
            background="rgba(0,0,0,0.45)",
            display="flex",
            align_items="center",
            justify_content="center",
            z_index="1000",
        ),
        rx.box(),
    )


# ── Page ─────────────────────────────────────────────────────────────────────

def admin():
    return rx.box(
        modal_oferta(),

        rx.hstack(

            # SIDEBAR
            rx.box(
                rx.vstack(
                    rx.image(src="/logo.png", width="150px", object_fit="contain"),
                    rx.box(height="1px", background="rgba(255,255,255,0.12)", width="100%"),

                    rx.vstack(
                        menu_item("layout-dashboard", "Dashboard", True),
                        spacing="1",
                        width="100%",
                    ),

                    rx.spacer(),

                    rx.box(height="1px", background="rgba(255,255,255,0.12)", width="100%"),

                    rx.link(
                        rx.hstack(
                            rx.icon("log-out", size=18),
                            rx.text("Volver al inicio", font_weight="700", font_size="14px"),
                            spacing="3", align="center",
                        ),
                        href="/",
                        width="100%",
                        padding="12px 16px",
                        border_radius="12px",
                        color="rgba(255,255,255,0.72)",
                        text_decoration="none",
                        _hover={"background": "rgba(255,255,255,0.09)", "color": "white"},
                        transition="all 0.2s",
                    ),

                    width="100%",
                    height="100%",
                    spacing="4",
                    align="start",
                ),
                width="240px",
                height="100vh",
                background="#001D3D",
                padding="24px 18px",
                position="fixed",
                left="0",
                top="0",
                z_index="100",
            ),

            # CONTENIDO PRINCIPAL
            rx.box(
                rx.vstack(

                    # Header
                    rx.hstack(
                        rx.vstack(
                            rx.text("PANEL ADMINISTRATIVO", color="#0077B6", font_weight="900",
                                    font_size="12px", letter_spacing="0.10em"),
                            rx.heading("Bienvenida, IEKRENA 👋", color="#001D3D", size="7", font_weight="900"),
                            spacing="0", align="start",
                        ),
                        rx.spacer(),
                        rx.box(
                            rx.hstack(
                                rx.box(
                                    rx.text("IL", color="white", font_weight="900", font_size="16px"),
                                    width="42px", height="42px", border_radius="999px",
                                    background="#0077B6",
                                    display="flex", align_items="center", justify_content="center",
                                ),
                                rx.vstack(
                                    rx.text("Iekrena admin", font_weight="800", font_size="14px", color="#001D3D"),
                                    rx.text("Administradora", font_size="12px", color="#6B7280"),
                                    spacing="0", align="start",
                                ),
                                spacing="2", align="center",
                            ),
                        ),
                        width="100%", align="center",
                    ),

                    # Stats
                    rx.grid(
                        stat_card("calendar-check", "Reservas totales",  AdminState.total_reservas, "+12% este mes", "#0077B6"),
                        stat_card("users",           "Visitantes",        "55.6 mil", "+18% esta semana", "#7C3AED"),
                        stat_card("tag",             "Ofertas activas",   AdminState.ofertas_activas.to_string(), "Actualizadas", "#059669"),
                        stat_card("dollar-sign",     "Ventas USD",        AdminState.total_ventas, "+15% este mes", "#EA580C"),
                        columns="4",
                        spacing="4",
                        width="100%",
                    ),

                    # Panel ofertas
                    rx.box(
                        rx.vstack(
                            # Header del panel
                            rx.hstack(
                                rx.vstack(
                                    rx.text("GESTIÓN DE OFERTAS", color="#0077B6", font_weight="900",
                                            font_size="12px", letter_spacing="0.10em"),
                                    rx.heading("Ofertas turísticas", color="#001D3D", size="6", font_weight="900"),
                                    spacing="0", align="start",
                                ),
                                rx.spacer(),
                                rx.hstack(
                                    rx.box(
                                        rx.hstack(
                                            rx.text(AdminState.total_ofertas, font_weight="900", color="#0077B6", font_size="15px"),
                                            rx.text("total", color="#6B7280", font_size="13px"),
                                            spacing="1", align="center",
                                        ),
                                        background="#EFF8FF",
                                        padding="8px 16px",
                                        border_radius="999px",
                                    ),
                                    rx.button(
                                        rx.hstack(
                                            rx.icon("plus", size=16),
                                            rx.text("Nueva oferta", font_weight="800", font_size="14px"),
                                            spacing="2", align="center",
                                        ),
                                 
                                        on_click=AdminState.abrir_nueva,
                                        background="linear-gradient(135deg, #FFD166, #FFB703)",
                                        color="#001D3D",
                                        border_radius="12px",
                                        height="44px",
                                        padding="0 20px",
                                        border="none",
                                        cursor="pointer",
                                        box_shadow="0 4px 14px rgba(255,183,3,0.35)",
                                        _hover={"transform": "translateY(-1px)"},
                                        transition="all 0.2s",
                                    ),
                                    rx.button(
    "Actualizar reservas",
    on_click=AdminState.cargar_reservas,
    background="#0077B6",
    color="white",
    border_radius="12px",
    height="44px",
    padding="0 20px",
    border="none",
    cursor="pointer",
),
                                    spacing="3", align="center",
                                ),
                                width="100%", align="center",
                            ),

                            rx.box(height="1px", background="#E5E7EB", width="100%"),

                            # Lista de ofertas
                            rx.vstack(
                                rx.foreach(AdminState.ofertas, oferta_row),
                                spacing="3",
                                width="100%",
                            ),

                            rx.box(
    rx.vstack(
        rx.heading("Reservas recientes", color="#001D3D", size="6"),

        rx.foreach(
            AdminState.reservas,
            lambda reserva: rx.box(
                rx.vstack(
                    rx.text(reserva.get("nombre_completo", ""), font_weight="800", color="#001D3D"),
                    rx.text(reserva.get("email", ""), color="#64748B"),
                   rx.hstack(
    rx.text("Destino:", color="#0077B6", font_weight="700"),
    rx.text(reserva.get("destino", ""), color="#0077B6", font_weight="700"),
    spacing="1",
),
rx.hstack(
    rx.text("Total:", color="#FFB703", font_weight="900"),
    rx.text(reserva.get("total", ""), color="#FFB703", font_weight="900"),
    spacing="1",
),
                    spacing="1",
                    align="start",
                ),
                background="#F8FAFC",
                padding="16px",
                border_radius="14px",
                width="100%",
            ),
        ),

        spacing="3",
        align="start",
        width="100%",
    ),
    width="100%",
),

                            
                            spacing="5",
                            align="start",
                            width="100%",
                        ),
                        background="white",
                        padding="28px",
                        border_radius="24px",
                        box_shadow="0 4px 20px rgba(0,0,0,0.07)",
                        width="100%",
                    ),

                    spacing="6",
                    width="100%",
                    align="start",
                ),

                margin_left="240px",
                width="calc(100% - 240px)",
                min_height="100vh",
                background="#F1F5F9",
                padding="32px 36px",
            ),

            width="100%",
            spacing="0",
        ),
    )