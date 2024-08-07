from jugadores import Adivinador, Creador
from tablero import Tablero


class Jugar:
    def __init__(self):
        self.tablero = Tablero()
        self.creador_codigo = None
        self.adivinador_codigo = None
        
    def elegir_rol(self):
        modo_juego = input("Tienes 2 opciones de juego, puedes ser el creador del codigo o el adivinador: ").lower()
        if modo_juego == "c":
            self.creador_codigo = Creador(True)
            self.adivinador_codigo = Adivinador(False)
        else: 
            self.creador_codigo = Creador(False)
            self.adivinador_codigo = Adivinador(True)
        self.tablero.definir_color(self.creador_codigo.crea_codigo())
def jugadas_turnos(self):
        for turnos in range(12):
            intento = self.adivinador_codigo.adivinador()
            retroalimentacion = self.tablero.comprobar_color(intento)
            self.tablero.actualizar_tablero(intento,retroalimentacion)
            self.tablero.mostrar_tabla()
            print(turnos)
            if retroalimentacion == ["color_verde"]*4:
                print("Felicidades haz ganado")
                return
        
        print("Tus intentos se han agotado")

def iniciar_juego(self):
        self.elegir_rol()
        self.jugadas_turnos()


if __name__ == "__main__":
    juego = Jugar()
    juego.iniciar_juego()
            