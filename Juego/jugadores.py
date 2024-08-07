import random 

class Jugador:

     lista = [ "r", "g", "y", "b"]
     def __init__(self, jugador1 = True):
        self.jugador1 = jugador1
      
      
class Creador(Jugador):
      def crea_codigo(self):
            if self.jugador1:
                  color_codigo = input("INGRESE EL CODIGO DE COLORES:").strip().split()
            else:
                  color_codigo = random.choices(self.lista, k=4)
            return color_codigo
            
class Adivinador(Jugador):
      def adivinador(self):    
            if self.jugador1:
                  color_codigo = input("Ingrese el codigo de colores a adivinar:").strip().split()
            else: 
                  color_codigo = random.choices(self.lista,k=4)
            return color_codigo
