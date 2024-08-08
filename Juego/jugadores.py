import random 

#clase padre 
class Jugador:
     #Lista de colores posibles 
     lista = [ "r", "g", "y", "b"]
     def __init__(self, jugador1 = True):
        self.jugador1 = jugador1
      
#Genera un codigo de colores basado en el primer jugador, hereda de la clase padre(Jugador)  
class Creador(Jugador):
      def crea_codigo(self):
            #Condicion de que si es el primer jugador, el codigo es ingresado manualmente 
            if self.jugador1:
                  color_secreto = input("Ingrese el codido de colores:").strip().split()
            else:
                  color_secreto = random.choices(self.lista, k=4)
            return color_secreto

#Clase en caso de que el usuario desee ser adivinador.         
class Adivinador(Jugador):
      def adivinador(self):    
            if self.jugador1:
                  color_secreto = input("Ingrese el codigo de colores a adivinar:").strip().split()
            else: 
                  color_secreto = random.choices(self.lista,k=4)
            return color_secreto
