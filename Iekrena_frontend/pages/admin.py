import reflex as rx


def menu_item(icono: str, texto: str, activo: bool = False):
    return rx.box(
        rx.hstack(
            rx.icon(icono, size=20),
            rx.text(
                texto,
                font_weight="700",
                font_size="15px",
            ),
            spacing="3",
            align="center",
        ),
        width="100%",
        padding="14px 18px",
        border_radius="14px",
        background="#0077B6" if activo else "transparent",
        color="white" if activo else "rgba(255,255,255,.75)",
        _hover={"background": "rgba(255,255,255,.08)"},
    )


def stat_card(titulo, valor, detalle):
    return rx.box(
        rx.vstack(
            rx.text(
                titulo,
                color="#64748B",
                font_weight="700",
            ),
            rx.heading(
                valor,
                color="#001D3D",
                size="8",
                font_weight="900",
            ),
            rx.text(
                detalle,
                color="#16A34A",
                font_weight="700",
                font_size="13px",
            ),
            spacing="1",
            align="start",
        ),
        background="white",
        padding="24px",
        border_radius="22px",
        box_shadow="0 10px 30px rgba(0,0,0,.08)",
    )


def oferta_row(destino, precio, oferta):
    return rx.hstack(
        rx.text(destino, width="180px", font_weight="800"),
        rx.text(precio, width="120px"),
        rx.text(
            oferta,
            width="120px",
            color="#0077B6",
            font_weight="900",
        ),
        rx.badge(
            "Activa",
            color_scheme="green",
        ),
        rx.spacer(),
        rx.button(
            "Editar",
            background="#0077B6",
            color="white",
        ),
        rx.button(
            "Eliminar",
            background="#D62828",
            color="white",
        ),
        width="100%",
        padding="12px 0",
        border_bottom="1px solid #E2E8F0",
    )


def admin():
    return rx.hstack(

        # SIDEBAR
        rx.box(
            rx.vstack(
                rx.image(
                    src="/logo.png",
                    width="170px",
                ),

                menu_item("layout-dashboard", "Dashboard", True),
                menu_item("tag", "Ofertas"),
                menu_item("calendar", "Reservas"),
                menu_item("users", "Usuarios"),
                menu_item("chart-column", "Visitantes"),
                menu_item("settings", "Configuración"),

                rx.spacer(),

                menu_item("log-out", "Cerrar sesión"),

                width="100%",
                height="100%",
                spacing="3",
                align="start",
            ),

            width="260px",
            height="100vh",

            background="#001D3D",

            padding="24px",

            position="fixed",
            left="0",
            top="0",
        ),

        # CONTENIDO
        rx.box(
            rx.vstack(

                # BANNER
                rx.box(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "PANEL ADMINISTRATIVO",
                                color="#FFB703",
                                font_weight="900",
                            ),

                            rx.heading(
                                "Bienvenida, Lorena 👋",
                                color="white",
                                size="9",
                                font_weight="900",
                            ),

                            rx.text(
                                "Gestiona ofertas, reservas y usuarios desde un solo lugar.",
                                color="rgba(255,255,255,.90)",
                            ),

                            spacing="2",
                            align="start",
                        ),

                        background="""
                        linear-gradient(
                            rgba(0,29,61,.45),
                            rgba(0,29,61,.75)
                        ),
                        url('/admin_banner.jpg')
                        """,

                        background_size="cover",
                        background_position="center",

                        height="280px",

                        border_radius="28px",

                        display="flex",
                        align_items="end",

                        padding="32px",
                    )
                ),

                # STATS
                rx.grid(
                    stat_card(
                        "Reservas Totales",
                        "1,248",
                        "+12% este mes",
                    ),
                    stat_card(
                        "Visitantes",
                        "5,432",
                        "+18% esta semana",
                    ),
                    stat_card(
                        "Ofertas Activas",
                        "8",
                        "Actualizadas",
                    ),
                    stat_card(
                        "Ventas USD",
                        "$125,680",
                        "+15% este mes",
                    ),

                    columns="4",
                    spacing="5",
                    width="100%",
                ),

              # OFERTAS
rx.box(
    rx.box(
        rx.vstack(
            rx.text(
                "GESTIÓN DE OFERTAS",
                color="#FFB703",
                font_weight="900",
            ),

            rx.heading(
                "Administra promociones",
                color="white",
                size="7",
            ),

            spacing="1",
            align="start",
        ),

        background="""
        linear-gradient(
            rgba(0,29,61,.45),
            rgba(0,29,61,.70)
        ),
        url('/offers_banner.jpg')
        """,

        background_size="cover",
        background_position="center",

        height="220px",

        border_radius="24px",

        display="flex",
        align_items="end",

        padding="24px",
    ),

    margin_top="10px",
),

                rx.box(
                    rx.hstack(
                        rx.heading(
                            "Ofertas activas",
                            color="#001D3D",
                            size="6",
                        ),

                        rx.spacer(),

                        rx.button(
                            "+ Nueva oferta",
                            background="#FFB703",
                            color="#001D3D",
                            font_weight="900",
                        ),

                        width="100%",
                    ),

                    rx.vstack(
                        oferta_row(
                            "Punta Cana",
                            "$499",
                            "$299",
                        ),
                        oferta_row(
                            "Aruba",
                            "$699",
                            "$449",
                        ),
                        oferta_row(
                            "Bahamas",
                            "$899",
                            "$599",
                        ),
                        oferta_row(
                            "Cancún",
                            "$599",
                            "$379",
                        ),
                        spacing="0",
                        width="100%",
                    ),

                    background="white",

                    padding="24px",

                    border_radius="24px",

                    box_shadow="0 10px 30px rgba(0,0,0,.08)",

                    width="100%",
                ),

                spacing="6",
                width="100%",
            ),

            margin_left="260px",

            width="calc(100% - 260px)",

            min_height="100vh",

            background="#F8FAFC",

            padding="32px",
        ),

        width="100%",
        spacing="0",
    )