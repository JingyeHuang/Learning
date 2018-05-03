
# coding: utf-8

# In[1]:


import pygame
import sys
from pygame.locals import *
from random import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image).convert_alpha()
        #convert_alpha are used to convert surfaces to the same pixel format as used by the screen. This ensures that you won't lose performance because of conversions when you're blitting them to the screen.
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
        if self.rect.right < 0:
            self.rect.left = self.width
            
        elif self.rect.left > self.width:
            self.rect.right = 0
        
        elif self.rect.top > self.height:
            self.rect.bottom = 0
        
        elif self.rect.bottom < 0:
            self.rect.top = self.height
        
def main():
    pygame.init()
    
    ball_image = 'gray_ball.png'
    bg_image = 'background.png'
    
    running = True
    
    bg_size = width, height = 1024, 680
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('Play the Balls')
    
    background = pygame.image.load(bg_image).convert_alpha()
    
    balls = []
    
    for i in range(5):
        position = randint(0, width-100), randint(0, height-100)   #the width of the ball is 100
        speed = [randint(-10,10), randint(-10,10)]
        ball = Ball(ball_image, position, speed, bg_size)
        balls.append(ball)
    
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                
        screen.blit(background,(0,0))
        
        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)
            
        pygame.display.flip()
        clock.tick(30)
                
    
if __name__ == '__main__':
    main()

