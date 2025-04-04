# Notas dia 1 (Viernes 28 Marzo) Proyecto - Christian Massa


# Proyecto final de curso de Python / Pygame.

# Videojuego tipo RPG (Algo como los Pokémon antiguos) 

# Con Didac Perales

# Notas dia 2 (Lunes 31 de Marzo) 

# Didac ha terminado de hacer PORFIN el sprite del personaje del jugador. Pero solo el principal, el que se ve de frente.
# He hecho los primeros tiles (texturas/fragmentos de mundo), son de arena, los cuales ahora estoy haciendo modificaciones como por ejemplo, colocar tierra en los bordes.

# Notas dia 3 (Miercoles 2 de Abril) 
# Código inicial completado, si, he usado una inteligencia artificial, pero ahora almenos tenemos una idea de como hacer el juego. Planeo usar algunos tutoriales
# junto a la inteligencia artificial para aprender a hacer el juego por mi propia mano.

# Voy a colocar como será el juego, o almenos como pensamos que será.

# --------COMO SERÁ EL JUEGO--------

# El jugador será Jason y tendrá que matar personas, los cuales solo verán a Jason si este se encuentra dentro de su campo de visión. (El campo de visión es del tamaño de un cuarto de circunferencia, es decir, 90 grados. 45 grados desde el centro hacia arriba y 45 grados desde el centro hacia abajo) . En caso de que Jason se acerque a esas personas sin entrar en el campo de vision, estos no escaparán y morirán en el momento. En caso de que Jason entre en el campo de vision de estos, el jugador entrará en una pantalla de ataque junto a una barra donde habrá debajo una flecha que indica el momento en el que golpeas. la barra tiene un lugar de color verde y el resto es de color rojo. Si le das al verde, matas a la persona, si le das al rojo permites que la persona escape y el jugador recibirá un poco de daño.

El juego comienza en la casa de Jason, que servirá como su punto de aparición.
Allí, Jason podrá conseguir el mapa y su arma principal.
Una vez haya recogido estos objetos, saldrá por la puerta y aparecerá en el centro del mapa.
En ese momento, el reloj comenzará a contar y tendrás 15 minutos para atrapar a todos los campistas.
Si no logras atraparlos antes de que se acabe el tiempo, perderás el juego.
A los 5 minutos de iniciar, aparecerá Tommy Jarvis. 
Él podrá matarte si te dispara tres veces. 
Las balas de Tommy tienen un tiempo de recarga de 30 segundos entre cada disparo.
Para entrar a las casas, Jason deberá romper las puertas, lo cual se hará presionando repetidamente una tecla.
La velocidad de Jason es más lenta que la de los campistas, pero solo si estos tienen energía. 
Esta energía se va agotando con el tiempo.
Cuando la energía de un campista se agota, habrá un tiempo de espera de 10 segundos antes de que se recargue. 
Para que los campistas puedan volver a correr, su barra de energía debe alcanzar al menos el 50% de su capacidad.  
Cuando los campistas no tengan energía, se moverán más lentamente que Jason.
Cuando jason mata a alguine sonara el audio ki ki ki ma ma ma
Enla casa de jason su madre le dira: audio kill them all
Cuando gane la partida su madre le dira: audio good boy jason.
