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

clock = pygame.time.Clock()

"""name = input("Enter the name of your character : ")"""

screen = pygame.display.set_mode((1200, 600))

t=0

running= True

while running:
  dt=clock.tick(60)
  t+=dt
  screen.fill(BLACK)


class Monstre:
    def __init__(self,force,vie=True):
        self.force=force
        self.vie=vie
    
    def deplacement(self):
        #suivre le perso, en tenant compte des murs etc


    def estvaincu(self,autre):
        self.vie=False
        self.donne_force(autre)
        self.donne_vie(autre)

    def avaincu(self,autre):
        #self.dommages=
        autre.vie=False
        autre.donne_force(self)
        autre.donne_vie(self)
    
    def donne_force(self,autre):
        autre.force=self.force
        self.force=0
    
    def donne_vie(self,autre):
        autre.vie=self.vie
        self.vie=0

    #def dommages(self,autre):
        

class Chevalier(Monstre):
    

class Objet:
    def __init__(self, bonus, piece): # le type de la pièce vient de la classe de sandra
        self.donne = bonus
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
