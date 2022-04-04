import pygame as pg
from pygame.sprite import Group
from mario import Mario
from settings import Settings
from map import Map
import sounds
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
    mario = Mario(screen, settings, pipes, bricks, stats, enemies, fireballs, secret_bricks, ground) #Missing a lot of arguments, add when completed

    if stats.game_active:
        game_f.check_events(mario, stats, fireballs)

Game()