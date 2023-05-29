import pygame
from modules.feldash import Feldash
from modules.jugador import Jugador

pygame.init()

v=pygame.display.set_mode([800,500])
imagen = pygame.image.load("E:\\PROYECTOS\\feldash\\src\\main\\public\\images\\player.png")
#clases
feldash = Feldash((128,128,128),0.5,v)
player = Jugador(imagen,(128,128,128),0.5,v)

#condiguracion
pygame.display.set_caption("Feldash")

ciclo = True

while ciclo:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            ciclo=False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                player.moverY(True)
    
    feldash.jugar(player)
    
    #controles del teclado
    #--- salto
    
    
    pygame.display.update()
    
pygame.quit()