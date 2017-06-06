#!/usr/bin/python
import sys, pygame, time
pygame.init()

size = width, height = 640, 480
speed = [1, 1]
left = [-1, 0]
right = [1, 0]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

box = pygame.image.load("box.png")
boxrect = box.get_rect()

pygame.display.set_caption ('Gra opis dlugi', 'Gra opis krotki')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    #ballrect = ballrect.move(1,0)


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        boxrect = boxrect.move(left)

    if pressed[pygame.K_RIGHT]:
       boxrect = boxrect.move(right)

    if pressed[pygame.K_UP]:
        speed[0] = -speed[0]
        time.sleep(0.1)
    if pressed[pygame.K_DOWN]:
        speed[0] = -speed[0]
        time.sleep(0.1)
      
    if pygame.key.get_focused():
        press=pygame.key.get_pressed()
       # print "cos sie dzieje"


    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(box, boxrect)
    pygame.display.flip()

