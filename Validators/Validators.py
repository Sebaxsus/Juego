import pygame, sys

pygame.init()

a = pygame.display.Info()

imgBola = pygame.image.load('PF/Multimedia/bola.jpg')

screen = pygame.display.set_mode((a.current_w, a.current_h-250))

print(a.current_w, a.current_h- 250)

while True:
    screen.fill((0,0,0))
    rect = imgBola.get_rect()
    rect.center=(200,300)
    screen.blit(imgBola, rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()