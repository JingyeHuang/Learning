
# coding: utf-8

# In[1]:


import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 800, 600
speed = [0,0]
fullscreen = False

screen = pygame.display.set_mode(size) 
pygame.display.set_caption('Jgame')
pika = pygame.image.load('pika.jpg')
position = pika.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                if position.left > 0:
                    speed = [-10,0]
                else:
                    speed = [0,0]
                
            if event.key == K_RIGHT:
                if position.right < width:
                    speed = [10,0]
                else:
                    speed = [0,0]
                
            if event.key == K_UP:
                if position.top >0:
                    speed = [0,-10]
                else:
                    speed = [0,0]
                
            if event.key == K_DOWN:
                if position.bottom < height:
                    speed = [0,10]
                else:
                    speed = [0,0]
                
        if event.type == pygame.KEYUP:
            speed = [0,0]
        
    position = position.move(speed)
                
    screen.fill([255,255,255])
    #refresh image
    screen.blit(pika, position)
    #refresh screen
    pygame.display.flip()
    #delay
    pygame.time.delay(10)

