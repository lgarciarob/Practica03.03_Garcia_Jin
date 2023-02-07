import pygame
#Iniciacion de Pygame
pygame.init()
#Crear la ventana del juego
ventana = pygame.display.set_mode((640,480))
#Nombre del titulo de la ventana
pygame.display.set_caption("Patata_lere")

#Creamos nuestra pelota
patata = pygame.image.load("patata_lere (1) (1).png")
patatarect = patata.get_rect()
#La velocidad a la que se mueve la pelota
speed = [4,4]
#Posicion de la pelota en la pantalla
patatarect.move_ip(0,0)

sarten = pygame.image.load("sarten_lere2 (2).png")
sartenrect = sarten.get_rect()
sartenrect.move_ip(240,450)

fondo = pygame.image.load("cocina_lere (1) (1).png")

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]:
        sartenrect = sartenrect.move(-3,0)
    if keys [pygame.K_RIGHT]:
        sartenrect = sartenrect.move(3,0)

    if sartenrect.colliderect(patatarect):
        speed[1] = -speed[1]
    patatarect = patatarect.move(speed)
    if patatarect.left < 0 or patatarect.right > ventana.get_width():
        speed[0] = -speed[0]

    if patatarect.top < 0 or patatarect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    ventana.fill((252,243,207))
    ventana.blit(fondo, (0, 0))
    ventana.blit(patata, patatarect)
    ventana.blit(sarten, sartenrect)
    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()
    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()
