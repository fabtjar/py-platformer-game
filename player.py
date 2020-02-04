from core.game_object import GameObject
from core.keyboard import Keyboard


class Player(GameObject):
    def __init__(self, game, image, x=0, y=0):
        super().__init__(game, image, x, y)
        self.vel = 200
        self.gravity = 1500
        self.jump_force = 350
        self.on_ground = False
        self.keyboard = None
        self.level_colliders = None

    def update(self, delta_time):
        input_hor = 0
        is_jumping = False
        if self.keyboard.is_key_down(Keyboard.UP):
            is_jumping = True
        if self.keyboard.is_key_down(Keyboard.LEFT):
            input_hor -= 1
        if self.keyboard.is_key_down(Keyboard.RIGHT):
            input_hor += 1

        self.vel_x = input_hor * self.vel
        self.vel_y += self.gravity * delta_time

        if is_jumping and self.on_ground:
            self.vel_y = -self.jump_force

        move_x = self.vel_x * delta_time
        move_y = self.vel_y * delta_time

        for collider in self.level_colliders:
            hit = self.collider.get_overlapping(collider, move_x, 0)
            if hit:
                move_x = hit["gap_x"]
        self.x += move_x

        self.on_ground = False
        for collider in self.level_colliders:
            hit = self.collider.get_overlapping(collider, 0, move_y)
            if hit:
                if move_y > 0:
                    self.on_ground = True
                move_y = hit["gap_y"]
                self.vel_y = 0
        self.y += move_y

        self.collider.x, self.collider.y = self.x, self.y
