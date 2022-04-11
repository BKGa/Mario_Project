import pygame as pg
from vector import Vector
from pygame.sprite import Sprite, Group
from copy import copy
from random import randint
from sounds import Sound
from goomba import Goomba
from koopa import Koopa



class Fireballs:
    def __init__(self, game, owner):
        self.game = game
        self.stats = game.stats
        self.sound = game.sound
        self.owner = owner
        self.enemy = Goomba, Koopa #Unsure with this code just yet
        self.fireballs = Group()

    def add(self, fireball):
        self.fireballs.add(fireball)

    def empty(self):
        self.fireballs.empty()

    def fire(self):
        new_laser = Fireball(self.game)
        self.fireballs.add(new_laser)
        snd = self.sound
        #snd.play_fire_phaser() if type(self.owner) is alien.AlienFleet else snd.play_fire_photon()

    def update(self):
        for fireball in self.fireballs.copy():
            if fireball.rect.bottom <= 0: self.fireballs.remove(fireball)

        collisions = pg.sprite.groupcollide(self.alien_fleet.fleet, self.fireballs, False, True)
        for enemy in collisions:
            if not enemy.dying:
                enemy.hit()

        if self.alien_fleet.length() == 0:
            self.game.restart()

        for fireball in self.fireballs:
            fireball.update()

    def draw(self):
        for fireball in self.fireballs:
            fireball.draw()


class Fireball(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.w, self.h = self.settings.laser_width, self.settings.laser_height
        self.ship = game.ship

        self.rect = pg.Rect(0, 0, self.w, self.h)
        self.center = copy(self.ship.center)


        fireball_images = [pg.image.load(f'images/fireball{n}.png' for n in range(3))]
        self.color = fireball_images
        #Add code that would be used to determine which way the player is facing
        #Ex: If mario's image = fire mario facing to the right, then the vector speed for the fireball would be (1,0)
        #If mario's image is facing to the left, then the vector speed would be (-1,0)
        self.v = Vector(1, 0) * self.settings.laser_speed_factor

    def update(self):
        self.center += self.v
        self.rect.x, self.rect.y = self.center.x, self.center.y

    def draw(self): pg.draw.rect(self.screen, color=self.color, rect=self.rect)