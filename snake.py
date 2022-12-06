from settings import *
import pygame
import drawing
import random

sin_a = 1
cos_a = 0

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self, sin_a, cos_a):
        player_speed = -2


        self.x += player_speed * cos_a
        self.y += player_speed * sin_a
    def is_in(self):
        if self.x == 0 or self.y == 0 or self.y == HEIGHT or self.x == WIDTH:
            return True
        else:
            return False

    def bonus(self, time):
        if time > 240:
            return True

    def is_in_bonus(self, pos_x, pos_y):
        if pos_x - 5 < self.x < pos_x + 5 and pos_y - 5 < self.y < pos_y + 5:
            return True

    def in_game(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        else:
            return False

    def dead(self, blocks_x, blocks_y):
        for i in range(1, len(blocks_x)):
            if self.x == blocks_x[i] and self.y == blocks_y[i]:
                return True
