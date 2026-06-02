import reflex as rx
from Iekrena_frontend.pages.home import home
from Iekrena_frontend.pages.destinos import destinos
from Iekrena_frontend.pages.detalles import detalles
from Iekrena_frontend.pages.reservas import reservas
from Iekrena_frontend.pages.contacto import contacto


app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="cyan",
        radius="large",
    )
)

app.add_page(home, route="/", title="IEKRENA TRIPS")
app.add_page(destinos, route="/destinos", title="Destinos")
app.add_page(detalles, route="/detalles", title="Detalles del viaje")
app.add_page(reservas, route="/reservas", title="Reservas")
app.add_page(contacto, route="/contacto", title="Contacto")