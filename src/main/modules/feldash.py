import pygame

class Feldash:
    #metodo
    def __init__(self,fondo,velocidadJugador,pantalla):
        #Atributos
        self.gravedad =9.8
        self.__fondo = fondo
        self.velocidadJugador= velocidadJugador
        self.pantalla=pantalla
        
    def jugar(self,player):
        self.pantalla.fill(self.__fondo)
        # Definir dimensiones y posición del rectángulo
        x = 0
        y = 350
        ancho = 800
        alto = 150
        #usamos la clase Jugador,: player = Jugador()
        player.dibujar(280)
        
        pygame.draw.rect(self.pantalla,"black",(x,y,ancho,alto))
        
    def gameover():
        pass