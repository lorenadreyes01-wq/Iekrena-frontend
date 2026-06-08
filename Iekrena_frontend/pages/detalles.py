import reflex as rx
from Iekrena_frontend.components.navbar import navbar
from Iekrena_frontend.components.footer import footer

class DetallesState(rx.State):
    destino: str = ""

    def cargar_destino(self):
        self.destino = self.router.page.params.get("destino", "")


DESTINOS = [
    {
        "nombre": "Punta Cana",
        "pais": "República Dominicana",
        "imagen": "/puntacana.jpg",
        "precio": "$299",
        "duracion": "3 días / 2 noches",
        "personas": "20 personas",
        "descripcion": "Disfruta playas paradisíacas, aguas cristalinas y resorts frente al mar.",
        "servicios": ["Hospedaje", "Desayuno incluido", "Transporte", "Tour de playa"],
        "itinerario": ["Llegada al hotel", "Día de playa y actividades acuáticas", "Desayuno y regreso"],
        "experiencias": [
            {"titulo": "Playa Bávaro", "imagen": "/bavaro_experience.jpg"},
            {"titulo": "Paseo en catamarán", "imagen": "/catamaran_experience.jpg"},
            {"titulo": "Snorkeling", "imagen": "/snorkeling_experience.jpg"},
        ],
    },
    {
        "nombre": "Samaná",
        "pais": "República Dominicana",
        "imagen": "/samana.jpg",
        "precio": "$279",
        "duracion": "2 días / 1 noche",
        "personas": "18 personas",
        "descripcion": "Un destino natural con playas, montañas, cascadas y paisajes únicos.",
        "servicios": ["Transporte", "Guía turístico", "Entrada a excursiones", "Almuerzo"],
        "itinerario": ["Salida hacia Samaná", "Visita a playa o cascada", "Regreso al punto de partida"],
        "experiencias": [
            {"titulo": "Salto El Limón", "imagen": "/el_limon_experience.jpg"},
            {"titulo": "Avistamiento de ballenas", "imagen": "/whales_experience.jpg"},
            {"titulo": "Cayo Levantado", "imagen": "/cayo_levantado_experience.jpg"},
        ],
    },
    {
        "nombre": "Aruba",
        "pais": "Aruba",
        "imagen": "/aruba.jpg",
        "precio": "$349",
        "duracion": "4 días / 3 noches",
        "personas": "15 personas",
        "descripcion": "Arena blanca, playas tranquilas y una experiencia caribeña inolvidable.",
        "servicios": ["Hotel", "Desayuno", "Tour por la isla", "Asistencia de viaje"],
        "itinerario": ["Llegada y check-in", "Tour por playas", "Día libre", "Regreso"],
        "experiencias": [
            {"titulo": "Flamingo Beach", "imagen": "/flamingo_experience.jpg"},
            {"titulo": "Eagle Beach", "imagen": "/eagle_beach_experience.jpg"},
            {"titulo": "Jeep Tour", "imagen": "/jeep_experience.jpg"},
        ],
    },
    {
        "nombre": "Jamaica",
        "pais": "Jamaica",
        "imagen": "/jamaica.jpg",
        "precio": "$309",
        "duracion": "4 días / 3 noches",
        "personas": "16 personas",
        "descripcion": "Vive cultura, naturaleza, música y playas espectaculares.",
        "servicios": ["Hotel", "Tour cultural", "Transporte", "Guía"],
        "itinerario": ["Llegada", "Tour cultural", "Excursión natural", "Regreso"],
        "experiencias": [
            {"titulo": "Dunn's River Falls", "imagen": "/dunns_river_experience.jpg"},
            {"titulo": "Ruta del reggae", "imagen": "/reggae_experience.jpg"},
            {"titulo": "Blue Mountains", "imagen": "/blue_mountains_experience.jpg"},
        ],
    },
    {
        "nombre": "Cartagena",
        "pais": "Colombia",
        "imagen": "/cartagena.jpg",
        "precio": "$269",
        "duracion": "3 días / 2 noches",
        "personas": "20 personas",
        "descripcion": "Una ciudad histórica, colorida y llena de cultura caribeña.",
        "servicios": ["Hotel", "City tour", "Transporte", "Guía local"],
        "itinerario": ["Llegada", "Recorrido por ciudad amurallada", "Día libre", "Regreso"],
        "experiencias": [
            {"titulo": "Ciudad amurallada", "imagen": "/old_city_experience.jpg"},
            {"titulo": "Islas del Rosario", "imagen": "/rosario_islands_experience.jpg"},
            {"titulo": "Atardecer en Cartagena", "imagen": "/sunset_cartagena.jpg"},
        ],
    },
    {
        "nombre": "San Juan",
        "pais": "Puerto Rico",
        "imagen": "/sanjuan.jpg",
        "precio": "$289",
        "duracion": "3 días / 2 noches",
        "personas": "18 personas",
        "descripcion": "Historia, playas y vida urbana en un mismo destino.",
        "servicios": ["Hotel", "Tour histórico", "Transporte", "Asistencia"],
        "itinerario": ["Llegada", "Tour por Viejo San Juan", "Playa", "Regreso"],
        "experiencias": [
            {"titulo": "Viejo San Juan", "imagen": "/old_sanjuan_experience.jpg"},
            {"titulo": "Castillo El Morro", "imagen": "/morro_experience.jpg"},
            {"titulo": "Vida nocturna", "imagen": "/nightlife_pr.jpg"},
        ],
    },
    {
        "nombre": "Cancún",
        "pais": "México",
        "imagen": "/Cancun.jpg",
        "precio": "$329",
        "duracion": "4 días / 3 noches",
        "personas": "22 personas",
        "descripcion": "Playas turquesas, vida nocturna y experiencias inolvidables.",
        "servicios": ["Resort", "Desayuno", "Tour a playa", "Transporte"],
        "itinerario": ["Llegada", "Playa y resort", "Excursión opcional", "Regreso"],
        "experiencias": [
            {"titulo": "Xcaret", "imagen": "/xcaret_experience.jpg"},
            {"titulo": "Cenote", "imagen": "/cenote_experience.jpg"},
            {"titulo": "Chichén Itzá", "imagen": "/chichenitza_experience.jpg"},
        ],
    },
    {
        "nombre": "Bahamas",
        "pais": "Bahamas",
        "imagen": "/bahamas.jpg",
        "precio": "$499",
        "duracion": "5 días / 4 noches",
        "personas": "14 personas",
        "descripcion": "Un paraíso tropical con aguas cristalinas y ambiente exclusivo.",
        "servicios": ["Hotel", "Tour marítimo", "Desayuno", "Asistencia"],
        "itinerario": ["Llegada", "Tour en barco", "Día libre", "Actividades acuáticas", "Regreso"],
        "experiencias": [
            {"titulo": "Pig Beach", "imagen": "/pig_beach_experience.jpg"},
            {"titulo": "Paseo en bote", "imagen": "/boat_experience.jpg"},
            {"titulo": "Buceo", "imagen": "/diving_bahamas.jpg"},
        ],
    },
    {
        "nombre": "Turks & Caicos",
        "pais": "Caribe",
        "imagen": "/turksandcaicos.jpg",
        "precio": "$599",
        "duracion": "5 días / 4 noches",
        "personas": "12 personas",
        "descripcion": "Destino exclusivo con playas de lujo y aguas impresionantes.",
        "servicios": ["Resort premium", "Desayuno", "Tour privado", "Transporte"],
        "itinerario": ["Llegada VIP", "Día de playa", "Tour privado", "Día libre", "Regreso"],
        "experiencias": [
            {"titulo": "Grace Bay", "imagen": "/grace_bay_experience.jpg"},
            {"titulo": "Yate privado", "imagen": "/luxury_yacht.jpg"},
            {"titulo": "Diving", "imagen": "/diving_turks.jpg"},
        ],
    },
    {
        "nombre": "Bora Bora",
        "pais": "Polinesia Francesa",
        "imagen": "/borabora.jpg",
        "precio": "$899",
        "duracion": "6 días / 5 noches",
        "personas": "10 personas",
        "descripcion": "Una experiencia premium en uno de los destinos más soñados del mundo.",
        "servicios": ["Resort de lujo", "Desayuno", "Tour en laguna", "Asistencia VIP"],
        "itinerario": ["Llegada", "Tour por laguna", "Día libre", "Cena especial", "Actividades acuáticas", "Regreso"],
        "experiencias": [
            {"titulo": "Villa sobre el agua", "imagen": "/villa_water.jpg"},
            {"titulo": "Tour en laguna", "imagen": "/lagoon_tour.jpg"},
            {"titulo": "Cena al atardecer", "imagen": "/sunset_dinner.jpg"},
        ],
    },
    {
        "nombre": "Maldivas",
        "pais": "Maldivas",
        "imagen": "/maldivas.jpg",
        "precio": "$999",
        "duracion": "6 días / 5 noches",
        "personas": "10 personas",
        "descripcion": "Lujo absoluto en villas sobre el agua y paisajes inolvidables.",
        "servicios": ["Villa sobre el agua", "Desayuno", "Cena especial", "Traslado"],
        "itinerario": ["Llegada", "Día libre en villa", "Cena romántica", "Excursión marina", "Spa", "Regreso"],
        "experiencias": [
            {"titulo": "Water Villa", "imagen": "/water_villa.jpg"},
            {"titulo": "Spa Maldives", "imagen": "/spa_maldives.jpg"},
            {"titulo": "Cena privada", "imagen": "/private_dinner.jpg"},
        ],
    },
    {
        "nombre": "Puerto Rico",
        "pais": "Puerto Rico",
        "imagen": "/puertorico.jpg",
        "precio": "$289",
        "duracion": "3 días / 2 noches",
        "personas": "18 personas",
        "descripcion": "Playas, historia, bosques tropicales y cultura caribeña vibrante.",
        "servicios": ["Hotel", "Tour cultural", "Transporte", "Asistencia"],
        "itinerario": ["Llegada", "Viejo San Juan", "El Yunque", "Regreso"],
        "experiencias": [
            {"titulo": "Viejo San Juan", "imagen": "/old_sanjuan_pr.jpg"},
            {"titulo": "Bahía bioluminiscente", "imagen": "/bioluminescent_bay.jpg"},
            {"titulo": "El Yunque", "imagen": "/el_yunque.jpg"},
        ],
    },
]


def experiencia_item(exp):
    return rx.box(
        rx.image(
            src=exp["imagen"],
            width="100%",
            height="105px",
            object_fit="cover",
            border_radius="14px",
        ),
        rx.text(
            exp["titulo"],
            color="#001D3D",
            font_weight="800",
            font_size="13px",
            margin_top="8px",
        ),
    )


def info_item(titulo, valor):
    return rx.vstack(
        rx.text(titulo, color="#0077B6", font_size="13px", font_weight="800"),
        rx.text(valor, color="#001D3D", font_size="16px", font_weight="600"),
        spacing="1",
        align="start",
    )


def detalle_card(destino):
    return rx.box(
        rx.grid(
            rx.image(
                src=destino["imagen"],
                width="100%",
                height="100%",
                min_height="500px",
                object_fit="cover",
                border_radius="20px",
            ),

            rx.vstack(
                rx.text(destino["pais"], color="#0077B6", font_weight="800"),
                rx.heading(destino["nombre"], size="7", color="#001D3D", font_weight="900"),
                rx.text(destino["descripcion"], color="#374151", line_height="1.6"),

                rx.hstack(
                    info_item("Precio", f'{destino["precio"]} USD'),
                    info_item("Duración", destino["duracion"]),
                    info_item("Máximo", destino["personas"]),
                    spacing="7",
                    wrap="wrap",
                ),

                rx.heading("Servicios incluidos", size="4", color="#001D3D"),
                rx.vstack(
                    *[rx.text(f"• {s}", color="#001D3D") for s in destino["servicios"]],
                    spacing="1",
                    align="start",
                ),

                spacing="4",
                align="start",
            ),

            rx.vstack(
                rx.heading("Itinerario", size="4", color="#001D3D"),
                rx.vstack(
                    *[
                        rx.text(
                            f"Día {i + 1}: {item}",
                            color="#001D3D",
                            font_weight="600",
                            font_size="14px",
                        )
                        for i, item in enumerate(destino["itinerario"])
                    ],
                    spacing="1",
                    align="start",
                ),

                rx.heading("Experiencias destacadas", size="4", color="#001D3D"),
                rx.grid(
                    *[experiencia_item(exp) for exp in destino["experiencias"]],
                    columns="3",
                    spacing="3",
                    width="100%",
                ),

                rx.link(
                    rx.button(
                        "Reservar ahora",
                        background="#FFB703",
                        color="#001D3D",
                        border_radius="10px",
                        height="48px",
                        padding="0 28px",
                        font_weight="900",
                        margin_top="10px",
                        cursor="pointer",
                        _hover={"background": "#FFC107"},
                        transition="background 0.15s",
                    ),
                    href="/reservas",
                ),

                spacing="4",
                align="start",
            ),

            columns="3",
            spacing="6",
            width="100%",
        ),

        background="white",
        padding="18px",
        border_radius="24px",
        box_shadow="0 10px 30px rgba(0,0,0,0.10)",
        border="1px solid #E5E7EB",
    )


def detalles():
    return rx.box(
        navbar("destinos"),

        rx.box(
            rx.vstack(
                rx.heading(
                    "DETALLES DEL VIAJE",
                    color="white",
                    font_size="62px",
                    font_weight="900",
                    text_align="center",
                ),
                rx.text(
                    "Explora la información completa de cada destino.",
                    color="white",
                    font_size="21px",
                    text_align="center",
                ),
                spacing="3",
                align="center",
            ),
            height="55vh",
            background=(
                "linear-gradient(rgba(0,20,35,.55), rgba(0,20,35,.60)),"
                "url('/hero.png')"
            ),
            background_size="cover",
            background_position="center",
            display="flex",
            align_items="center",
            justify_content="center",
            padding_top="120px",
        ),

       rx.vstack(

    rx.cond(
        (DetallesState.destino == "") | (DetallesState.destino.lower() == "punta cana"),
        detalle_card(DESTINOS[0]),
        rx.box(),
    ),

    rx.cond(
        (DetallesState.destino == "") | ((DetallesState.destino).lower() == "samaná") | ((DetallesState.destino).lower() == "samana"),
        detalle_card(DESTINOS[1]),
        rx.box(),
    ),

    rx.cond(
        (DetallesState.destino == "") | ((DetallesState.destino).lower() == "aruba"),
        detalle_card(DESTINOS[2]),
        rx.box(),
    ),

    rx.cond(
        (DetallesState.destino == "") | ((DetallesState.destino).lower() == "jamaica"),
        detalle_card(DESTINOS[3]),
        rx.box(),
    ),

    rx.cond(
        (DetallesState.destino == "") | ((DetallesState.destino).lower() == "cartagena"),
        detalle_card(DESTINOS[4]),
        rx.box(),
    ),

    rx.cond(
        (DetallesState.destino == "") | ((DetallesState.destino).lower() == "san juan"),
        detalle_card(DESTINOS[5]),
        rx.box(),
    ),

    rx.cond(
        (DetallesState.destino == "") | ((DetallesState.destino).lower() == "cancún") | ((DetallesState.destino).lower() == "cancun"),
        detalle_card(DESTINOS[6]),
        rx.box(),
    ),

    rx.cond(
    (DetallesState.destino == "") | ((DetallesState.destino).lower() == "bahamas"),
    detalle_card(DESTINOS[7]),
    rx.box(),
    ),

   rx.cond(
    (
        (DetallesState.destino == "") |
        ((DetallesState.destino).lower() == "turks & caicos") |
        ((DetallesState.destino).lower() == "turks caicos") |
        ((DetallesState.destino).lower() == "turks and caicos")
    ),
    detalle_card(DESTINOS[8]),
    rx.box(),
),
    rx.cond(
        (DetallesState.destino == "") | ((DetallesState.destino).lower() == "bora bora"),
        detalle_card(DESTINOS[9]),
        rx.box(),
    ),

    rx.cond(
        (DetallesState.destino == "") | ((DetallesState.destino).lower() == "maldivas"),
        detalle_card(DESTINOS[10]),
        rx.box(),
    ),

    rx.cond(
        (DetallesState.destino == "") | ((DetallesState.destino).lower() == "puerto rico"),
        detalle_card(DESTINOS[11]),
        rx.box(),
),
    ),

      rx.vstack(
        # todos los rx.cond aquí dentro
        spacing="5",
        padding="40px",
        background="#F8FAFC",
    ),

    footer(),
)