# IEKRENA TRIPS - Frontend

## Descripción del Proyecto

IEKRENA TRIPS es una plataforma web de turismo diseñada para facilitar la búsqueda, exploración y reserva de destinos turísticos nacionales e internacionales. La aplicación ofrece una experiencia visual moderna e intuitiva, permitiendo a los usuarios descubrir destinos, consultar ofertas especiales y gestionar reservas de manera sencilla.

---

## Tecnologías Utilizadas

* Python
* Reflex Framework
* HTML/CSS (generado por Reflex)
* Componentes Radix UI
* Git y GitHub

---

## Funcionalidades Implementadas

### Página de Inicio

* Hero principal con buscador de destinos.
* Sección de destinos destacados.
* Sección de experiencias turísticas.
* Diseño responsive y moderno.

### Página de Destinos

* Catálogo de destinos disponibles.
* Tarjetas informativas con imágenes.
* Navegación hacia detalles completos.

### Página de Detalles

* Información detallada de cada destino.
* Servicios incluidos.
* Itinerarios.
* Experiencias destacadas por destino.
* Botón de reserva.

### Página de Ofertas

* Promociones destacadas.
* Descuentos especiales.
* Temporizador para ofertas limitadas.
* Diseño orientado a conversión.

### Página de Reservas

* Formulario de reserva.
* Selección de destino.
* Selección de experiencias.
* Método de pago.
* Cálculo dinámico del precio total.
* Resumen de reserva en tiempo real.

### Página de Contacto

* Información de contacto.
* Formulario de mensajes.
* Redes sociales.
* Horarios de atención.

### Inicio de Sesión

* Acceso mediante correo y contraseña.
* Base preparada para autenticación con roles.

### Panel Administrativo

* Dashboard administrativo.
* Gestión de ofertas.
* Estadísticas generales.
* Base preparada para integración con backend.

---

## Estructura del Proyecto

```text
Iekrena_frontend/
│
├── assets/
│
├── components/
│   ├── navbar.py
│   └── footer.py
│
├── pages/
│   ├── home.py
│   ├── destinos.py
│   ├── detalles.py
│   ├── ofertas.py
│   ├── reservas.py
│   ├── contacto.py
│   ├── login.py
│   └── admin.py
│
└── Iekrena_frontend.py
```

---

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/usuario/iekrena-trips.git
```

### Acceder al proyecto

```bash
cd iekrena-trips
```

### Instalar dependencias

```bash
poetry install
```

### Ejecutar la aplicación

```bash
poetry run reflex run
```

---

## Diseño e Identidad Visual

### Colores Principales

| Color           | Código  |
| --------------- | ------- |
| Azul Marino     | #001D3D |
| Amarillo Dorado | #FFB703 |
| Azul Turquesa   | #0077B6 |
| Fondo Claro     | #F8FAFC |

### Estilo Visual

* Tropical
* Moderno
* Elegante
* Profesional
* Inspirado en agencias de viajes internacionales

---

## Funcionalidades Futuras

* Integración con base de datos MySQL.
* Sistema completo de autenticación.
* Roles de usuario y administrador.
* Gestión dinámica de ofertas.
* Reservas en línea.
* Pasarela de pagos.
* Dashboard con estadísticas reales.
* Panel de administración funcional.
* Integración con APIs de turismo.

---

## Equipo de Desarrollo

Proyecto desarrollado por el equipo de IEKRENA TRIPS como parte de un proyecto académico enfocado en el desarrollo de plataformas web para el sector turístico.

---

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/iekrena-trips.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd Iekrena-frontend
```

### 3. Instalar las dependencias

```bash
poetry install
```

### 4. Ejecutar la aplicación

```bash
poetry run reflex run
```

### 5. Abrir en el navegador

```text
http://localhost:3000
```

---

## Requisitos

* Python 3.11 o superior
* Poetry
* Reflex Framework

### Verificar Python

```bash
python --version
```

### Verificar Poetry

```bash
poetry --version
```

## Autor

**Lorena Duran Reyes**

**Iekna Frank**

Colegio CAFAM
Técnico en Informática
