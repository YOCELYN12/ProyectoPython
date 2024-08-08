from colored import fg,attr

class Tablero:
    #Diccionario de los colores 
    color = {
        "r": fg(1), "b": fg(4), "g": fg(2), "y": fg(3)       
    }
    #Constuctor de la clase que inicializa el codigo en 0 al igual que los turnos
    def __init__(self):
        self.color_secreto = []
        self.turnos = []
    
    #Define el color secreto en el tablero
    def definir_color(self,color):
        self.color_secreto = color
    
    #Metodo que se encarga de comparar los intentos del jugador, con el codigo secreto
    def comprobar_color(self,intento):
        retroalimentacion = []
        
        copia_color_adivinar = self.color_secreto.copy()
        
        for i in range(4):
           
            if intento[i] == copia_color_adivinar[i]:
                # Si el color en la posición correcta, sera del"color_verde"
                retroalimentacion.append("color_verde")
            elif intento[i] in copia_color_adivinar:
                 # Si el color está en el código secreto pero en la posición incorrecta, sera "color_amarillo"
                retroalimentacion.append("color_amarillo")
            else: 
                # Si el color no está en el código secreto, sera del "color_blanco"
                retroalimentacion.append("color_blanco")
        return retroalimentacion

    def mostrar_tabla(self):
        for intento,retroalimentacion in self.turnos:
            intento_jugado = " ".join([self.color[color_jugado] + "o" + attr("reset") for color_jugado in intento])
            
            #Representa la retroalimentacion para el usuario.
            retroalimentacion_jugada = " ".join([
                fg(2) + "o" +attr("reset") if retro_adivina == "color_verde"

                else fg(3) + "o" + attr("reset") if retro_adivina == "color_amarillo"

                else "o"

                for retro_adivina in retroalimentacion
            ])

        print(f"{intento_jugado}|{retroalimentacion_jugada}")

    
    def actualizar_tablero(self,intento,retroalimentacion):
        self.turnos.append((intento,retroalimentacion))



            
           