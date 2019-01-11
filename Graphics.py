import pygame
from pygame.locals import*

background_color = (255,255,255)
(width, height) = (500, 800)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bit Life Graphics")
screen.fill(background_color)
        
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 10, 500, -200), 70)
pygame.draw.rect(screen, (40, 116, 166), pygame.Rect(0, 500, 500, 0), 100)
pygame.draw.rect(screen, (40, 116, 166), pygame.Rect(0, 500, 500, 0), 100)
pygame.draw.circle(screen, (253, 254, 254), [30, 23], 16, 2)
pygame.draw.line(screen, (253, 254, 254), [25,26], [35,26], 2)
pygame.draw.line(screen, (253, 254, 254), [25,22], [35,22], 2)
pygame.draw.line(screen, (253, 254, 254), [25,18], [35,18], 2)
pygame.draw.circle(screen, (46, 204, 113), [245, 500], 60, 0)
pygame.draw.circle(screen, (253, 254, 254), [245, 500], 58, 5)


pygame.font.init()
myfont = pygame.font.SysFont('Chunkfive', 40)
textsurface = myfont.render('BitLyfe', False, (255, 255, 0))
screen.blit(textsurface,(200,10))
 
pygame.init()
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
