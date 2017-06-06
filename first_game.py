#!/usr/bin/python
import sys, pygame, time
pygame.init()

size = width, height = 640, 480
start_poz = [5,5]
speed = [1, 1]
left = [-1, 0]
right = [1, 0]
black = 0, 0, 0
white = 255, 255, 255

point = 0

screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("comicsansms", 72)


ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

box = pygame.image.load("box.png")
boxrect = box.get_rect()

pygame.display.set_caption ('Gra opis')

ballrect.move (start_poz)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    #ballrect = ballrect.move(1,0)

    if boxrect.colliderect(ballrect):
        speed[1] = -speed[1]


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        boxrect = boxrect.move(left)

    if pressed[pygame.K_RIGHT]:
       boxrect = boxrect.move(right)


    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    if ballrect.top < 0:
#        speed[1] = -speed[1]
        point += 1

    text = font.render(str(point), True, (0, 128, 0))

    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(box, boxrect)
    screen.blit(text, start_poz)
    pygame.display.flip()

