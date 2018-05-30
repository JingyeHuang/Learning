
# coding: utf-8

# In[2]:


import pygame
import sys
import traceback
from pygame.locals import *
from random import *

class Ball(pygame.sprite.Sprite):  #pygame.sprite是pygame提供的动画精灵
    def __init__(self, grayball_image, greenball_image, position, speed, bg_size, target):
        pygame.sprite.Sprite.__init__(self)
        
        self.grayball_image = pygame.image.load(grayball_image).convert_alpha()
        #convert_alpha are used to convert surfaces to the same pixel format as used by the screen. This ensures that you won't lose performance because of conversions when you're blitting them to the screen.
        self.greenball_image = pygame.image.load(greenball_image).convert_alpha()
        self.rect = self.grayball_image.get_rect()
        self.rect.left, self.rect.top = position
        self.side = [choice([-1,1]),choice([-1,1])]
        self.speed = speed
        self.collide = False
        self.width, self.height = bg_size[0], bg_size[1]
        self.radius = self.rect.width / 2
        
        self.target = target
        self.control = False   #Ture: Auto , False:player control the ball
        
    def move(self):
        if self.control:
            self.rect = self.rect.move(self.speed)
        else:
            self.rect = self.rect.move((self.side[0]*self.speed[0], self.side[1]*self.speed[1]))
        
        if self.rect.right <= 0:
            self.rect.left = self.width
            
        elif self.rect.left >= self.width:
            self.rect.right = 0
        
        elif self.rect.top >= self.height:
            self.rect.bottom = 0
        
        elif self.rect.bottom <= 0:
            self.rect.top = self.height
            
    def check(self, motion):
        if self.target < motion < self.target + 5 :
            return True
        else:
            return False
        
    
class Glass(pygame.sprite.Sprite):
    def __init__(self, glass_image, bg_size, mouse_image):
        pygame.sprite.Sprite.__init__(self)
        
        self.glass_image = pygame.image.load(glass_image).convert_alpha()
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left, self.glass_rect.top = (bg_size[0]-self.glass_rect.width) // 2 , (bg_size[1]-self.glass_rect.height)
        
        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left, self.mouse_rect.top = self.glass_rect.left, self.glass_rect.top
        pygame.mouse.set_visible(False)

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
    
    grayball_image = 'gray_ball.png'
    bg_image = 'background.png'
    glass_image = 'glass.png'
    mouse_image = 'mouse.png'
    greenball_image = 'green_ball.png'
    
    running = True
    
    bg_size = width, height = 1024, 680
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('Play the Balls')
    
    background = pygame.image.load(bg_image).convert_alpha()
    
    hole = [(117,119,199,201),(225,227,390,392),(503,505,320,322),(698,700,192,194),(906,908,419,421)]
    
    balls = []
    group = pygame.sprite.Group()
    
    glass = Glass(glass_image, bg_size, mouse_image)
    
    for i in range(5):
        position = randint(0, width-100), randint(0, height-100)   #the width of the ball is 100
        speed = [randint(1,10), randint(1,10)]
        ball = Ball(grayball_image,greenball_image, position, speed, bg_size, 5*(i+1))
        while pygame.sprite.spritecollide(ball,group,False,pygame.sprite.collide_circle):  # When the new born ball collide with others
            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)
        balls.append(ball)
        group.add(ball)
    
    motion = 0   #鼠标触发事件次数
    
    MYTIMER = USEREVENT + 1
    pygame.time.set_timer(MYTIMER, 1000) #1000毫秒触发一次check事件
    
    pygame.key.set_repeat(100,100)   #每过100毫秒，重新发送一次key
    
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == GAMEOVER:
                loser_sound.play()
                pygame.time.delay(2000)
                laugh_sound.play()
                pygame.time.delay(2000)
                running = False
            
            elif event.type == MYTIMER:
                if motion:
                    for each in group:
                        if each.check(motion):
                            each.speed = [0,0]    #小球停下来
                            each.control = True
                    motion = 0
            
            elif event.type == MOUSEMOTION:
                motion += 1
                
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    for each in group:
                        if each.control:
                            each.speed[1] -= 1

                if event.key == K_s:
                    for each in group:
                        if each.control:
                            each.speed[1] += 1

                if event.key == K_a:
                    for each in group:
                        if each.control:
                            each.speed[0] -= 1
                            
                if event.key == K_d:
                    for each in group:
                        if each.control:
                            each.speed[0] += 1
                
                if event.key == K_SPACE:
                    for each in group:
                        if each.control:
                            for i in hole:
                                if i[0] <= each.rect.left <= i[1] and i[2] <= each.rect.top <= i[3] :
                                    hole_sound.play()
                                    each.speed = [0,0]
                                    group.remove(each)
                                    temp = balls.pop(balls.index(each))
                                    balls.insert(0,temp)
                                    hole.remove(i)
                                    
                            if not hole:
                                pygame.mixer.music.stop()
                                winner_sound.play()
                                pygame.time.delay(3000)
                                laugh_sound.play()
                                pygame.time.delay(3000)
                                pygame.quit()
                                sys.exit()
                        
                
        screen.blit(background,(0,0))
        screen.blit(glass.glass_image, glass.glass_rect)
        
        glass.mouse_rect.left, glass.mouse_rect.top = pygame.mouse.get_pos()
        if glass.mouse_rect.left < glass.glass_rect.left:
            glass.mouse_rect.left = glass.glass_rect.left
        if glass.mouse_rect.left > glass.glass_rect.right - glass.mouse_rect.width:
            glass.mouse_rect.left = glass.glass_rect.right - glass.mouse_rect.width
        if glass.mouse_rect.top < glass.glass_rect.top:
            glass.mouse_rect.top = glass.glass_rect.top
        if glass.mouse_rect.top > glass.glass_rect.bottom - glass.mouse_rect.height:
            glass.mouse_rect.top = glass.glass_rect.bottom - glass.mouse_rect.height
            
        screen.blit(glass.mouse_image, glass.mouse_rect)
        
        for each in balls:
            each.move()
            if each.collide:
                each.speed = [randint(1,10),randint(1,10)]
                each.collide = False
            if each.control:
                screen.blit(each.greenball_image, each.rect)
            else:
                screen.blit(each.grayball_image, each.rect)
            
        for each in group:   #其中一个球与其他碰撞时
            group.remove(each)
            if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                each.side[0] = -each.side[0]
                each.side[1] = -each.side[1]
                each.collide = True
                if each.control:
                    each.side[0] = -1   #控制的小球碰撞后向反方向移动
                    each.side[1] = -1
                    each.control = False
            
            group.add(each)
            
        pygame.display.flip()
        clock.tick(30)
                
    
if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

