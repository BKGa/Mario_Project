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

        self.small_mario = []
        self.small_star_mario = []
        self.shroom_mario = []
        self.flower_mario = []
        self.star_mario = []

        self.image = self.small_mario[0]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.x_change = 0
        self.y_change = 0

        self.moving_left = False
        self.moving_right = False
        self.jump = False
        self.facing_right = True
        self.crouch = False
        self.dead = False
        self.fire_pow = False
        self.star_pow = False
        self.mushroom_pow = False

    def update(self, stats, level, clips):
        if self.dead:
            self.die_animation(level, clips, stats)


    def calculate_gravity(self):
        if self.y_change == 0:
            self.y_change = 1
        else:
            self.y_change += .1

    def die_animation(self, level, clips, stats):
        pass