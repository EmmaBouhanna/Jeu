# Jeu


import sys
import pygame
from pygame.locals import *
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

CELL_SIZE = (20, 20)

def draw_cell(pos, color=WHITE):
  x,y=pos
  for line in range(CELL_SIZE[1]):
    for col in range(CELL_SIZE[0]):
      #itertools product
      screen_pos=(CELL_SIZE[0]*x+col, CELL_SIZE[1]*y+line)
      screen.set_at(screen_pos,color)

clock = pygame.time.Clock()
name = input("Enter the name of your character : ")

screen = pygame.display.set_mode((1200, 600))

t=0
FPS = 60 #nombre d'images par seconde

running= True

while running:
  dt=clock.tick(FPS)
  t+=dt
  screen.fill(RED)

  for event in pygame.event.get(KEYDOWN):
    if event.key == K_q:
      sys.exit()
      # on quitte le programme lors d'un appui sur Q
  if t>200:
    t=0
    pos = 1, 1
    draw_cell(pos)
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
        self.donne = random.randint(4, 6) """
