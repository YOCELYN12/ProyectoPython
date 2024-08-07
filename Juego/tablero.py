from colored import fg,attr

class Tablero:
    color = {
        "rojo": fg(1), "blanco": fg(4), "verde": fg(2), "amarillo": fg(3)       
    }
    
    def __init__(self):
        self.color_secreto = []
        self.turnos = []
    
    def definir_color(self,color):
        retroalimentacion = []
        
        
        
        
    
    

    def validar_ganador(self,intento):
        retroalimentacion = []
        copia_color = self.color_adivinar.copy()
        for i in range(4):
            if intento[i] == copia_color[1]:
                def validar_ganador(self,intento):
                    retroalimentacion = []
                    copia_color = self.color_secreto.copy()
        for i in range(4):
            if intento[1]== copia_color[1]:
                retroalimentacion.append("color_verder")
                copia_color[i]= None
            elif intento[i] in copia_color:
                retroalimentacion.append("color_amarillo")
                copia_color.remove(intento[i])
            else: retroalimentacion.append("color_blanco")
            return retroalimentacion
        
        def mostrar(self):
            for intento, retroalimentacion in self.turnos:
                fila_color = " ".join([self.colores[color]+ "🟠"+ attr("reset")for color in  intento])
                
                fila_retroalimentacion = " ".join([
                    fg(2) + "🟠"+ attr("reset") if adivina == "color_verde"
                    else fg(3) + "🟠" + attr("reset") if adivina == "color_amarillo"
                    else"🟠" 
                    
                    for adivina in retroalimentacion
                    ])
                
                print(f"{fila_color} {fila_retroalimentacion}")
                    
            def actualiza(self,intento,retroalimentacion):
                self.turnos.append((intento,retroalimentacion))






                
    

                    
         ""