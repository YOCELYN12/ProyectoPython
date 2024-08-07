import random 

class Jugador:

     lista = [ "red", "green", "yellow", "blue"]
     def __init__(self, es_el_jugador = True):
        self.es_el_jugador = es_el_jugador
      
      
class Creador(Jugador):
      def crea_codigo(self):
            if self.es_el_jugador:
                  color_codigo = input("INGRESE EL CODIGO DE COLORES:").strip.split()
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
