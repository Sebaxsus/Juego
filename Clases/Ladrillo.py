import pygame

class Ladrillo:
    def __init__(self,posx, posy, ancho, alto, color,screen):
        self.posx, self.posy = posx, posy
        self.ancho, self.alto = ancho, alto
        self.color = color
        self.damage = 100
        self.screen = screen
        NEGRO = (0,0,0)
        BLANCO = (255,255,255)
        VERDE = (0,255,0)
        ROJO = (255,0,0)

        if self.color == BLANCO:
            self.vida = 100
        elif self.color == VERDE:
            self.vida = 200
        else:
            self.vida = 300

        
        self.ladrilloRect = pygame.Rect(self.posx, self.posy, self.ancho, self.alto)
        self.ladrillo = pygame.draw.rect(self.screen,self.color,self.ladrilloRect)

    def mostrar(self):
        if self.vida > 0:
            self.cubo = pygame.draw.rect(self.screen, self.color, self.ladrilloRect)
    
    def choque(self):
        self.vida -= self.damage

    def getRect(self):
        return self.ladrilloRect
    
    def getVida(self):
        return self.vida
    
    def getColor(self):
        return self.color