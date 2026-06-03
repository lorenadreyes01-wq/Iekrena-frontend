import reflex as rx


def footer():
    return rx.box(
        rx.vstack(

            # PARTE SUPERIOR
            rx.hstack(

                # LOGO Y DESCRIPCIÓN
                rx.vstack(
                    rx.image(
                        src="/logo_white.png",
                        width="220px",
                    ),

                    rx.text(
                        "Explora el Caribe, reserva experiencias únicas y descubre los mejores destinos con IEKRENA TRIPS.",
                        color="rgba(255,255,255,0.75)",
                        max_width="320px",
                    ),

                    align="start",
                    spacing="4",
                ),

                rx.spacer(),

                # MENÚ
                rx.vstack(
                    rx.heading("Menú", color="white", size="4"),

                    rx.link("Inicio", href="/", color="rgba(255,255,255,0.75)"),
                    rx.link("Destinos", href="/destinos", color="rgba(255,255,255,0.75)"),
                    rx.link("Ofertas", href="/ofertas", color="rgba(255,255,255,0.75)"),
                    rx.link("Reservas", href="/reservas", color="rgba(255,255,255,0.75)"),

                    align="start",
                    spacing="3",
                ),

                # CONTACTO
                rx.vstack(
                    rx.heading("Contacto", color="white", size="4"),

                    rx.hstack(
                        rx.image(src="/mail.png", width="18px"),
                        rx.text("info@iekrenatrips.com", color="rgba(255,255,255,0.75)"),
                    ),

                    rx.hstack(
                        rx.image(src="/phone.png", width="18px"),
                        rx.text("+1 (809) 000-0000", color="rgba(255,255,255,0.75)"),
                    ),

                    rx.hstack(
                        rx.image(src="/location.png", width="18px"),
                        rx.text("Santo Domingo, RD", color="rgba(255,255,255,0.75)"),
                    ),

                    align="start",
                    spacing="3",
                ),

                # REDES
                rx.vstack(
                    rx.heading("Síguenos", color="white", size="4"),

                    rx.hstack(
                        rx.image(src="/facebook.png", width="24px"),
                        rx.image(src="/instagram.png", width="24px"),
                        rx.image(src="/twitter.png", width="24px"),
                        rx.image(src="/youtube.png", width="24px"),
                        spacing="4",
                    ),

                    rx.text(
                        "Descubre experiencias únicas y ofertas exclusivas.",
                        color="rgba(255,255,255,0.75)",
                        max_width="220px",
                    ),

                    align="start",
                    spacing="4",
                ),

                width="100%",
                align="start",
                spacing="9",
                wrap="wrap",
            ),

            # LINEA
            rx.divider(
                border_color="rgba(255,255,255,0.15)"
            ),

            # PARTE INFERIOR
            rx.hstack(
                rx.text(
                    "© 2026 IEKRENA TRIPS. Todos los derechos reservados.",
                    color="rgba(255,255,255,0.60)",
                ),

                rx.spacer(),

                rx.text(
                    "Diseñado para que vivas lo mejor del Caribe.",
                    color="rgba(255,255,255,0.60)",
                ),

                width="100%",
                wrap="wrap",
            ),

            spacing="8",
            width="100%",
            max_width="1200px",
        ),

        background="linear-gradient(135deg,#001D3D,#002B5B)",
        padding="70px 50px 35px 50px",
        margin_top="0",
    )