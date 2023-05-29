import pygame
from modules.feldash import Feldash

class Jugador(Feldash):
    
    def __init__(self,imagen,fondo,velocidadJugador,pantalla):
        super().__init__(fondo,velocidadJugador,pantalla)
        
        self.__imagen = imagen
        self.x=100
        self.__fuerzasalto=0
        
    def dibujar(self,y):
        self.pantalla.blit(self.__imagen,(self.x,y))


    def moverY(self,key):
        if key:
            self.pantalla.blit(self.__imagen,(self.x,300))
            