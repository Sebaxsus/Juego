import pygame
#Clase Jugador
class Jugador:
    def __init__(self, posx,posy, ancho, alto, vel, color,screen, SIZE):
        self.posx, self.posy = posx, posy
        self.ancho, self.alto = ancho, alto
        self.vel, self.color = vel, color
        self.screen, self.SIZE = screen, SIZE

        self.jugadorRect = pygame.Rect(self.posx, self.posy, self.ancho, self.alto)
        self.jugador =pygame.draw.rect(screen, self.color, self.jugadorRect)
    
    #Metodo para renderizar el objecto en pantalla
    def mostrar(self):
        self.jugador = pygame.draw.rect(self.screen, self.color, self.jugadorRect)

    def update(self, xFac):
        self.posx += self.vel*xFac

        if self.posx <= 0:
            self.posx = 0
        elif self.posx+self.ancho >= self.SIZE[0]:
            self.posx = self.SIZE[0]-self.ancho
        
        self.jugadorRect = pygame.Rect(self.posx, self.posy, self.ancho, self.alto)
    
    def getRect(self):
        return self.jugadorRect
