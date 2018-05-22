
# coding: utf-8

# In[1]:


import pygame
import sys
from pygame.locals import *
from random import *

class Ball(pygame.sprite.Sprite):  #pygame.sprite是pygame提供的动画精灵
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image).convert_alpha()
        #convert_alpha are used to convert surfaces to the same pixel format as used by the screen. This ensures that you won't lose performance because of conversions when you're blitting them to the screen.
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]
        self.radius = self.rect.width / 2
        
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
    
    #Background music
    pygame.mixer.init()
    
    pygame.mixer.music.load('bg_music.ogg')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    
    loser_sound = pygame.mixer.Sound('loser.wav')
    laugh_sound = pygame.mixer.Sound('laugh.wav')
    winner_sound = pygame.mixer.Sound('winner.wav')
    hole_sound = pygame.mixer.Sound('hole.wav')
    
    #音乐结束，游戏结束
    GAMEOVER = USEREVENT
    pygame.mixer.music.set_endevent(GAMEOVER)
    
    ball_image = 'gray_ball.png'
    bg_image = 'background.png'
    
    running = True
    
    bg_size = width, height = 1024, 680
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('Play the Balls')
    
    background = pygame.image.load(bg_image).convert_alpha()
    
    balls = []
    group = pygame.sprite.Group()
    
    for i in range(5):
        position = randint(0, width-100), randint(0, height-100)   #the width of the ball is 100
        speed = [randint(-10,10), randint(-10,10)]
        ball = Ball(ball_image, position, speed, bg_size)
        while pygame.sprite.spritecollide(ball,group,False,pygame.sprite.collide_circle):  # When the new born ball collide with others
            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)
        balls.append(ball)
        group.add(ball)
    
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == GAMEOVER:
                loser_sound.play()
                pygame.time.delay(2000)
                laugh_sound.play()
                pygame.time.delay(2000)
                running = False
                
        screen.blit(background,(0,0))
        
        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)
            
        for each in group:   #其中一个球与其他碰撞时
            group.remove(each)
            if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
            group.add(each)
            
        pygame.display.flip()
        clock.tick(30)
                
    
if __name__ == '__main__':
    main()

