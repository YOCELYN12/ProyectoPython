from jugadores import Adivinador, Creador
from tablero import Tablero


class Jugar:
    def __init__(self):
        self.taablero = Tablero()
        self.creador_codigo = None
        self.adiviandor_codigo = None
        
    def elegir_rol(self):
        modo_juego = input("Tienes 2 opciones de juego, puedes ser el creador del codigo o el adivinador: ").lower()
        if modo_juego == "creador del codigo":
            self.creador_codigo = Creador(True)
            self.adiviandor_codigo = Adivinador(False)