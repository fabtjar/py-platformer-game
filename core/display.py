from sdl2 import *


class Display:
    def __init__(self, title, width, height, scale):
        self.window = SDL_CreateWindow(
            str.encode(title),
            SDL_WINDOWPOS_UNDEFINED,
            SDL_WINDOWPOS_UNDEFINED,
            width * scale,
            height * scale,
            0
        )
        self.renderer = SDL_CreateRenderer(self.window, -1, SDL_RENDERER_ACCELERATED)
        self.get_image = None
        SDL_RenderSetScale(self.renderer, scale, scale)

    def draw(self, image, x, y):
        SDL_RenderCopy(self.renderer, self.get_image(image), None, SDL_Rect(int(x), int(y), 16, 16))

    def destroy(self):
        SDL_DestroyRenderer(self.renderer)
        SDL_DestroyWindow(self.window)
