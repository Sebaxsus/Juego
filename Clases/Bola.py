import pygame

class Bola:
    def __init__(self, posx, posy, rad, vel, color, screen, SIZE):
        self.posx, self.posy = posx, posy
        self.rad = rad
        self.vel, self.color = vel, color
        self.xFac, self.yFac = 1,1
        self.screen, self.SIZE = screen, SIZE

        self.bola = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.rad)
    #Metodo para mostrar la bola en pantalla
    def mostrar(self):
        self.bola = pygame.draw.circle(self.screen, self.color, (self.posx, self.posy), self.rad)
    #Metodo para actualizar la pantalla
    def update(self):
        self.posx += self.xFac*self.vel
        self.posy += self.yFac*self.vel
        #Rebotar la bola si toca alguna pared vertical
        if self.posx <= 0 or self.posx >= self.SIZE[0]:
            self.xFac *= -1
        #Rebotar la bola desde el techo esquinero de la pantalla 
        if self.posy <= 0:
            self.yFac *= -1
        #Si la bola toca el fondo esquinero de la pantalla se devuelve True
        if self.posy >= self.SIZE[1]:
            return True

        return False
    #Reinicia la posicion de la bola
    def reset(self):
        self.posx = 0
        self.posy = self.SIZE[1]
        self.xFac, self.yFac =1, -1
    #Metodo para cambiar la direccion de la bola en el plano Y
    def golpe(self):
        self.yFac *= -1
    #Devuelve la bola
    def getRect(self):
        return self.bola