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
