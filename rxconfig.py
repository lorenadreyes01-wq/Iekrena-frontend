import reflex as rx

config = rx.Config(
    app_name="Iekrena_frontend",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)