
# coding: utf-8

# In[1]:


import pygame
import sys

pygame.init()

size = width,height = 600,400
bg = (255,255,255) #RGB

screen = pygame.display.set_mode(size)
pygame.display.set_caption('First pygame')
oturtle = pygame.image.load('turtle.png')
turtle = pygame.transform.chop(oturtle, (207,200,50,50))

# 0 -> 未选择， 1 -> 选择中， 2 -> 完成选择
select = 0
select_rect = pygame.Rect(0,0,0,0)

# 0 -> 未拖拽， 1 -> 拖拽中， 2 -> 完成拖拽
drag = 0

position = turtle.get_rect()
position.center = width//2, height//2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #第一次点击，选择范围:
                if select == 0 and drag == 0:
                    pos_start = event.pos
                    select = 1
                    
                #第二次点击，拖拽图像
                if select == 2 and drag == 0:
                    capture = screen.subsurface(select_rect).copy() #获得矩形区域的子对象
                    cap_rect = capture.get_rect()
                    drag = 1
                    
                #第三次点击，初始化
                if select == 2 and drag == 2:
                    select = 0
                    drag = 0         
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                 #第一次释放，选择结束
                if select == 1 and drag == 0:
                    pos_stop = event.pos
                    select = 2
                    
                #第二次释放，选择拖拽
                if select == 2 and drag == 1:
                    drag = 2
                    
        
    screen.fill(bg)
    #refresh image
    screen.blit(turtle, position)
    #refresh screen
    
    #实时绘制选择框
    if select:
        mouse_pos = pygame.mouse.get_pos()
        if select == 1:
            pos_stop = mouse_pos
        select_rect.left, select_rect.top = pos_start
        select_rect.width, select_rect.height = pos_stop[0] - pos_start[0], pos_stop[1] - pos_start[1]
        pygame.draw.rect(screen, (0,0,0), select_rect, 1)  #画在screen上，用黑色(0,0,0)，矩形为select_rect，线粗为1个像素
        
    #拖拽裁剪的图像
    if drag:
        if drag == 1:
            cap_rect.center = mouse_pos  #矩形随着鼠标移动
        screen.blit(capture, cap_rect)
    
    pygame.display.flip()
    #delay
    pygame.time.delay(10)

