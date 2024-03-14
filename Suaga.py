import pygame, random, time

pygame.init()

#      Ancho, Alto
SIZE = (600, 500)

#Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)

#Fuente de los textos
fuenteTexto = pygame.font.Font('freesansbold.ttf', 15)

#Creo la pantalla y le pongo un titulo
screen = pygame.display.set_mode(size=SIZE)
pygame.display.set_caption("Pin Pon?")

#Tasa de refresco de la pantalla
clock = pygame.time.Clock()
FPS = 30

class Ladrillo:
    def __init__(self,posx, posy, ancho, alto, color):
        self.posx, self.posy = posx, posy
        self.ancho, self.alto = ancho, alto
        self.color = color
        self.damage = 100

        if color == BLANCO:
            self.vida = 100
        else:
            self.vida = 100

        
        self.ladrilloRect = pygame.Rect(self.posx, self.posy, self.ancho, self.alto)
        self.ladrillo = pygame.draw.rect(screen,self.color,self.ladrilloRect)

    def mostrar(self):
        if self.vida > 0:
            self.cubo = pygame.draw.rect(screen, self.color, self.ladrilloRect)
    
    def choque(self):
        self.vida -= self.damage

    def getRect(self):
        return self.ladrilloRect
    
    def getVida(self):
        return self.vida
    
class Bola:
    def __init__(self, posx, posy, rad, vel, color):
        self.posx, self.posy = posx, posy
        self.rad = rad
        self.vel, self.color = vel, color
        self.xFac, self.yFac = 1,1

        self.bola = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.rad)
    #Metodo para mostrar la bola en pantalla
    def mostrar(self):
        self.bola = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.rad)
    #Metodo para actualizar la pantalla
    def update(self):
        self.posx += self.xFac*self.vel
        self.posy += self.yFac*self.vel
        #Rebotar la bola si toca alguna pared vertical
        if self.posx <= 0 or self.posx >= SIZE[0]:
            self.xFac *= -1
        #Rebotar la bola desde el techo esquinero de la pantalla 
        if self.posy <= 0:
            self.yFac *= -1
        #Si la bola toca el fondo esquinero de la pantalla se devuelve True
        if self.posy >= SIZE[1]:
            return True

        return False
    #Reinicia la posicion de la bola
    def reset(self):
        self.posx = 0
        self.posy = SIZE[1]
        self.xFac, self.yFac =1, -1
    #Metodo para cambiar la direccion de la bola en el plano Y
    def golpe(self):
        self.yFac *= -1
    #Devuelve la bola
    def getRect(self):
        return self.bola

#Funcion para verificar colision entre la bola y un ladrillo
def verChoque(ladrillo, bola):
    if pygame.Rect.colliderect(ladrillo, bola):
        return True
    else:
        return False
    
#Funcion para colocar ladrillos
def colocarLadrillos(ancho, alto, separacionH, separacionV):
    listaLadrillos = []

    for i in range(0, SIZE[0], ancho+separacionH):
        for j in range(0, SIZE[1]//2, alto+separacionV):
            listaLadrillos.append(Ladrillo(i,j, ancho, alto,BLANCO))
    
    return listaLadrillos

#Funcion Fin del juego
def gameOver():
    gameOver = True

    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

class Jugador:
    def __init__(self, posx,posy, ancho, alto, vel, color):
        self.posx, self.posy = posx, posy
        self.ancho, self.alto = ancho, alto
        self.vel, self.color = vel, color

        self.jugadorRect = pygame.Rect(self.posx, self.posy, self.ancho, self.alto)
        self.jugador =pygame.draw.rect(screen, self.color, self.jugadorRect)
    
    #Metodo para renderizar el objecto en pantalla
    def mostrar(self):
        self.jugador = pygame.draw.rect(screen, self.color, self.jugadorRect)

    def update(self, xFac):
        self.posx += self.vel*xFac

        if self.posx <= 0:
            self.posx = 0
        elif self.posx+self.ancho >= SIZE[0]:
            self.posx = SIZE[0]-self.ancho
        
        self.jugadorRect = pygame.Rect(self.posx, self.posy, self.ancho, self.alto)
    
    def getRect(self):
        return self.jugadorRect

def lost(vidas, bola):
    
    while True:
        keys = pygame.key.get_pressed()
        time.sleep(1)
        print(keys[pygame.K_SPACE])
        if keys[pygame.K_SPACE]:
            break
    vidas -= 1
    bola.reset()
    return True


def main():
    running = True
    vidas = 3
    puntuacion = 0

    textoPuntuacion = fuenteTexto.render("Puntuacion",True,BLANCO)
    rectTextoPuntuacion = textoPuntuacion.get_rect()
    rectTextoPuntuacion.center = (50, SIZE[1]-10)

    textoVidas = fuenteTexto.render("Vidas", True, BLANCO)
    rectTextoVidas = textoVidas.get_rect()
    rectTextoVidas.center = (180, SIZE[1]-10)

    jugador = Jugador(0, SIZE[1]-50, 100, 20, 10, BLANCO)
    jugadorXFac = 0

    bola = Bola(0, SIZE[1]-150, 7, 5, BLANCO)

    anchoLadrillo, altoLadrillo = 40, 15
    separacionH, separacionV = 20, 20

    listaLadrillos = colocarLadrillos(anchoLadrillo, altoLadrillo, separacionH, separacionV)

    #Bucle del juego
    while running:
        screen.fill(NEGRO)
        screen.blit(textoPuntuacion, rectTextoPuntuacion)
        screen.blit(textoVidas, rectTextoVidas)\
        
        keys = pygame.key.get_pressed()

        textoPuntuacion = fuenteTexto.render(f"Puntuacion: {puntuacion}", True, BLANCO)
        textoVidas = fuenteTexto.render(f"Vidas: {vidas}", True, BLANCO)

        #Si todos los ladrillos se destruyeron entonces generar nuevos
        if not listaLadrillos:
            listaLadrillos = colocarLadrillos(anchoLadrillo, altoLadrillo, separacionH, separacionV)
        
        
        if vidas <= 0:
            running = gameOver()

            while listaLadrillos:
                listaLadrillos.pop(0)
            
            vidas = 3
            puntuacion = 0
            listaLadrillos = colocarLadrillos(anchoLadrillo, altoLadrillo, separacionH, separacionV)

        #Manejar los eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jugadorXFac = -1
                if event.key == pygame.K_RIGHT:
                    jugadorXFac = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    jugadorXFac = 0
        
        #Verificar Colision
        if(verChoque(jugador.getRect(), bola.getRect())):
            bola.golpe()
        for ladrillo in listaLadrillos:
            if(verChoque(ladrillo.getRect(), bola.getRect())):
                bola.golpe()
                ladrillo.choque()

                if ladrillo.getVida() <= 0:
                    listaLadrillos.pop(listaLadrillos.index(ladrillo))
                    puntuacion += 5
        
        #Actualizar
        jugador.update(jugadorXFac)
        vidaPerdida = bola.update()

        if vidaPerdida:
            print(vidas)
            if keys[pygame.K_SPACE]:
                vidas -= 1
                bola.reset()
                
                
        
        #mostrar en pantalla
        jugador.mostrar()
        bola.mostrar()

        for ladrillo in listaLadrillos:
            ladrillo.mostrar()
        
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__": 
    main() 
    pygame.quit()       