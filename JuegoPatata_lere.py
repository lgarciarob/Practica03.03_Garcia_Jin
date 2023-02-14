import pygame
import time
#from Ladrillo import Block

#Iniciacion de Pygame
pygame.init()

#Iniciacion de carga de sonidos
pygame.mixer.init()

#Crear la ventana del juego
ventana = pygame.display.set_mode((640,480))

#Nombre del titulo de la ventana
pygame.display.set_caption("Patata_lere")

#Creamos nuestra pelota
patata = pygame.image.load("patata_lere (1) (1).png")
patatarect = patata.get_rect()

#La velocidad a la que se mueve la pelota
speed = [3,3]
speed_patata = 1

#Posicion de la pelota en la pantalla
patatarect.move_ip(320,240)

#Crear nuestra barra
sarten = pygame.image.load("sarten_lere2 (2).png")
sartenrect = sarten.get_rect()

#Posicion de la barra en la pantalla
sartenrect.move_ip(240,450)

#Crear fondos
fondo_game_over = pygame.image.load("game over (1).png")
fondo = pygame.image.load("cocina_lere (1) (1).png")
fondo_winner = pygame.image.load("win.png")
#Crear sonidos
sonido_fondo = pygame.mixer.music.load("Like-A-Dino_.wav")
pygame.mixer.music.play(-1)
sonido_perdedor = pygame.mixer.Sound("Sonido-de-perdedor.wav")
sonido_ganador = pygame.mixer.Sound("Sonido-de-ganador.wav")
#Crear ladrillos

ladrillo = pygame.image.load("Bloque_Ladrillo.png")
ladrillorect = ladrillo.get_rect()

ganador = True
class Ladrillo:
    def __init__(self, pos_x, pos_y, imagen):
        self.rect = pygame.Rect(pos_x, pos_y, imagen.get_width(), imagen.get_height())
        self.imagen = imagen

ladrillos = []
for fila in range(2):
   for columna in range(12):
       pos_x = columna * ladrillo.get_width()
       pos_y = fila * ladrillo.get_height()
       ladrillos.append(Ladrillo(pos_x, pos_y, ladrillo))


jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

#Configuracion de controles
    keys = pygame.key.get_pressed()

    if keys [pygame.K_LEFT]:
        sartenrect = sartenrect.move(-6,0)
    if keys [pygame.K_RIGHT]:
        sartenrect = sartenrect.move(6,0)
   #limites de borde
    if sartenrect.right > 640:
        sartenrect.right = 640
    if sartenrect.left < 0:
        sartenrect.left = 1
#Colisiones
    if sartenrect.colliderect(patatarect):
        speed[1] = -speed[1]
        #aumento de velocidad por colision de barra
        if speed[0] < 10 and speed[1] < 10:
            speed[0] += 1
            if speed[1] < 0:
                speed[1] -= 2
            else:
                speed[1] += 2

    patatarect = patatarect.move(speed)
    if patatarect.left < 0 or patatarect.right > ventana.get_width():
        speed[0] = -speed[0]

    if patatarect.top < 0:
        speed[1] = -speed[1]



    if patatarect.bottom > ventana.get_height() and len(ladrillos) > 0:
#quitar ladrilllos en la pantalla final
        ganador = False
        ladrillos.clear()
        ventana.blit(fondo_game_over, (0, 0))
        pygame.mixer.Sound.play(sonido_perdedor)
        pygame.mixer.music.stop()
        jugando = False

    else:
        ventana.fill((252,243,207))
        ventana.blit(fondo, (0, 0))
        ventana.blit(patata, patatarect)
        ventana.blit(sarten, sartenrect)
#rompe ladrillo
    for ladrillo in ladrillos:
        ventana.blit(ladrillo.imagen, ladrillo.rect)
        if patatarect.colliderect(ladrillo.rect):
            ladrillos.remove(ladrillo)
            speed[1] = -speed[1]
    if len(ladrillos) == 0 and ganador:
        ventana.blit(fondo_winner, (0,0))
        pygame.mixer.Sound.play(sonido_ganador)
        pygame.mixer.music.stop()
        jugando = False


    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()
    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)

time.sleep(5)
pygame.quit()
