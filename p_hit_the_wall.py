#coding:utf-8


import pygame
import sys

from pygame.locals import *

#初始化Pygame
pygame.init()

size = width, height = 1000 , 800

x_speed = -2
y_speed = 1
speed = [x_speed,y_speed]
bg = (255, 255, 255)

fullscreen = False

#设置帧率
clock = pygame.time.Clock()


#创建指定大小的窗口 surface
screen = pygame.display.set_mode(size)

#设置窗口标题
pygame.display.set_caption('LLl会撞墙')

#加载图片
ratio = 1
pig_0 = pygame.image.load('pig.jpg')

pig = pig_0

pig_peng_0 = pygame.image.load('peng.png')

pig_peng = pig_peng_0



#获得图像的位置矩形
position_0 = pig_0.get_rect()
position = pig.get_rect()

position_peng = pig_peng.get_rect()

#设置左右翻转图像
r_head = pygame.transform.flip(pig, True, False )
l_head = pig

r_head_peng = pygame.transform.flip(pig_peng, True, False )
l_head_peng = pig_peng


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                #when press LEFT or RIGHT ,pig change to origin picture.
                pig = l_head
                pig_peng = l_head_peng 

                pig_0 = l_head
                pig_peng_0 = l_head_peng 
                
                speed = [-1, 0]    #为啥加速度不行？？？
                #x_speed += -1
                #speed = [x_speed,y_speed]
            if event.key == K_RIGHT:
                pig = r_head
                pig_peng = r_head_peng

                pig_0 = r_head
                pig_peng_0 = r_head_peng
                
                speed = [1, 0]
                #x_speed += 1
                #speed = [x_speed,y_speed]
            if event.key == K_UP:
                speed = [0, -1]
                #y_speed += -1
                #speed = [x_speed,y_speed]
            if event.key == K_DOWN:
                speed = [0, 1]
                #y_speed += 1
                #speed = [x_speed,y_speed]

            #全屏 F11
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    #创建全屏大小的窗口 surface
                    screen = pygame.display.set_mode((1920,1080), FULLSCREEN | HWSURFACE)
                    width = 1920
                    height = 1080
                else:
                    #创建指定大小的窗口 surface
                    size = width, height = 1000 , 800
                    screen = pygame.display.set_mode(size)

                

            #放大缩小、恢复
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                    print (str(ratio) + '\n')
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                    print (str(ratio) + '\n')
                if event.key == K_SPACE :
                    ratio = 1.0

                if speed[0] > 0:
                    pig_0 = r_head
                    pig_peng_0 = r_head_peng

                if speed[0] < 0:
                    pig_0 = l_head
                    pig_peng_0 = l_head_peng
                    
                    


                pig = pygame.transform.smoothscale(pig_0, (int(position_0.width * ratio), int(position_0.height * ratio)))
                pig_peng = pygame.transform.smoothscale(pig_peng_0, (int(position_0.width * ratio), int(position_0.height * ratio)))



                position.width, position.height = pig.get_rect().width, pig.get_rect().height    

    #move the image
               
    position = position.move(speed)


    if position.left < 0 or position.right > width:
        #翻转图像
        print position


        #更新图像
        screen.blit(pig, position)
        screen.blit(pig_peng, position)

        #更新界面
        pygame.display.flip()
        #延迟10毫秒
        pygame.time.delay(300)

        pig = pygame.transform.flip(pig, True, False )
        pig_peng = pygame.transform.flip(pig_peng, True, False )
        

        #反向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom >height:
        speed[1] = -speed[1]

        #更新图像
        screen.blit(pig, position)
        screen.blit(pig_peng, position)

        #更新界面
        pygame.display.flip()
        #延迟10毫秒
        pygame.time.delay(300)


        


    #填充背景
    screen.fill(bg)

    #更新图像
    screen.blit(pig, position)
    '''screen.blit(pig_peng, position_peng)'''
    #更新界面
    pygame.display.flip()
    #延迟10毫秒
    '''pygame.time.delay(10)'''
    clock.tick(100)
