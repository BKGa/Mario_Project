import pygame as pg
from pygame.sprite import Sprite

class Koopa(Sprite):
    def __init__(self, screen, settings, pipes, blocks, enemies, mario):
        super(Koopa, self).__init__()
        self.screen = screen
        self.settings = settings
        self.pipes = pipes
        self.blocks = blocks
        self.enemies = enemies
        self.mario = mario
        self.shell = False
        self.frames = []
        self.kicked = False
        self.change_direction = False
        self.x_change = -0.5
        self.y_change = 0.0
        self.x = self.rect.x
        self.y = self.rect.y
        self.facing_left = True
        sheet = pg.image.load('images/allsprites.png')

    def update(self, mario):
        if self.shell:
            self.image = self.frames[4]
            if self.kicked:
                if self.rect.x >= self.mario.rect.x:
                    if not self.change_direction:
                        self.x_change = -1
                        self.set_direction = True
                    self.move()
                if self.kicked and self.rect.x <= self.mario.rect.x:
                    if not self.set_direction:
                        self.x_change = -1
                        self.set_direction = True
                    self.move()
                collide_enemies = pg.sprite.spritecollide(self,self.enemies, False)
                for enemy in collide_enemies:
                    self.enemies.remove(enemy) #Each enemy that collides with the shell will get deleted

        else:
            self.move()


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

