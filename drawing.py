import pygame
from settings import *
from map import map


class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.font1 = pygame.font.SysFont('Arial', 56, bold=True)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, blocks_x, blocks_y):
        self.sc_map.fill(DARKGREEN)
        pygame.draw.circle(self.sc_map, RED, (int(blocks_x[0]), int(blocks_y[0])), 5)
        self.sc.blit(self.sc_map, MAP_POS)

    def bonus(self, x, y):
        pygame.draw.circle(self.sc_map, WHITE, (int(x), int(y)), 5)
        self.sc.blit(self.sc_map, MAP_POS)

    def score(self, score):
        score = str(score)
        render = self.font1.render(score, 0, WHITE)
        self.sc.blit(render, BONUS_POS)

    def add_blocks(self, blocks_x, blocks_y, score, length):
        if score > 0:
            for i in range(1, score*7):
                pygame.draw.circle(self.sc_map, RED, (int(blocks_x[i]), int(blocks_y[i])), 5)
        self.sc.blit(self.sc_map, MAP_POS)

    def main(self):
        self.sc_map.fill(SKYBLUE)
        main_text = str('Press Space to play:')
        render = self.font.render(main_text, 0, WHITE)
        self.sc.blit(render, MAIN_POS)

    def game_over(self):
        self.sc_map.fill(SKYBLUE)
        main_text = str("Game over!")
        render = self.font.render(main_text, 0, WHITE)
        self.sc.blit(render, GAMEOVER_POS)

    def game_over1(self):
        main_text1 = str('Press ESC to exit, SPACE to play again:')
        render = self.font.render(main_text1, 0, WHITE)
        self.sc.blit(render, GAMEOVER_POS1)

    def pause(self):
        self.sc_map.fill(SKYBLUE)
        pause_text = str('PAUSE')
        render = self.font1.render(pause_text, 0, WHITE)
        self.sc.blit(render, PAUSE_POS)