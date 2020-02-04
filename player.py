from core.game_object import GameObject
from core.keyboard import Keyboard


class Player(GameObject):
    def __init__(self, image, x=0, y=0):
        super().__init__(image, x, y)
        self.vel = 200
        self.keyboard = None

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

        super().update(delta_time)
