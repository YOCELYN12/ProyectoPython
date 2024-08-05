import random 
from colored import fg,attr

color = {"red", "blanco", "amarillo", "verde"}
print(f" el color es{color}")
nombre_jugador = input("A continuacion, ingrese su nombre:")
print(f"{nombre_jugador} tienes 12 intentos, la metodologia del juego es la siguiente tendras 2 opcines de juego, eres el creador del codigo, o el adivinador, si deseas ser el creador del codigo deberas proporcinar el codigo secreto,  que en este caso son los 4 colores, que la computadora intentara adivinar. Si deseas ser el adivinador el programa generarara un codigo secreto aleatorio para que intentes adivinar. ")

tipo_de_juego = input("Ingresa el modo en el que quieres jugar, (Creador de codigo) o (Adivinador):")

if tipo_de_juego == "Adivinador":
      print("hola")
elif tipo_de_juego == "Creador de codigo":
      print("funciona")

    
