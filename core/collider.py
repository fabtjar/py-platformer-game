class Collider:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height

    def is_overlapping(self, other, move_x=0, move_y=0):
        return (
            self.x + move_x - self.width / 2 < other.x + other.width / 2 and
            self.x + move_x + self.width / 2 > other.x - other.width / 2 and
            self.y + move_y - self.height / 2 < other.y + other.height / 2 and
            self.y + move_y + self.height / 2 > other.y - other.height / 2
        )
