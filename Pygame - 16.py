
# coding: utf-8

# In[1]:


import pygame
import sys
import math
from pygame.locals import *

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

points = [(200,75),(300,25),(400,75),(450,25),(450, 125),(400,75),(300,125)]

size = width,height = 800,400

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('First pygame')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    screen.fill(WHITE)
    
    pygame.draw.arc(screen,RED, (100,100, 440,100), 0,math.pi, 1)
    pygame.draw.arc(screen,RED, (100,100, 440,100), math.pi, math.pi*2, 1)
    
    pygame.draw.lines(screen, GREEN, 1, points, 1)
    pygame.draw.line(screen, GREEN, (100,80),(540,250), 1)
    pygame.draw.aaline(screen, RED, (200,80),(640,250), 1)
    
    pygame.display.flip()
    
    clock.tick(20)

