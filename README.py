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
    