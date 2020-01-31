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