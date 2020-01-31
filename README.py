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

Grid = np.zeros(CELL_NUMBER)

for i in range(10):
    Grid[3,i]=1

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

screen = pygame.display.set_mode((CELL_SIZE[0]*CELL_NUMBER[0], CELL_SIZE[1]*CELL_NUMBER[1]))

t=0
FPS = 60 #nombre d'images par seconde

running= True

while running:
  dt=clock.tick(FPS)
  t+=dt
  screen.fill(BLACK)

# Ceci ne fait pas partie de la classe a priori
"""for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False   """

for event in pygame.event.get(KEYDOWN):
    if event.key == K_q:
      # on quitte le programme lors d'un appui sur Q
      sys.exit()

if t>200:
    t=0
    draw_level(Grid)
    pygame.display.update()




class Niveau:
    def __init__(self):
        self.nbre_pieces = random.randint(3, 7)


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







