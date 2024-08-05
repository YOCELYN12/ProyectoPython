from colored import fg,attr

class Tablero:
    color = {
        "rojo": fg(1), "blanco": fg(4), "verde": fg(2), "amarillo": fg(3)       
    }
    
    def __init__(self):
        self.color_secreto = []
        self.turnos = []
    
    

                    
         