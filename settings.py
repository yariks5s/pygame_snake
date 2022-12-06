import math

# game settings
WIDTH = 1280
HEIGHT = 720
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 36
BONUS_POS = (0, 0)
FPS_POS = (WIDTH-40, 0)
MAIN_POS = (HALF_WIDTH - 170, HALF_HEIGHT)
GAMEOVER_POS = (HALF_WIDTH - 110, HALF_HEIGHT - 50)
GAMEOVER_POS1 = (HALF_WIDTH - 325, HALF_HEIGHT)
PAUSE_POS = (HALF_WIDTH - 110, HALF_HEIGHT - 25)

# minimap settings
MAP_SCALE = 1
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, 0)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)
DARKGREEN = (22, 66, 26)

# player settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2