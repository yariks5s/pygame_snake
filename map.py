from settings import *

text_map = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'W............................W',
    'W............................W',
    'W............................W',
    'W............................W',
    'W............................W',
    'W............................W',
    'W............................W',
    'W............................W',
    'W............................W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
]

world_map = set()
map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
            map.add((i * MAP_TILE, j * MAP_TILE))