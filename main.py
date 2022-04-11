import pygame as pg
from pygame.sprite import Group
from mario import Mario
from settings import Settings
from map import Map
import sounds
import goomba
import koopa
import game_functions as game_f
from stats import Stats
from mario import Mario
from settings import Settings
#Import other functions like the flag, pole, pipe, level, etc, when done

def Game():
    settings = Settings()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    stats = Stats()
    pipes = Group()
    ground = Group()
    enemies = Group()
    fireballs = Group()
    flags = Group()
    power_ups = Group()
    bricks = Group()
    secret_bricks = Group()
    secret_pipes = Group()
    poles = Group()
    mario = Mario(screen, settings, pipes, bricks, stats, enemies, poles, fireballs, secret_bricks, ground, secret_pipes) #Missing a lot of arguments, add when completed

    if stats.game_active:
        game_f.check_events(mario, stats, fireballs)

Game()
