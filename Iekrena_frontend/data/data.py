
PRECIOS: dict[str, int] = {
    "Punta Cana":     299,
    "Samaná":         279,
    "Aruba":          349,
    "Jamaica":        309,
    "Cartagena":      269,
    "San Juan":       289,
    "Cancún":         329,
    "Bahamas":        499,
    "Turks & Caicos": 599,
    "Bora Bora":      899,
    "Maldivas":       999,
    "Puerto Rico":    289,
}
 
# Destinos en oferta: precio_oferta, precio_original, porcentaje
OFERTAS: dict[str, dict] = {
    "Punta Cana": {"antes": 499, "ahora": 299, "descuento": "-40%"},
    "Aruba":      {"antes": 699, "ahora": 449, "descuento": "-36%"},
    "Bahamas":    {"antes": 899, "ahora": 599, "descuento": "-33%"},
    "Cancún":     {"antes": 599, "ahora": 379, "descuento": "-37%"},
    "Samaná":     {"antes": 549, "ahora": 385, "descuento": "-30%"},
    "Jamaica":    {"antes": 699, "ahora": 499, "descuento": "-28%"},
}
 
PRECIO_EXPERIENCIA: int = 50
 