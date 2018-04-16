
# coding: utf-8

# In[1]:


import pygame
import sys
from pygame.locals import *

pygame.init()

size = width,height = 600,400
speed = [-2,1]
bg = (255,255,255) #RGB

fullscreen = False

screen = pygame.display.set_mode(size, RESIZABLE)
pygame.display.set_caption('First pygame')
# LOAD IMAGE
oturtle = pygame.image.load('turtle.png')
turtle = oturtle
# Retreive image rect
oturtle_rect = oturtle.get_rect()
position = turtle_rect = oturtle_rect
print(position)

#设置放大缩小比率
ratio = 1.0

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
                    width, height = resolution[0][0], resolution[0][1]
                else:
                    screen = pygame.display.set_mode(size)
            
            #放大缩小surface
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                #最大放大一倍，最小缩小50%
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio >0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0
                    
                turtle = pygame.transform.smoothscale(oturtle, (int(oturtle_rect.width *ratio), int(oturtle_rect.height *ratio))  )
                    
        #用户调整窗口尺寸
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            screen = pygame.display.set_mode(size, RESIZABLE)
            
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

