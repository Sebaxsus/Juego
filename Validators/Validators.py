import pygame, sys

pygame.init()

a = pygame.display.Info()

print(a.current_w, a.current_h- 250)

while True:
    pygame.display.set_mode((a.current_w, a.current_h-250)).fill((0,0,0))
    for event in pygame.event.get():
        if event.type == (pygame.KEYDOWN[pygame.K_ESCAPE]):
            print("Ok")
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()