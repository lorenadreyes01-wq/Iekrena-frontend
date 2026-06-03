import reflex as rx


def nav_item(icon: str, text: str, href: str, active: bool = False):
    return rx.link(
        rx.vstack(
            rx.box(
                rx.image(
                    src=icon,
                    width="64px",
                    height="64px",
                    object_fit="contain",
                ),
                width="88px",
                height="88px",
                display="flex",
                align_items="center",
                justify_content="center",
                border_radius="18px",
                background="rgba(0, 180, 216, 0.22)" if active else "transparent",
                box_shadow="0 0 20px rgba(0, 212, 255, 0.50)" if active else "none",
            ),

            rx.text(
                text,
                color="#FFB703" if active else "rgba(255,255,255,0.90)",
                font_size="14px",
                font_weight="800",
            ),

            rx.box(
                width="48px" if active else "0px",
                height="4px",
                background="#FFB703",
                border_radius="999px",
            ),

            spacing="1",
            align="center",
        ),
        href=href,
        text_decoration="none",
    )


def circle_icon(icon: str, href: str = "#"):
    return rx.link(
        rx.box(
            rx.image(
                src=icon,
                width="54px",
                height="54px",
                object_fit="contain",
            ),

            width="84px",
            height="84px",

            display="flex",
            align_items="center",
            justify_content="center",

            border="1.5px solid rgba(0, 212, 255, 0.50)",
            border_radius="999px",

            background="rgba(0, 95, 115, 0.25)",

            box_shadow="0 0 16px rgba(0, 212, 255, 0.25)",

            _hover={
                "background": "rgba(0, 95, 115, 0.50)",
                "box_shadow": "0 0 24px rgba(0, 212, 255, 0.45)",
            },

            transition="all 0.2s ease",
        ),
        href=href,
        text_decoration="none",
    )


def divider():
    return rx.box(
        width="1px",
        height="78px",
        background="rgba(255,255,255,0.15)",
        flex_shrink="0",
    )


def navbar(active_page: str = "inicio"):
    return rx.box(
        rx.hstack(

            rx.image(
                src="/logo.png",
                width="190px",
                height="auto",
                object_fit="contain",
            ),

            divider(),

            rx.hstack(
                nav_item("/home.png", "Inicio", "/", active_page == "inicio"),
                nav_item("/pin.png", "Destinos", "/destinos", active_page == "destinos"),
                nav_item("/tag.png", "Ofertas", "/ofertas", active_page == "ofertas"),
                nav_item("/calendar.png", "Reservas", "/reservas", active_page == "reservas"),
                nav_item("/envelope.png", "Contacto", "/contacto", active_page == "contacto"),

                spacing="4",
                align="center",
                gap="10px",
            ),

            divider(),

         
    rx.hstack(
    circle_icon("/search.png", "/"),
    circle_icon("/user.png", "/admin"),

  

    rx.link(
        rx.button(
            rx.text(
                "Iniciar sesión",
                font_size="15px",
                font_weight="800",
            ),

            background="linear-gradient(135deg, #FFD166, #FFB703)",
            color="#001D3D",

            border_radius="999px",

            height="62px",
            padding="0 34px",

            box_shadow="0 6px 20px rgba(255,183,3,0.40)",

            _hover={
                "background": "linear-gradient(135deg, #FFE08A, #FFC300)",
                "box_shadow": "0 8px 28px rgba(255,183,3,0.55)",
            },
        ),
        href="/login",
        text_decoration="none",
    ),

    spacing="3",
    align="center",
),

            width="100%",
            align="center",
            justify="between",
        ),

        position="fixed",
        top="12px",
        left="50%",
        transform="translateX(-50%)",

        width="96%",
        max_width="1400px",

        z_index="999",

        padding="12px 28px",

        background="rgba(0, 29, 61, 0.90)",
        backdrop_filter="blur(20px)",

        border="1px solid rgba(0, 212, 255, 0.30)",
        border_radius="24px",

        box_shadow="0 0 32px rgba(0, 212, 255, 0.18), 0 20px 50px rgba(0,0,0,0.35)",
    )