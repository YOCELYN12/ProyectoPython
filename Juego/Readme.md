*Archivo jugadores*
Se crea la clase Jugador, la misma sera la principal, tendra la lista de colores para el juego, con el constructor que se va a encargar de inicializar el juego con el jugador1.

Despues esta la clase Creador, la cual hereda de Jugador, la misma tendra el metodo crea_codigo, que se encargara de crear el codigo o el jugador o la maquina, segun lo que el jugador indique.

Por ultimo esta la clasre Adivinador que hereda de jugador, la misma tendra el metodo adivinador en este la compututadore genera un codigo secreto de colores que el jugador tendra que adivinar.


*Archivo tablero*
Se crea la clase Tablero, la misma tendra la logica de la estructuracion del juego en si, la misma tiene una lista con los colores importados, ademas del constructo que va a tener la inicializacion del codigo vacio, ademas con los metodos que se van a encargar de  generar el codigo de colores segun el modo en el que el usuario desee jugar.


*Archivo maquina*
Se crea la clase con el nombre jugar, la misma contendra toda la logica del juego en si, ademas de los archivos previamente creados (tablero y jugadores), la misma esta compusta por metodos como (elegir_rol, jugadas_turnos e iniciar_juego)