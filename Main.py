import pygame, random, time
from Clases.Jugador import Jugador
from Clases.Bola import Bola
from Clases.Ladrillo import Ladrillo

pygame.init()

pygame.mixer.init()

sonidoGolpe = pygame.mixer.Sound('PF/Multimedia/ping-82822.mp3')
sonidoBreak = pygame.mixer.Sound('PF/Multimedia/hit-someting-6037.mp3')
sonidoWin = pygame.mixer.Sound('PF/Multimedia/decidemp3-14575.mp3')
sonidoLose = pygame.mixer.Sound('PF/Multimedia/negative_beeps-6008.mp3')

#Obtengo la info de la pantalla en la que se va a ejecutar el programa
display = pygame.display.Info()

#      Ancho              , Alto
#SIZE = (display.current_w, display.current_h)
SIZE = (600,500)

bgImg = pygame.transform.scale(pygame.image.load('PF/Multimedia/download.jpg'), (SIZE))

#Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)

#Fuente de los textos
fuenteTexto = pygame.font.Font('freesansbold.ttf', 15)
listaRandColor = []

#Creo la pantalla y le pongo un titulo
screen = pygame.display.set_mode(size=SIZE)
pygame.display.set_caption("Pin Pon?")

#Tasa de refresco de la pantalla
clock = pygame.time.Clock()
FPS = 30



#Funcion para verificar colision entre la bola y un ladrillo
def verChoque(ladrillo, bola):
    if pygame.Rect.colliderect(ladrillo, bola):
        return True
    else:
        return False
    
#Funcion para colocar ladrillos
def colocarLadrillos(ancho, alto, separacionH, separacionV, nivel): #Pedir Nivel, Si Nivel es 2 entonces random.choice([BLANCO, VERDE]), Si Nivel es 3 entonces random.choice([BLANCO, VERDE, ROJO])
    listaLadrillos = []
    
    match nivel:
        case 1:
            listaRandColor.append(BLANCO)
        case 2:
            #listaRandColor = [BLANCO, VERDE]
            listaRandColor.append(VERDE)
        case 3:
            #listaRandColor = [BLANCO, VERDE, ROJO]
            listaRandColor.append(ROJO)
    #print(nivel, " ", listaRandColor)
    for i in range(0, SIZE[0], ancho+separacionH):
        for j in range(0, SIZE[1]//2, alto+separacionV):
            listaLadrillos.append(Ladrillo(i,j, ancho, alto,random.choice(listaRandColor),screen))
    
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

def velocidadNivel(nivel):
    vel = 10
    match nivel:
        case 1:
            vel = 10
        case 2:
            vel = 15
        case 3:
            vel = 20
    return vel

def main():
    running = True
    vidas = 3
    puntuacion = 0
    nivel = 1

    textoPuntuacion = fuenteTexto.render("Puntuacion",True,BLANCO)
    rectTextoPuntuacion = textoPuntuacion.get_rect()
    rectTextoPuntuacion.center = (50, SIZE[1]-10)

    textoVidas = fuenteTexto.render("Vidas", True, BLANCO)
    rectTextoVidas = textoVidas.get_rect()
    rectTextoVidas.center = (180, SIZE[1]-10)

    textoNivel = fuenteTexto.render("Nivel", True, BLANCO)
    rectTextoNivel = textoNivel.get_rect()
    rectTextoNivel.center = (300, SIZE[1]-10)

    velJ = 30 #Velocidad del Jugador
    #velB = 10 #Velocidad de la bola

    jugador = Jugador(0, SIZE[1]-50, 100, 20, velJ, BLANCO, screen, SIZE)
    jugadorXFac = 0

    bola = Bola(0, SIZE[1]-150, 7, velocidadNivel(nivel), ROJO, screen, SIZE)

    anchoLadrillo, altoLadrillo = 40, 15
    separacionH, separacionV = 20, 20

    listaLadrillos = colocarLadrillos(anchoLadrillo, altoLadrillo, separacionH, separacionV, nivel)

    #Bucle del juego
    while running:
        screen.fill(NEGRO)
        screen.blit(bgImg, (0, 0))
        screen.blit(textoPuntuacion, rectTextoPuntuacion)
        screen.blit(textoVidas, rectTextoVidas)
        screen.blit(textoNivel, rectTextoNivel)
        
        keys = pygame.key.get_pressed()

        textoPuntuacion = fuenteTexto.render(f"Puntuacion: {puntuacion}", True, BLANCO)
        textoVidas = fuenteTexto.render(f"Vidas: {vidas}", True, BLANCO)
        textoNivel = fuenteTexto.render(f"Nivel: {nivel}", True, BLANCO)

        #Si todos los ladrillos se destruyeron entonces generar nuevos
        if not listaLadrillos:
            sonidoWin.play()
            nivel += 1
            listaLadrillos = colocarLadrillos(anchoLadrillo, altoLadrillo, separacionH, separacionV, nivel)
        
        
        if vidas <= 0:
            sonidoLose.play()
            nivel = 1
            running = gameOver()

            while listaLadrillos:
                listaLadrillos.pop(0)
            
            vidas = 3
            puntuacion = 0
            listaLadrillos = colocarLadrillos(anchoLadrillo, altoLadrillo, separacionH, separacionV, nivel)

        #Manejar los eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jugadorXFac = -1
                if event.key == pygame.K_RIGHT:
                    jugadorXFac = 1
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_F2:
                    sonidoWin.play()
                    nivel += 1
                    while listaLadrillos:
                        listaLadrillos.pop(0)

                    listaLadrillos = colocarLadrillos(anchoLadrillo, altoLadrillo, separacionH, separacionV, nivel)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    jugadorXFac = 0
        
        #Verificar Colision
        if(verChoque(jugador.getRect(), bola.getRect())):
            bola.golpe()
            sonidoGolpe.play()
        for ladrillo in listaLadrillos:
            if(verChoque(ladrillo.getRect(), bola.getRect())):
                bola.golpe()
                ladrillo.choque()

                if ladrillo.getVida() <= 0:
                    if ladrillo.getColor() == BLANCO:
                        listaLadrillos.pop(listaLadrillos.index(ladrillo))
                        puntuacion += 5
                    if ladrillo.getColor() == VERDE:
                        listaLadrillos.pop(listaLadrillos.index(ladrillo))
                        puntuacion += 10
                    if ladrillo.getColor() == ROJO:
                        listaLadrillos.pop(listaLadrillos.index(ladrillo))
                        puntuacion += 20
                    sonidoBreak.play()
        
        #Actualizar
        jugador.update(jugadorXFac)
        vidaPerdida = bola.update()

        if vidaPerdida:
            #print(vidas)
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
    sonidoGolpe.set_volume(0.3)
    sonidoBreak.set_volume(0.2) 
    sonidoLose.set_volume(0.5)
    sonidoWin.set_volume(0.5)
    main() 
    pygame.quit()       