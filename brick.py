import pygame as pg
from pygame.sprite import Sprite

class Brick(Sprite):

    def __init__(self, screen, block_type, settings):
        super().__init__()
        self.screen = screen
        self.block_type = block_type
        self.settings = settings

        self.size = 40
        self.ground = pg.image.load('images/Ground_Brick.png')
        self.item_brick = pg.image.load('images/Item_Brick.png')
        self.blue_brick = pg.image.load('images/Blue_Brick.png')
        self.blue_stone = pg.image.load('images/Blue_Stone.png')
        self.invisible_brick = pg.image.load('images/Invisible_Block.png')
        self.brick = pg.image.load('images/Red_Brick.png')
        self.stair_brick = pg.image.load('images/Stair_Brick.png')
        self.empty_brick =pg.image.load('images/Empty_Brick.png')

        if block_type == 0:
            self.image = self.brick
        elif block_type == 1:
            self.image = self.item_brick
        elif block_type == 2:
            self.image = self.stair_brick
        elif block_type == 3:
            self.image = self.invisible_brick
        elif block_type == 4:
            self.image = self.blue_brick
        elif block_type == 5:
            self.image = self.blue_stone

        self.image = pg.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.original_pos = self.rect.y
        self.frame_count = 0
        self.bouncing = False

    def convert(self):
        self.image = self.empty_brick
        self.image = pg.transform.scale(self.image, (40, 40))

    def update(self):
        if self.bouncing:
            if self.frame_count <= 5:
                self.rect.y -= 1
            elif self.frame_count <= 10:
                self.rect.y += 1
            else:
                self.frame_count = 0
                self.bouncing = False
            self.frame_count += 1
