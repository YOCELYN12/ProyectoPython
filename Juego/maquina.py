from jugadores import Adivinador, Creador
from tablero import Tablero


class Jugar:
    def __init__(self):
        self.tablero = Tablero()
        self.creador_codigo = None
        self.adivinador_codigo = None
    
    #Le permite al usuario elegir el modo en el que desea jugar
    def elegir_rol(self):
        modo_juego = input("Tienes 2 opciones de juego, puedes ser el creador del codigo o el adivinador (c/a): ").lower()
        if modo_juego == "c":
            #Se establece al jugador1 como el creador del codigo, y el otro jugador debera debera de adivinar el codigo
            self.creador_codigo = Creador(True)
            self.adivinador_codigo = Adivinador(False)
        else: 
            #Condicion en caso de que la anterior no se cumpla
            self.creador_codigo = Creador(False)
            self.adivinador_codigo = Adivinador(True)
        self.tablero.definir_color(self.creador_codigo.crea_codigo())
        
    #Metodo con 12 intentos para poder adivinar el codigo  
    def jugadas_turnos(self):
        for turnos in range(12):
            #Primer intento del jugador
            intento = self.adivinador_codigo.adivinador()
            
            #Se compara el primer intento con el codigo secreto, y devuelve la retroalimentacion
            retroalimentacion = self.tablero.comprobar_color(intento)
            
            #Actualiza el tablero incluyendo la retroalimentacion.
            self.tablero.actualizar_tablero(intento,retroalimentacion)
            
            #Retroalimentacio para el usuario, que muestra el estado del trablero
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
            