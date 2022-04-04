import pygame as pg
from pygame.sprite import Sprite
from fireball import Fireball
from map import Map

class Mario(Sprite):
    def __init__(self, screen, settings, pipes, bricks, stats, enemies, poles, fireballs, secret_bricks, ground, secret_pipes):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.pipes = pipes
        self.bricks = bricks
        self.stats = stats
        self.enemies = enemies
        self.pole = poles
        self.fireballs = fireballs
        self.secret_bricks = secret_bricks
        self.ground = ground
        self.secret_pipe = secret_pipes

