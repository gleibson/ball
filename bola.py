#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import pygame
pygame.init()

screen = width, heigth = 800, 600
speed = [1,1]
gravity = 1
black = 0,0,0
scenario = pygame.display.set_mode(screen)

ball = pygame.image.load("bola.png")
ballrect = ball.get_rect()

while 1:
   if ballrect.bottom > heigth:
       ballrect.bottom = heigth
   if ballrect.right > width:
       ballrect.right = width
   ballrect = ballrect.move(speed)
   if ballrect.right < 0 or ballrect.left > width:
       speed[0] = -speed[0]
   if ballrect.top < 0 or ballrect.bottom > heigth:
       speed[1] = -speed[1]
   if speed[1] >= 0:
       speed[1] = speed[1] + gravity
   else: 
       speed[1] = speed[1] + 1.1*gravity
   speed[1] = speed[1] + gravity
   print 'speed[1]: ' + str(speed[1]) + ' ballrect.bottom: ' + str(ballrect.bottom)
   scenario.fill(black)
   scenario.blit(ball, ballrect)
   pygame.display.flip()
   sleep(0.02)
