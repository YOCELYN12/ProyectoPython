from colored import fg,attr

class Tablero:
    color = {
        "rojo": fg(1), "blanco": fg(4), "verde": fg(2), "amarillo": fg(3)       
    }
    
    def __init__(self):
        self.color_secreto = []
        self.turnos = []
    
    def definir_color(self,color):
        self.color_adivinar = color
    
    def comprobar_color(self,intento):
        retroalimentacion = []
        
        copia_color_adivinar = self.color_adivinar.copy()
        for elemento in range(4):
            if intento[elemento] == copia_color_adivinar[elemento]:
                retroalimentacion.append("color_verde")
                copia_color_adivinar[elemento] = None
            elif intento[elemento] in copia_color_adivinar:
                retroalimentacion.append("color_amarillo")
                copia_color_adivinar.remove(intento[elemento])
            else: 
                retroalimentacion.append("color_blanco")
        return retroalimentacion

    def mostrar_tabla(self):
        for intento,retroalimentacion in self.turnos:
            intento_jugado = " ".join([self.lista[color_jugado] + "o" + attr("reset") for color_jugado in intento])
            
            retroalimentacion_jugada = " ".join([
                fg(2) + "o" +attr("reset") if retro_adivina == "color_verde"
            ])
            
           