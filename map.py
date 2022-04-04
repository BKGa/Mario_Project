from vector import Vector
from settings import Settings
from brick import Brick

class Map():
    def __init__(self, screen, settings, bricks, pipes, mario, enemies, ground, upgrades, stats, secret_bricks):
        self.level = 'images/level_loc.txt'
        self.secret_level = 'images/Underground_level.txt'
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.bricks = bricks
        self.secret_bricks = secret_bricks
        self.pipes = pipes
        self.mario = mario
        self.upgrades = upgrades
        self.enemies = enemies
        self.ground = ground



    def set_map(self): # Unsure how to read each letter accurately from a text file in a row/column format
        for y in range(0, self.level.size[1]):
            for x in range(0, self.level.size[0]):
                letter = self.level((x, y))

                if letter == 'B':
                    Map.create_brick(self, x * 40, y * 40, 0)
                if letter == 'G':
                    Map.create_enemy(self, x*40, y*40, 0)
                if letter == 'K':
                    Map.create_enemy(self, x*40, y*40, 0)
                if letter == 'R':
                    Map.create_brick(self, x*40, y*40, 0)
                if letter == 'M':
                    Map.create_brick(self, x*40, y*40, 0)
                if letter == 'I':
                    Map.create_brick(self, x*40, y*40, 0)
                if letter == 'S':
                    Map.create_brick(self, x*40, y*40, 0)
                if letter == 'A':
                    Map.create_secret_brick(self, x*40, y*40, 0)
                if letter == 'C':
                    Map.create_coin(self, x*40, y*40, 0)
                if letter == 'N':
                    Map.create_secret_brick(self, x*40, y*40, 0)
                if letter == '?':
                    Map.create_brick(self, x*40, y*40, 0)
                if letter == 'L':
                    Map.create_brick(self, x*40, y*40, 0)
                if letter == 'X':
                    Map.create_brick(self, x*40, y*40, 4)

    def create_brick(self, x, y, num):
        self.brick = Brick(self.screen, self.settings, num)
        self.brick.rect.x = x
        self.brick.rect.y = y
        self.bricks.add(self.brick)
        if num == 4:
            self.ground.add(self.brick)

