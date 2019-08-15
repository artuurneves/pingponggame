import pygame, random, time
from pygame.locals import *

def move_ball():
    pass

pygame.init()
int = 0

game_over = False
points = 0
clock = pygame.time.Clock()
RIGHT = 1
LEFT = 3
START = 0


my_direction = START

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pong Ping')

raquete = [(300, 350), (310, 350), (320, 350), (330, 350), (340, 350)]
raquete_skin = pygame.Surface((10, 10))
raquete_skin.fill((255,255,255))

ball = pygame.Surface((10, 10))
ball.fill((255,255,255))
ball_pos_init = (random.randint(0, 399), 0)

clock = pygame.time.Clock()

while True:
    # clock.tick(1)

    screen.fill((0, 0, 0))
    screen.blit(ball, ball_pos_init)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT

    if my_direction != START:

        if my_direction == LEFT:
            raquete[0] = (raquete[0][0] - 10, raquete[0][1])

            for i in range(1, len(raquete)):
                raquete[i] = (raquete[i][0] - 10, raquete[i][1])

        if my_direction == RIGHT:
            raquete[0] = (raquete[0][0] + 10, raquete[0][1])

            for i in range(1,len(raquete)):
                raquete[i] = (raquete[i - 1][0] + 10, raquete[i][1])

    for pos in raquete:
        screen.blit(raquete_skin, pos)

    my_direction = START

    pygame.display.update()
    if game_over:
        break