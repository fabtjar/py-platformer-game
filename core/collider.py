from math import copysign


class Collider:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height

    def get_overlapping(self, other, move_x=0, move_y=0):
        if (
            self.x + move_x - self.width / 2 < other.x + other.width / 2 and
            self.x + move_x + self.width / 2 > other.x - other.width / 2 and
            self.y + move_y - self.height / 2 < other.y + other.height / 2 and
            self.y + move_y + self.height / 2 > other.y - other.height / 2
        ):
            dist_x = other.x - self.x
            dist_y = other.y - self.y
            width_x = self.width / 2 + other.width / 2
            width_y = self.height / 2 + other.height / 2
            return {
                "gap_x": dist_x - copysign(width_x, dist_x),
                "gap_y": dist_y - copysign(width_y, dist_y)
            }
