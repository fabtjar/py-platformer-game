import time

from sdl2 import *

from core.assets import AssetsManager
from core.display import Display
from core.keyboard import Keyboard


class Game:
    def __init__(self, title, width, height, scale):
        SDL_Init(SDL_INIT_VIDEO)

        self.width = width
        self.height = height
        self.display = Display(title, width, height, scale)
        self.assets_manager = AssetsManager(self.display.renderer)
        self.display.get_image = self.assets_manager.get_image
        self.keyboard = Keyboard()

    def run(self):
        event = SDL_Event()
        last_time = time.time()
        running = True

        while running:
            time_now = time.time()
            delta_time = time_now - last_time
            last_time = time_now

            SDL_PollEvent(event)
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                self.keyboard.set_key_down(event.key.keysym.sym, True)
            elif event.type == SDL_KEYUP:
                self.keyboard.set_key_down(event.key.keysym.sym, False)

            self.update(delta_time)

            SDL_RenderPresent(self.display.renderer)

        self.destroy()

    def draw(self, drawable):
        drawable.draw(self.display)

    def destroy(self):
        self.assets_manager.destroy()
        self.display.destroy()
        SDL_Quit()
