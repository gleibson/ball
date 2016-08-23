#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from time import sleep
import pygame
from pygame.locals import *
pygame.init()

screen = width, heigth = 800, 600
speed = [1,1]
gravity = 1
black = 0,0,0
scenario = pygame.display.set_mode(screen)
racket_center = [400,300]

ball = pygame.image.load("bola.png")
ballrect = ball.get_rect()

racket = pygame.image.load("raquete.png")
racketrect = racket.get_rect()
racketrect.center = (400, 300)

while 1:
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
   if ballrect.bottom > heigth:
       ballrect.bottom = heigth
   ballrect = ballrect.move(speed)
   if ballrect.bottom >= racketrect.top and ballrect.right >= racketrect.left and ballrect.left <= racketrect.right:
      speed[1] = -speed[1]
      speed[1] = speed[1] - 1.5 * gravity
#      raw_input("Press Enter to continue...")
   else:
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > heigth:
            speed[1] = -speed[1]
        
        if speed[1] >= 0:
            speed[1] = speed[1] + gravity
        else: 
            speed[1] = speed[1] + 1.1*gravity
   speed[1] = speed[1] + gravity
#   print 'ballrect.left' = + str(ballrect.left) + ' |ballrect.right = ' + str(ballrect.right) + '|ballrect.bottom = ' + str(ballrect.bottom)
#   print 'racketrect.left' = + str(racketrect.left) + '|racketrect.right = ' + str(racketrect.right) + '|racketrect.top = ' + str(racketrect.top)
   buton = pygame.key.get_pressed()
   if (buton[K_LEFT]):
      racket_center[0] = racket_center[0] - 1
   elif (buton[K_RIGHT]):
      racket_center[0] = racket_center[0] + 1
   racketrect.center = (racket_center[0], racket_center[1])
   scenario.fill(black)
   scenario.blit(ball, ballrect)
   scenario.blit(racket, racketrect)
   pygame.display.flip()
   sleep(0.02)
#        raw_input("Press Enter to continue...")
