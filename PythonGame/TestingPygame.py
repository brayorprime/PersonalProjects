from re import I
import pygame
from pygame.locals import *
import sys

pygame.init()

size = width, height = 1100,1100
speed = [10, 15]
black = 250,250,250
screen = pygame.display.set_mode(size)

background = pygame.image.load("PythonGame\Sprites\\background.png")
ball = pygame.image.load("PythonGame\Sprites\lilclari.png")

position = ball.get_rect()

bgrect = background.get_rect()

screen.blit(background, (0,0))
pygame.display.update()

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0

def exitGame():
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

while True:
    screen.blit(background, position, position)

    for event in pygame.event.get():
        if event.type in (KEYDOWN):
            position = position.move(speed)
	# position = position.move(speed)
    if position.left < 0 or position.right > bgrect.right: 
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > bgrect.bottom:
	    speed[1] = -speed[1]

    screen.blit(ball,position)
    pygame.display.update()
    pygame.display.flip()
    pygame.time.delay(10)



# o = GameObject(player, x*40, x*10)

# while True:
	
# 	screen.blit(background, o.pos, o.pos)

# 	o.move()
# 	screen.blit(o.image, o.pos)

# 	pygame.display.update()

# 	pygame.time.delay(100)