from vector import Vector

class Settings:
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (100, 255, 100)
    BROWN = (124, 66, 0)

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (107, 140, 255)

        #Mario Physics
        self.mario_speed_factor = 0.0005
        self.max_velocity = 0.35
        self.gravity = 0.002
        self.max_jump_height = 140
        self.friction = 1
        self.deceleration_friction = 0.95
        self.brake_friction = 0.85

        self.mario_limit = 3

        #self.alien_speed_factor = 0.25
        #self.alien_laser_speed = 0.5
        #self.fleet_drop_speed = 8
        #self.fleet_direction = Vector(1, 0)

        self.fireball_speed_factor = 1
        self.fireball_width = 5
        self.fireball = 5
        self.laser_color = 255, 0, 0