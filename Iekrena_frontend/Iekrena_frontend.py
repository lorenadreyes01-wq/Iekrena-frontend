import reflex as rx
from Iekrena_frontend.pages.home import home
from Iekrena_frontend.pages.ofertas import ofertas
from Iekrena_frontend.pages.destinos import destinos, DestinosState
from Iekrena_frontend.pages.detalles import detalles, DetallesState
from Iekrena_frontend.pages.reservas import reservas
from Iekrena_frontend.pages.contacto import contacto
from Iekrena_frontend.pages.admin import admin
from Iekrena_frontend.pages.login import login


app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="cyan",
        radius="large",
    )
)

app.add_page(home, route="/", title="IEKRENA TRIPS")
app.add_page(destinos, route="/destinos", title="Destinos", on_load=DestinosState.cargar_busqueda)
app.add_page(ofertas, route="/ofertas", title="Ofertas")
app.add_page(detalles, route="/detalles", title="Detalles del viaje", on_load=DetallesState.cargar_destino)
app.add_page(reservas, route="/reservas", title="Reservas")
app.add_page(contacto, route="/contacto", title="Contacto")
app.add_page(admin, route="/admin", title="Panel de Administrador")
app.add_page(login, route="/login", title="Iniciar sesion")