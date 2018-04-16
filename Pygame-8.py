
# coding: utf-8

# In[1]:


import pygame
import sys
from pygame.locals import *

pygame.init()

size = width,height = 600,400
speed = [5,0]
bg = (255,255,255) #RGB

screen = pygame.display.set_mode(size)
pygame.display.set_caption('First pygame')
turtle = pygame.image.load('turtle.png')
position = turtle.get_rect()
turtle_right = pygame.transform.rotate(turtle, 90)
turtle_top = pygame.transform.rotate(turtle, 180)
turtle_left = pygame.transform.rotate(turtle, 270)
turtle_bottom = turtle

left_head = turtle
right_head = turtle = pygame.transform.flip(turtle,True,False) #horizontal = True, vertical = False

turtle = turtle_top

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                turtle = left_head
                speed = [-5,0]
                
            if event.key == K_RIGHT:
                turtle = right_head
                speed = [5,0]
                
            if event.key == K_UP:
                speed = [0,-5]
                
            if event.key == K_DOWN:
                speed = [0,5]
            
    position = position.move(speed)
    
    if position.right > width:
        turtle = turtle_right
        position = turtle_rect = turtle.get_rect()      #重新得到turtle的矩形
        position.left = width - turtle_rect.width       #把position的left赋值到最右边
        speed = [0,5]
    
    if position.bottom > height:
        turtle = turtle_bottom
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        position.top = height - turtle_rect.height
        speed = [-5,0]
    
    if position.left < 0:
        turtle = turtle_left
        position = turtle_rect = turtle.get_rect()
        position.top = height - turtle_rect.height
        speed = [0,-5]
        
    if position.top < 0:
        turtle = turtle_top
        position = turtle_rect = turtle.get_rect()
        speed = [5,0]
        
    screen.fill(bg)
    #refresh image
    screen.blit(turtle, position)
    #refresh screen
    pygame.display.flip()
    #delay
    pygame.time.delay(10)

