import ctypes

from sdl2 import *
from sdl2 import sdlimage


class AssetsManager:
    def __init__(self, renderer):
        self._images = {}
        self.renderer = renderer

    def load_image(self, name, src):
        self._images[name] = sdlimage.IMG_LoadTexture(self.renderer, str.encode(src))

    def load_images(self, images):
        for name, src in images.items():
            self.load_image(name, src)

    def get_image(self, name):
        return self._images[name]

    def get_image_size(self, name):
        width = ctypes.c_int()
        height = ctypes.c_int()
        SDL_QueryTexture(self._images[name], None, None, width, height)
        return width.value, height.value

    def destroy(self):
        for image in self._images.values():
            SDL_DestroyTexture(image)
