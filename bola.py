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

racket = pygame.image.load("raquete.png")
racketrect = racket.get_rect()
racketrect.center = (400, 300)


while 1:
   if ballrect.bottom > heigth:
       ballrect.bottom = heigth
   if ballrect.right > width:
       ballrect.right = width
   ballrect = ballrect.move(speed)
   if ballrect.bottom >= racketrect.top and ballrect.right >= racketrect.left and ballrect.left <= racketrect.right:
      speed[1] = -speed[1]
      speed[1] = speed[1] - 1.5*gravity
      raw_input("Press Enter to continue...")
   
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
   
   scenario.fill(black)
   scenario.blit(ball, ballrect)
   scenario.blit(racket, racketrect)
   pygame.display.flip()
   sleep(0.02)
#        raw_input("Press Enter to continue...")
