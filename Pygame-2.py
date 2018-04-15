
# coding: utf-8

# In[ ]:


import pygame
import sys

pygame.init()

size = width,height = 600,400
bg = (255,255,255) #RGB

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pygame')

f = open('pygame record.txt','w')

while True:
    for event in pygame.event.get():
        f.write(str(event) + '\n')
        
        if event.type == pygame.QUIT:
            f.close()
            sys.exit()

