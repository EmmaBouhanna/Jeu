# Jeu

import sys
import pygame
from pygame.locals import *
import random
import numpy as np

pygame.init()

for event in pygame.event.get():   

    if event.type == QUIT:    

        pygame.quit()
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Grid 
CELL_SIZE = (10, 10)
CELL_NUMBER = (60, 120)
grid = np.zeros((60,120))#salle1
   
for i in range (3,23):
    grid[2,i]=1
    grid[5,i]=1
grid[3,3]=1
grid[4,3]=1
grid[4,22]=1
grid[3,22]=2

for i in range(28,70): #salle2
    grid[15,i]=1
    grid[30,i] = 1
for j in range (15,31):
    grid[j,28] = 1
    grid[j,69] = 1
grid[15,33]=2
grid[15,68]=2
grid[30,55]=2
for k in range(23,33):
    grid[3,k]=3
for l in range(3,15):
    grid[l,33]=3


for i in range(65, 91):
    grid[1,i]=1
    grid[13,i]=1
for j in range(1,14):
    grid[j,65]=1
    grid[j,90]=1
grid[13,68]=2
for k in range(14,15):
    grid[k,68]=3

for j in range(38, 54):
    grid[j,40]=1
    grid[j,65]=1
for i in range(40,66):
    grid[38,i]=1
    grid[53,i]=1
grid[38,55]=2
grid[40,65]=2
for k in range(31,38):
    grid[k,55]=3

for i in range (80,111):
    grid[35,i]=1
    grid[45,i]=1
for j in range(35,46):
    grid[j,80]=1
    grid[j,110]=1
grid[40,80] = 2
grid[35,83] = 2
for k in range(66,80):
    grid[40,k]=3
for k in range(34,35):
    grid[k,83]=3
for l in range(56,84):
    grid[33,l]=3


def draw_cell(pos, color=WHITE):
  x,y=pos
  for line in range(CELL_SIZE[1]):
    for col in range(CELL_SIZE[0]):
      #itertools product
      screen_pos=(CELL_SIZE[0]*x+col, CELL_SIZE[1]*y+line)
      screen.set_at(screen_pos,color)

def draw_level(Grid):
    for l in range(60):
        for c in range(120):
            pos = c, l
            if Grid[l,c] == 1 : #mur
                draw_cell(pos)
            elif Grid[l,c] == 2 : #porte
                draw_cell(pos, BLUE)
            elif Grid[l,c] == 3 : #couloir
                draw_cell(pos, GREY)

clock = pygame.time.Clock()
name = input("Enter the name of your character : ")

screen = pygame.display.set_mode((CELL_SIZE[1]*CELL_NUMBER[1], CELL_SIZE[0]*CELL_NUMBER[0]))

t=0
FPS = 60 #nombre d'images par seconde

running= True

while running:
    dt=clock.tick(FPS)
    t+=dt
    screen.fill(BLACK)
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  """ 
    for event in pygame.event.get(KEYDOWN):
        if event.key == K_q:
            sys.exit()
        # on quitte le programme lors d'un appui sur Q
    if t>200:
        t=0
        draw_level(grid)
        perso = pygame.image.load("superhero-drawing-001.jpg").convert()
        screen.blit(perso, (4,5))
        pygame.display.update()
        

 



