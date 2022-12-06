import pygame
from settings import *
from snake import Player
import math
import random
from map import world_map
from drawing import Drawing

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)

# Цикл игры
sin_a = 0
cos_a = 0
time = 0
score = 0
length = 4
blocks_x = [player.x, ]
blocks_y = [player.y, ]
x = random.randint(0, WIDTH)
y = random.randint(0, HEIGHT)
is_in = False
is_pause = False
game_over = False
running = True
while running:
    if is_in and not game_over and not is_pause:
        blocks_x[0] = player.x
        blocks_y[0] = player.y
        # Держим цикл на правильной скорости
        time += 1
        clock.tick(FPS)
        # Ввод процесса (события)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        # pressing the buttons
        keys = pygame.key.get_pressed()

        if sin_a == 0 and cos_a == 0:
            if keys[pygame.K_w]:
                sin_a = 1
                cos_a = 0
            if keys[pygame.K_s]:
                sin_a = -1
                cos_a = 0
            if keys[pygame.K_a]:
                sin_a = 0
                cos_a = 1
            if keys[pygame.K_d]:
                sin_a = 0
                cos_a = -1
        if sin_a == 1 and cos_a == 0:
            if keys[pygame.K_a]:
                sin_a = 0
                cos_a = 1
            if keys[pygame.K_d]:
                sin_a = 0
                cos_a = -1
        if sin_a == -1 and cos_a == 0:
            if keys[pygame.K_a]:
                sin_a = 0
                cos_a = 1
            if keys[pygame.K_d]:
                sin_a = 0
                cos_a = -1
        if sin_a == 0 and cos_a ==1:
            if keys[pygame.K_w]:
                sin_a = 1
                cos_a = 0
            if keys[pygame.K_s]:
                sin_a = -1
                cos_a = 0
        if sin_a == 0 and cos_a == -1:
            if keys[pygame.K_s]:
                sin_a = -1
                cos_a = 0
            if keys[pygame.K_w]:
                sin_a = 1
                cos_a = 0
        if keys[pygame.K_ESCAPE]:
            is_pause = True

        player.movement(sin_a, cos_a)

        if player.is_in():
            game_over = True

        if player.dead(blocks_x, blocks_y):
            game_over = True


        sc.fill(DARKGREEN)

        print(score, blocks_x, blocks_y)

        drawing.mini_map(blocks_x, blocks_y)
        drawing.add_blocks(blocks_x, blocks_y, score, length)
        if player.bonus(time):
            drawing.bonus(x, y)

        if player.is_in_bonus(x, y):
            time = 0
            score += 1
            for i in range(7):
                blocks_x.append(player.x)
                blocks_y.append(player.y)
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)

        if score > 0:
            for i in range(score*7-1, -1, -1):
                blocks_x[i+1] = blocks_x[i]
                blocks_y[i+1] = blocks_y[i]

        drawing.fps(clock)
        drawing.score(score)

        pygame.display.flip()

    if not is_in:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        sc.fill(SKYBLUE)
        drawing.main()

        is_in = player.in_game()
        pygame.display.flip()

    if game_over:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        sc.fill(SKYBLUE)
        drawing.game_over()
        drawing.game_over1()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_SPACE]:
            game_over = False
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            blocks_x = [0]
            blocks_y = [0]
            player.x = HALF_WIDTH
            player.y = HALF_HEIGHT
            score = 0
            length = 4
            time = 0
        pygame.display.flip()

    if is_pause:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        sc.fill(SKYBLUE)
        drawing.pause()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            is_pause = False
        pygame.display.flip()
pygame.quit()