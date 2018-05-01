
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

turtle = pygame.image.load('turtle.png').convert()
background = pygame.image.load('background.jpg').convert()
position = turtle.get_rect()
position.center = width//2 , height//2

for i in range(position.width):
    for j in range(position.height):
        temp = turtle.get_at((i,j))  #获得单个像素的颜色
        if temp[3] != 0:
            temp[3] = 200
        turtle.set_at((i,j),temp)  #修改透明度

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    screen.blit(background,(0,0))
    screen.blit(turtle, position)
    
    pygame.display.flip()
    
    clock.tick(30)

