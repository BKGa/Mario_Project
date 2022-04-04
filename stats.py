import pygame as pg

class Stats:
    def __init__(self):
        self.game_active = True
        self.game_over = False
        self.at_pole = False
        self.at_bottom_of_flag = False
        self.active_secret = False
        self.active_main = True
        self.main_level = True
        self.score = 0
        self.coins = 0
        self.time = 400
        self.lives = 3
        self.timer = 0
        self.play_victory = False
        self.high_score = 0
        self.world_record = open('highscore.txt')

    def reset_stats(self):
        self.score = 0
        self.coins = 0
        self.time = 400
        self.lives = 3
        self.game_over = False
        self.at_pole = False
        self.at_bottom_of_flag = False
        self.active_secret = False
        self.main_level = True

    def update_highscore_txt(self):
        self.world_record.seek(0)
        self.current = int(self.world_record.read())

    def save_high_score(self):
        try:
            with open("highscore.txt", "w+") as f:
                f.write(str(round(self.high_score, -1)))  # 314.15 --> 310,  (0) --> 314
        except:
            print("highscore.txt not found...")

    def get_score(self):
        return self.score

    def get_highscore(self):
        return self.high_score
