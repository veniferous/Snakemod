import pygame
from pygame import *
from sprites import Snake
from sprites import Apple
import random

pygame.init()

DEFAULT_SCREEN_SIZE = [740, 580]
INITIAL_DIRECTION = Snake.SnakeMove.RIGHT
DEFAULT_UPDATE_SPEED = 150

updatetime = pygame.time.get_ticks() + DEFAULT_UPDATE_SPEED

screen = pygame.display.set_mode(DEFAULT_SCREEN_SIZE)
display.set_caption("Tyler's Snake lel")

snake = Snake(None, None, None)
apple = None

def render_snake():
    screen.blit(snake.head.image, snake.head.rect)
    for count in range(len(snake.tail.tiles)):
        screen.blit(snake.tail.tiles[count]['image']
            , snake.tail.tiles[count]['rect'])

def create_apple():
    global apple
    global snake

    hlimit = (DEFAULT_SCREEN_SIZE[0]/Apple._DEFAULT_SIZE[0])-1
    vlimit = (DEFAULT_SCREEN_SIZE[1]/Apple._DEFAULT_SIZE[1])-1
    X, Y = None, None

    while snake.occupies_position([X, Y]) == True:
        X = random.randint(0, hlimit)*Apple._DEFAULT_SIZE[0]
        Y = random.randint(0, vlimit)*Apple._DEFAULT_SIZE[1]
    apple = Apple(None, None, [X, Y])

def render_apple():
    global apple
    screen.blit(apple.image, apple.rect)

is_done = False
is_over = False
direction = None
score = 0
create_apple()

while is_done == False:
    screen.fill(0)
    global direction
    if direction == None:
        direction = INITIAL_DIRECTION

    for e in event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                is_done = True
            elif e.key == K_UP:
                if direction != Snake.SnakeMove.DOWN:
                    direction = Snake.SnakeMove.UP
            elif e.key == K_DOWN:
                if direction != Snake.SnakeMove.UP:
                    direction = Snake.SnakeMove.DOWN
            elif e.key == K_RIGHT:
                if direction != Snake.SnakeMove.LEFT:
                    direction = Snake.SnakeMove.RIGHT
            elif e.key == K_LEFT:
                if direction != Snake.SnakeMove.RIGHT:
                    direction = Snake.SnakeMove.LEFT

    currenttime = pygame.time.get_ticks()
    global updatetime
    global is_over
    if is_over == False:
        if currenttime >= updatetime:
            moved = snake.move(direction, DEFAULT_SCREEN_SIZE[0], DEFAULT_SCREEN_SIZE[1])
            if moved == False:
                is_over = True
            if snake.occupies_position(apple.rect.topleft) == True:
                create_apple()
                snake.lengthen_tail(1, direction)
                global score
                score += 1
                display.set_caption('Snake: ' + str(score))

            render_apple()
            render_snake()
            pygame.display.update()
            updatetime += DEFAULT_UPDATE_SPEED
    else:
        display.set_caption('Snake: ' + str(score) + ' GAME OVER')
