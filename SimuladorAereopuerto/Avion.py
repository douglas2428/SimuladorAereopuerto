import threading
from time import sleep

class Avion(threading.Thread):
    def __init__(self, posx, posy, x, y, ancho, width, height, color, velocidad, inicio, final):
        threading.Thread.__init__(self)
        self.posx = posx
        self.posy = posy
        self.x = x
        self.y = y
        self.ancho = ancho
        self.width = width
        self.height = height
        self.color = color
        self.velocidad = velocidad
        self.ate = False
        self.inicio = inicio
        self.final = final
        self.start()
        
    def mover(self, x, y):
        self.posx = x
        self.posy = y 
    
    def aterrizar(self, inicio, final):
        bx = False
        by = False
        x = self.posx
        y = self.posy
        pendiente1 = 1
        pendiente2 = 1
        pendiente = (final[1] - inicio[1]) / (final[0] - inicio[0])
        if pendiente > 0:
            pendiente1 = pendiente
        elif pendiente < 0:
            pendiente2 = abs(pendiente)   
           
        print(pendiente)
        
        print("ATERRIZANDO")
        
        self.velocidad = 1
        while not bx or not by:
            if x < inicio[0]:
                x += self.velocidad
            elif x > inicio[0]:
                x -= self.velocidad
            if y < inicio[1]:
                y += self.velocidad
            elif y > inicio[1]:
                y -= self.velocidad 
            self.mover(x, y)      
            if x == inicio[0]:
                bx = True
            
            if y <= inicio[1] + 1 and y >= inicio[1] - 1:
                by = True
            sleep(0.05)
            
        bx = False
        by = False
        x = self.posx
        y = self.posy
        
        print("Comienzo")
        print(x)
        print(y)
        
        while not bx or not by:
            if x < final[0]:
                x += self.velocidad
            if x > final[0]:
                x -= self.velocidad
            if y < final[1]:
                y += self.velocidad * pendiente1
            if y > final[1]:
                y -= self.velocidad * pendiente2
            self.mover(x, y)
                  
            if x >= final[0] - 1:
                bx = True
                # by=True
            if y <= inicio[1] + 1 and y >= inicio[1] - self.velocidad - 1:
                by = True
            sleep(0.05)   
               
        print("ATERRIZAJE COMPLETADO")         
        self.ate = False               
                        
                       
    def run(self):
        incx = self.velocidad
        incy = self.velocidad
        
        while True:
            if not self.ate: 
                x = self.posx
                y = self.posy
            
            
                x += incx
                #para que no se salga de la pantalla
                if incx == self.velocidad and x + self.ancho > self.width - self.x:
                    incx = -self.velocidad
                if incx == -self.velocidad and x - self.ancho < 0:
                    incx = self.velocidad
                if incy == self.velocidad and y > self.height - self.y:
                    incy = -self.velocidad
                if incy == -self.velocidad and y < 0:
                    incy = self.velocidad        
                
                self.mover(x, y);
                sleep(0.05)   
            else:
                self.aterrizar(self.inicio, self.final)
