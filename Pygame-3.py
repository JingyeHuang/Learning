
# coding: utf-8

# In[ ]:


import pygame
import sys

pygame.init()

size = width,height = 600,400
bg = (0,0,0) #RGB
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pygame')
font = pygame.font.Font(None, 20)  #字体=None,大小=20

screen.fill(bg)

position = 0
line_height = font.get_linesize()  #得到行高

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        screen.blit(font.render(str(event), True, (0,255,0)), (0,position))   #第二个参数True是表示是否消除锯齿
        position += line_height
        
        if position > height:
            position = 0
            screen.fill(bg)
            
    pygame.display.flip()

