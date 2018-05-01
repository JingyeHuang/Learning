
# coding: utf-8

# In[1]:


import pygame
import sys
from pygame.locals import *

pygame.init()

size = width,height = 600,400
bg = (0,0,0) #RGB

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('First pygame')

turtle = pygame.image.load('turtle.jpg').convert()
background = pygame.image.load('background.jpg').convert()
position = turtle.get_rect()
position.center = width//2 , height//2

turtle.set_colorkey((255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    screen.blit(background,(0,0))
    screen.blit(turtle, position)
    
    pygame.display.flip()
    
    clock.tick(30)

