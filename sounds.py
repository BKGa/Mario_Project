import pygame as pg

class Sound:
    def __init__(self):
        pg.mixer.init()
        self.small_jump = pg.mixer.Sound('sounds/small_jump.wav')
        self.big_jump = pg.mixer.Sound('sounds/big_jump.wav')
        self.brick_break = pg.mixer.Sound('sounds/brick_break.wav')
        self.bump = pg.mixer.Sound('sounds/bump.wav')
        self.coin = pg.mixer.Sound('sounds/coin.wav')
        self.count_down = pg.mixer.Sound('sounds/count_down.wav')
        self.death = pg.mixer.Sound('sounds/death.wav')
        self.flagpole = pg.mixer.Sound('sounds/flagpole.wav')
        self.kick = pg.mixer.Sound('sounds/kick.wav')
        self.main_theme = pg.mixer.Sound('sounds/main_theme.wav')
        self.fast_theme = pg.mixer.Sound('sounds/main_theme_sped_up.wav')
        self.no_time = pg.mixer.Sound('sounds/out_of_time.wav')
        self.pipe = pg.mixer.Sound('sounds/pipe.wav')
        self.powerup = pg.mixer.Sound('sounds/powerup.wav')
        self.show_powerup = pg.mixer.Sound('sounds/powerup_appears.wav')
        self.win = pg.mixer.Sound('sounds/stage_clear.wav')
        self.stomp = pg.mixer.Sound('sounds/stomp.wav')
        self.fireball = pg.mixer.Sound('sounds/fire_ball.wav')

    def play_music(self, music, volume = 0.3):
        pg.mixer.music.unload()
        pg.mixer.music.load(music)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.play(-1, 0.0)

    def busy(self):
        return pg.mixer.get_busy()

    def play_sound(self, sound):
        pg.mixer.Sound.play(sound)

    def play_bg(self):
        self.play_music('sounds/main_theme.wav')

    def play_game_over(self):
        self.stop_bg()
        self.play_sound(self.death)

    def play_fireball(self):
        self.play_sound(self.fireball)