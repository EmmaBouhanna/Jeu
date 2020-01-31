# Jeu

import sys
import pygame
from pygame.locals import *
import random
import numpy as np

pygame.init()

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
for k in range(22,34):
    grid[3,k]=3
for l in range(3,16):
    grid[l,33]=3


for i in range(65, 91):
    grid[1,i]=1
    grid[13,i]=1
for j in range(1,14):
    grid[j,65]=1
    grid[j,90]=1
grid[13,68]=2
for k in range(13,16):
    grid[k,68]=3

for j in range(38, 54):
    grid[j,40]=1
    grid[j,65]=1
for i in range(40,66):
    grid[38,i]=1
    grid[53,i]=1
grid[38,55]=2
grid[40,65]=2
for k in range(30,39):
    grid[k,55]=3

for i in range (80,111):
    grid[35,i]=1
    grid[45,i]=1
for j in range(35,46):
    grid[j,80]=1
    grid[j,110]=1
grid[40,80] = 2
grid[35,83] = 2
for k in range(65,81):
    grid[40,k]=3
for k in range(33,36):
    grid[k,83]=3
for l in range(55,84):
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
            pos = l, c
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

# Ceci ne fait pas partie de la classe a priori
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False   

for event in pygame.event.get(KEYDOWN):
    if event.key == K_q:
      # on quitte le programme lors d'un appui sur Q


if t>200:
    t=0
    draw_level(grid)
    pygame.display.update()

class Monstre:
    def __init__(self,force,vie=True):
        self.force
    
    def deplacement()
    def vaincu
        self.vie
        self.donne_force
        self.donne_vie
    def avaincu
        self.dommages=


class Chevalier(Monstre):
    

class Objet:
    def __init__(self, piece): # le type de la pièce vient de la classe de sandra
        self.donne = 0
        self.localisation = (random.randint(len(piece.largeur), random.randint(len(piece.longueur)))


class Potion(Objet):
    def __init__(self, piece):
        self.donne = 1 # point de vie
        self.localisation = Objet.localisation
class Nourriture(Objet):
    def __init__(self,piece):
        self.donne = 1 # point de force 
        self.localisation = Objet.localisation

class Argent(Objet):
    def __init__(self):
        self.donne = random.randint(5, 11)
        self.localisation = Objet.localisation


class Armure(Objet):
    def __init__(self, piece):
        self.donne = random.randint(1,5)
        self.localisation = Objet.localisation

class Arme(Objet):
    def __init(self, piece)
        self.localisation = Objet.localisation
        self.donne = random.randint(4, 6) 



class Personnage:
    def __init__(self):
        self.force = 10
        self.pt_vie = 3
        self.sac = []
        self.armes = []
        self.pos = [] 
    
    def __repr__(self):
        print("@")
    
    def attack(self):
          
        
    def move_me(self, dx, dy):
        x = self.pos[0]+dx
        y = self.pos[1]+dy
        el = grid.get_el(x*grid.cell_size, (y)*grid.cell_size)
        
        if el == "." or el == "+" or el == "#":
            self.pos[0] = x
            self.pos[1] = y 
            return True
        # if el == "B" or el == "K":
            
        else:
            return False





