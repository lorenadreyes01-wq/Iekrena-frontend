import reflex as rx

class AuthState(rx.State):
    autenticado: bool = False

    def iniciar(self):
        self.autenticado = True

    def salir(self):
        self.autenticado = False