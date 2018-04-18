
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
pika = pygame.image.load('pika.png')
bg = pygame.image.load('bg.jpg')
position = pika.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                speed[0] = -10
                
            if event.key == K_RIGHT:
                speed[0] = 10
                
            if event.key == K_UP:
                speed[1] = -10
                
            if event.key == K_DOWN:
                speed[1] = 10
                
        if event.type == pygame.KEYUP:
            speed = [0,0]
    
    if (position.left < 0 and speed[0] < 0) or (position.right > width and speed[0] > 0):
        speed[0] = 0
    if (position.top < 0 and speed[1] < 0) or (position.bottom > height and speed[1] > 0):
        speed[1] = 0
    
    position = position.move(speed)
                
    screen.fill([255,255,255])
    #refresh image
    screen.blit(bg, (0,0))
    screen.blit(pika, position)
    #refresh screen
    pygame.display.flip()
    #delay
    pygame.time.delay(10)

