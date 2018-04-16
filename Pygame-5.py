
# coding: utf-8

# In[ ]:


import pygame
import sys
from pygame.locals import *

pygame.init()

size = width,height = 600,400
speed = [-2,1]
bg = (255,255,255) #RGB

fullscreen = False

screen = pygame.display.set_mode(size)
pygame.display.set_caption('First pygame')
turtle = pygame.image.load('turtle.png')
position = turtle.get_rect()
print(position)

left_head = turtle
right_head = turtle = pygame.transform.flip(turtle,True,False) #horizontal = True, vertical = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                turtle = left_head
                speed = [-1,0]
                
            if event.key == K_RIGHT:
                turtle = right_head
                speed = [1,0]
                
            if event.key == K_UP:
                speed = [0,-1]
                
            if event.key == K_DOWN:
                speed = [0,1]
                
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    resolution = pygame.display.list_modes() #获得屏幕分辨率
                    screen = pygame.display.set_mode(resolution[0], FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)
            
    position = position.move(speed)
    
    if position.left <0 or position.right> width:
        #revise image 水平翻转图像
        turtle = pygame.transform.flip(turtle,True,False) #horizontal = True, vertical = False
        #revise direction
        speed[0] = -speed[0]
        
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
        
    screen.fill(bg)
    #refresh image
    screen.blit(turtle, position)
    #refresh screen
    pygame.display.flip()
    #delay
    pygame.time.delay(10)

