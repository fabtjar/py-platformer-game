from core.keyboard import Keyboard


class Player:
    def __init__(self, image, x=0, y=0):
        self.image = image
        self.x = x
        self.y = y
        self.vel = 200
        self.vel_x, self.vel_y = 0, 0
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

        if input_hor or input_ver:
            self.vel_x = input_hor * self.vel * delta_time
            self.vel_y = input_ver * self.vel * delta_time
        else:
            self.vel_x, self.vel_y = 0, 0

        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self, display):
        display.draw(self.image, self.x, self.y)
