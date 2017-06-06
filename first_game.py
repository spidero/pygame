#!/usr/bin/python
import sys, pygame, time
pygame.init()

size = width, height = 640, 480
start_poz = [5,5]
fps_start_poz = [5,55]
speed = [1, 1]
left = [-1, 0]
right = [1, 0]
black = 0, 0, 0
white = 255, 255, 255

last_fps = 0
point = 0

c = pygame.time.Clock()
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("comicsansms", 72)
fps_font = pygame.font.SysFont("comicsansms", 14)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

box = pygame.image.load("box.png")
boxrect = box.get_rect()

pygame.display.set_caption ('Gra opis')

ballrect = ballrect.move(width/2,height/2)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    #ballrect = ballrect.move(1,0)

    c.tick()
    if pygame.time.get_ticks() - last_fps > 1000:
   #     print "FPS: ", c.get_fps()
        last_fps = pygame.time.get_ticks()


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
    fps_text = fps_font.render("FPS: "+str(c.get_fps()), True, (0, 128, 0))

    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(box, boxrect)
    screen.blit(text, start_poz)
    screen.blit(fps_text, fps_start_poz)
    pygame.display.flip()

