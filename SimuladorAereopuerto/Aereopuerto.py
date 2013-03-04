import threading
import pygame, sys
from pygame.locals import QUIT, KEYDOWN, K_DOWN, K_UP
from Avion import Avion

if __name__ == '__main__':
    pass

pygame.init()

# Definimos el color de fondo y el de la diagonal

COLOR_FONDO = (50, 150, 200)
COLOR_LINEA1 = (0, 255, 255)
COLOR_LINEA2 = (0, 0, 255)
colora1 = (0, 0, 255)
colora = (0, 255, 255)
semaforoPistaP = threading.Semaphore(2)
semaforoPistaD = threading.Semaphore(2)

aviones = [
           Avion(100, 100, 4, 2, 10, 400, 400, colora, 1, [15, 15], [409, 109]),
           Avion(0, 100, 4, 2, 10, 400, 200, colora1, 1, [15, 139], [409, 45])
          ]
# Definimos el tamanio de la aplicacion y la tasa de refresco
pantalla = pygame.display.set_mode((600, 400))
refresco = pygame.time.Clock()

tiempoEntra = 1

while True:
    time_passed = refresco.tick(50)
    
    # Comprobamos el cierre de la aplicacion y en caso afirmativo lanzamos la funcion salir
    for event in pygame.event.get():
        if event.type == QUIT:
            for a in aviones:
                a._stop()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                aviones[0].ate = True
                #aviones[1].inicio=[15,115]
                #aviones[1].final=[409,209]
                aviones[1].ate = True
            elif event.key == K_UP:
                aviones.append(Avion(100, 100, 4, 2, 10, 400, 400, (0, 255, 125), 1, [15, 15], [409, 109]))      

    if tiempoEntra / 1000 == 1:
        tiempoEntra = 1 
        aviones.append(Avion(100, 100, 4, 2, 10, 400, 400, (0, 255, 125), 1, [15, 15], [409, 109]))
        #semaforo.release()'''
        print("entroooo")
       
    # Fijamos el color de fondo y las lineas de diferentes colores, y lo sacamos por display
    pantalla.fill(COLOR_FONDO)
    pygame.draw.aaline(pantalla, COLOR_LINEA1, (15, 15), (409, 109))
    #pygame.draw.aaline(pantalla, COLOR_LINEA2, (15, 115), (409, 209))
    pygame.draw.aaline(pantalla, COLOR_LINEA2, (15, 139), (409, 45))
    for a in aviones:
        pygame.draw.rect(pantalla, a.color, (a.posx, a.posy, a.x, a.y), a.ancho)
        fuente = pygame.font.Font(None, 13)
        texto = fuente.render('x:' + str(a.posx), 0, a.color)
        pantalla.blit(texto, (a.posx + 5, a.posy + 5))
        texto = fuente.render('y:' + str(int(a.posy)), 0, a.color)
        pantalla.blit(texto, (a.posx + 5, a.posy + 13))
    
    tiempoEntra += 1

    pygame.display.flip()
