from sdl2 import SDLK_UP, SDLK_DOWN, SDLK_LEFT, SDLK_RIGHT


class Keyboard:
    UP = SDLK_UP
    DOWN = SDLK_DOWN
    LEFT = SDLK_LEFT
    RIGHT = SDLK_RIGHT

    def __init__(self):
        self._is_key_down = {}

    def set_key_down(self, key_code, is_down):
        self._is_key_down[key_code] = is_down

    def is_key_down(self, key_code):
        try:
            return self._is_key_down[key_code]
        except KeyError:
            return False
