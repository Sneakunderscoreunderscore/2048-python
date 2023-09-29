# 2048 game

from pygame.locals import *
import pygame, sys
import random as r
import time
pygame.init()

FPS = 60
FramesPerSec = pygame.time.Clock()

# colours
black = (0,0,0)
white = (255,255,255)
col2 = (220,220,120)
Display = pygame.display.set_mode((650,650))
pygame.display.set_caption("microsoft windows")

#1st collom  2nd row
grid = [["0","0","0","0"],["0","0","0","0"],["0","0","0","0"],["0","0","0","0"]]
grid_spots = [10,170,330,490]

def drawbg(Display):
    Display.fill(black)
    square = pygame.Rect(10,10,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(170,10,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(330,10,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(490,10,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(10,170,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(10,330,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(10,490,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(170,170,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(170,330,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(170,490,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(330,170,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(330,330,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(330,490,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(490,170,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(490,330,150,150)
    pygame.draw.rect(Display,white,square)
    square = pygame.Rect(490,490,150,150)
    pygame.draw.rect(Display,white,square)


class block2(pygame.sprite.Sprite):
    def __init__(self):
        self.bx = grid_spots[r.randint(0,3)]
        self.by = grid_spots[r.randint(0,3)]
        self.block = pygame.Rect(self.bx,self.by,150,150)
    def draw(self, Display):
        pygame.draw.rect(Display,col2,self.block)

    def update_grid(self):
        x = grid_spots.index(self.bx)
        y = grid_spots.index(self.by)
        grid_spots[x][y] = "2"

b1 = block2()
# game loop
        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    drawbg(Display)
    b1.draw(Display)
    b1.update_grid()
    print(grid_spots)
    
    pygame.display.update()
    FramesPerSec.tick(FPS)
