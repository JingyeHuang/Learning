
# coding: utf-8

# In[2]:


import pygame
import sys

pygame.init()

size = width,height = 600,400
speed = [-2,1]
bg = (255,255,255) #RGB

screen = pygame.display.set_mode(size)
pygame.display.set_caption('First pygame')
turtle = pygame.image.load('turtle.png')
position = turtle.get_rect()
print(position)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
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

