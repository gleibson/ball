#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys 
from PIL import Image
import pygame
from pygame.locals import*
pygame.init()
print 
size = width, high = 500, 420
speed_ball= [1,1]
speed_racket = [1,1]
gravity = 1
coordinates_ball=[0,0]
coordinates_racket=[175,400]
image_ball = "ball.png"
w_ball, h_ball = (Image.open(image_ball)).size
black = 0,0,0
white = 255,255,255
scenario = pygame.display.set_mode(size)
clock = pygame.time.Clock()
print 

class racket(pygame.sprite.Sprite):
    def __init__(self, x , y):
        pygame.sprite.Sprite.__init__(self)
        self.w_racket = 150
        self.h_racket = 20
        self.image = pygame.Surface([self.w_racket, self.h_racket])
        self.image.fill(white)
        self.rect = self.image.get_rect()

class ball(pygame.sprite.Sprite):
    def __init__(self, image_ball):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_ball)
        self.rect = self.image.get_rect()

print 'definition of classes'

characters = pygame.sprite.Group()

ball_1 = ball(image_ball)
racket_1 = racket(150,20)
characters.add(ball_1)
characters.add(racket_1)

print 'Sprites from the classes'

while 1: 
    print
    print 
    print
    print 'coordinates of the ball: x = ' + str(coordinates_ball[0]) + ', y = ' + str(coordinates_ball[1])
    print 'coordinates of the racket: x = ' + str(coordinates_racket[0]) + ', y = ' + str(coordinates_racket[1])
    print 'speed of the ball: x = ' + str(speed_ball[0]) + ', y = ' + str(speed_ball[1]) 
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print 'Windows was closed'
            sys.exit()

    if coordinates_ball[1] > high - h_ball:
        print 'I avoided the ball to be under limit of screen'
        coordinates_ball[1] = high - h_ball
  
    coordinates_ball[0] = coordinates_ball[0] + speed_ball[0]
    coordinates_ball[1] = coordinates_ball[1] + speed_ball[1]

    if coordinates_ball[0] > width - w_ball or coordinates_ball [0] < 0:
        print 'The ball changed of the direction in X'
        speed_ball[0] = -speed_ball[0]
    if coordinates_ball[1] > high - h_ball or coordinates_ball[1] < 0 :
        print 'The ball changed of the direction in y'
        speed_ball[1] = -speed_ball[1]
    if speed_ball[1] >= 0:
        print 'Ball is going down'
        speed_ball[1] = speed_ball[1] + gravity
    else:
        print 'The ball is going up'
        speed_ball[1] = speed_ball[1] + 1.1*gravity


    key = pygame.key.get_pressed()

    if (key[K_LEFT]):
        print 'Arrow of left pressed'
        coordinates_racket[0] = coordinates_racket[0] - speed_racket[0]
    elif (key[K_RIGHT]):
        print 'Arrow of right pressed'
        coordinates_racket[0] = coordinates_racket[0] + speed_racket[0]

    print 'coordinates of sprites'
    ball_1.rect.x = coordinates_ball[0]
    ball_1.rect.y = coordinates_ball[1]
    racket_1.rect.x = coordinates_racket[0]
    racket_1.rect.y = coordinates_racket[1]
      
#colision 
    print 'coordinates_ball[1] : ' + str(coordinates_ball[1])
    if pygame.sprite.collide_rect(ball_1, racket_1) == True:
        print 'Detected one colision between ball and racket'
        pygame.mixer.Sound('/usr/lib/libreoffice/share/gallery/sounds/apert.wav').play()
        print 'Sound'
#
        if coordinates_ball[1] > racket_1.rect.top:
           coordinates_ball[1] = racket_1.rect.top
           print 'Coordinate Y of the ball: ' + str(coordinates_ball[1]) + ' high: ' + str(high) + ' Top of the racket : ' + str(racket_1.rect.top) 
           print 'X'
        else: 
           speed_ball[1] = -speed_ball[1] - 1.1*gravity
           print 'y'

      
    key = pygame.key.get_pressed()
    scenario.fill(black)
    characters.draw(scenario)
    pygame.display.flip()
    print
    clock.tick(60)
