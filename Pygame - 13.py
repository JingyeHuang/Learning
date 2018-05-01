
# coding: utf-8

# In[1]:


import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

points = [(200,75),(300,25),(400,75),(450,25),(450, 125),(475,75),(300,125)]

size = width,height = 600,400

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('First pygame')



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    screen.fill(WHITE)
    
    pygame.draw.polygon(screen,GREEN, points, 0)
    
    pygame.display.flip()
    
    clock.tick(20)

