import pygame as pg
from pygame.sprite import Sprite

class Goomba(Sprite):
    def __init__(self, screen, settings, pipes, blocks, enemies, mario):
        super(Koopa, self).__init__()
        self.screen = screen
        self.settings = settings
        self.pipes = pipes
        self.blocks = blocks
        self.enemies = enemies
        self.mario = mario
        self.frames = []
        self.change_direction = False
        self.x_change = -0.5
        self.y_change = 0.0
        self.x = self.rect.x
        self.y = self.rect.y
        self.facing_left = True
        sheet = pg.image.load('images/allsprites.png')

    def update(self, mario):
        pass


    def move(self):
        collision = pg.sprite.spritecollide(self, self.blocks, False)
        if abs(self.rect.x - self.mario.rect.x) <= 2000 or not collision:

            pipe_collide = pg.sprite.spritecollide(self, self.pipes, False)
            for pipe in pipe_collide:
                if self.x_change > 0:
                    self.rect.right = pipe.rect.left - 2
                if self.x_change < 0:
                    self.rect.left = pipe.rect.right +2
                self.x_change *= -1
                self.swap()

    def swap(self):
        if self.moving_left:
            self.moving_left = False
        else:
            self.moving_left = True