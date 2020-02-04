from core.collider import Collider


class GameObject:
    def __init__(self, game, image, x=0, y=0):
        self.game = game
        self.image = image
        self.x, self.y = x, y
        self.width, self.height = game.assets_manager.get_image_size(image)
        self.offset_x = self.width * -0.5
        self.offset_y = self.height * -0.5
        self.vel, self.vel_x, self.vel_y = 0, 0, 0
        self.collider = Collider(self.x, self.y, self.width, self.height)

    def update(self, delta_time):
        self.x += self.vel_x * delta_time
        self.y += self.vel_y * delta_time
        self.collider.x, self.collider.y = self.x, self.y

    def draw(self, display):
        display.draw(self.image, self.x + self.offset_x, self.y + self.offset_y)
