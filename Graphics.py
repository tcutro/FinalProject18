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

a = 24
b = 56
c = 78
d = 97
def health_bars(player_stats):
    self.health = 100
    self.look = 100
    self.personality = 100
    self.smarts = 100
    if self.health <= 0:
        self.kill()
        
    if self.health >= 31:
        col = (46, 204, 113)
    elif self.health >= 13:
        col = (255, 111, 0)
    elif self.health >= 1:
        col = (178, 34, 34)
    max health = 100
    current health = a
    percentage = current health/max health
    
    pygame.draw.rect(screen, (234, 242, 248), pygame.Rect(195, 707, 290, 25), 0)

 
pygame.draw.rect(screen, (234, 242, 248), pygame.Rect(195, 585, 290, 25), 0)

pygame.draw.rect(screen, (234, 242, 248), pygame.Rect(195, 625, 290, 25), 0)

pygame.draw.rect(screen, (234, 242, 248), pygame.Rect(195, 665, 290, 25), 0)

pygame.draw.rect(screen, (234, 242, 248), pygame.Rect(195, 707, 290, 25), 0)

pygame.draw.rect(screen, (235, 237, 239), pygame.Rect(0, 46, 500, 45), 0)

pygame.draw.circle(screen, (253, 254, 254), [30, 23], 16, 2)
pygame.draw.line(screen, (253, 254, 254), [25,26], [35,26], 2)
pygame.draw.line(screen, (253, 254, 254), [25,22], [35,22], 2)

pygame.draw.line(screen, (144, 148, 151), [195,570], [195,745], 2)

pygame.draw.line(screen, (253, 254, 254), [25,18], [35,18], 2)

pygame.draw.circle(screen, (46, 204, 113), [245, 500], 60, 0)
pygame.draw.circle(screen, (253, 254, 254), [245, 500], 58, 5)

pygame.draw.line(screen, (253, 254, 254), [245,470], [245,500], 5)
pygame.draw.line(screen, (253, 254, 254), [225,485], [265,485], 5)

pygame.draw.line(screen, (93, 109, 126), [90,450], [90,550], 2)

pygame.draw.line(screen, (93, 109, 126), [180,450], [180,550], 2)

pygame.draw.line(screen, (93, 109, 126), [400,450], [400,550], 2)

pygame.draw.line(screen, (93, 109, 126), [310,450], [310,550], 2)

pygame.draw.line(screen, (28, 40, 51), [0,90], [500,90], 1)

pygame.draw.arc()


pygame.font.init()
myfont = pygame.font.SysFont('Chunkfive', 40)
textsurface = myfont.render('BitSkool', False, (255, 255, 0))
screen.blit(textsurface,(200,10))

myfont = pygame.font.SysFont('Chunkfive', 35)
textsurface = myfont.render('Happiness', False, (144, 148, 151))
screen.blit(textsurface,(45,585))

myfont = pygame.font.SysFont('Chunkfive', 35)
textsurface = myfont.render('Health', False, (144, 148, 151))
screen.blit(textsurface,(93,625))

myfont = pygame.font.SysFont('Chunkfive', 35)
textsurface = myfont.render('Smarts', False, (144, 148, 151))
screen.blit(textsurface,(87,665))

myfont = pygame.font.SysFont('Chunkfive', 35)
textsurface = myfont.render('Popularity', False, (144, 148, 151))
screen.blit(textsurface,(50,705))

myfont = pygame.font.SysFont('Chunkfive', 35)
textsurface = myfont.render('Month', False, (253, 254, 254))
screen.blit(textsurface,(210,510))

pygame.init()
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
x = "male"

if x == "male":

elif x == "female:
