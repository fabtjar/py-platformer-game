class GameObject:
    def __init__(self, image, x=0, y=0):
        self.image, self.x, self.y = image, x, y
        self.vel, self.vel_x, self.vel_y = 0, 0, 0

    def update(self, delta_time):
        self.x += self.vel_x * delta_time
        self.y += self.vel_y * delta_time

    def draw(self, display):
        display.draw(self.image, self.x, self.y)
