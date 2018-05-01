
# coding: utf-8

# In[1]:


import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

size = width,height = 600,400

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('First pygame')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    screen.fill(WHITE)
    
    pygame.draw.ellipse(screen,RED, (100,100, 440,100), 1)
    pygame.draw.ellipse(screen,RED, (220,120, 200,200), 1)
    
    pygame.display.flip()
    
    clock.tick(20)

