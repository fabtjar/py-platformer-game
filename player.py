from core.game_object import GameObject
from core.keyboard import Keyboard


class Player(GameObject):
    def __init__(self, game, image, x=0, y=0):
        super().__init__(game, image, x, y)
        self.vel = 200
        self.keyboard = None
        self.level_colliders = None

    def update(self, delta_time):
        input_hor, input_ver = 0, 0
        if self.keyboard.is_key_down(Keyboard.UP):
            input_ver -= 1
        if self.keyboard.is_key_down(Keyboard.DOWN):
            input_ver += 1
        if self.keyboard.is_key_down(Keyboard.LEFT):
            input_hor -= 1
        if self.keyboard.is_key_down(Keyboard.RIGHT):
            input_hor += 1

        self.vel_x = input_hor * self.vel
        self.vel_y = input_ver * self.vel

        move_x = self.vel_x * delta_time
        move_y = self.vel_y * delta_time

        for collider in self.level_colliders:
            if self.collider.is_overlapping(collider, move_x, 0):
                move_x = 0
            if self.collider.is_overlapping(collider, move_x, move_y):
                move_y = 0

        self.x += move_x
        self.y += move_y
        self.collider.x, self.collider.y = self.x, self.y
