from colored import fg,attr

class Tablero:
    color = {
        "rojo": fg(1), "blanco": fg(4), "verde": fg(2), "amarillo": fg(3)       
    }
    
    def __init__(self):
        self.color_secreto = []
        self.turnos = []
    
    def definir_color(self,color):
        self.color_secreto = color

    def validar_ganador(self,intento):
        retroalimentacion = []
        copia_color = self.color_secreto.copy()
        for i in range(4):
            if intento[1] == copia_color[1]:
                
    

                    
         