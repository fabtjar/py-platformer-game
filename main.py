from core.game import Game
from core.level import Level
from player import Player

GRID_SIZE = 16


def main():
    game = Game("Game", 320, 240, 3)

    game.assets_manager.load_images({
        "bg": "assets/background.png",
        "player": "assets/player.png",
        "wall": "assets/wall.png"
    })

    level = Level("wall", GRID_SIZE)
    player = Player(game, "player", 150, 50)
    player.keyboard = game.keyboard

    def update(delta_time):
        player.update(delta_time)

        draw()

    def draw():
        for bg_x in range(int(game.width / GRID_SIZE)):
            for bg_y in range(int(game.height / GRID_SIZE)):
                game.display.draw("bg", bg_x * GRID_SIZE, bg_y * GRID_SIZE)
        game.draw(level)
        game.draw(player)

    game.update = update
    game.run()


if __name__ == "__main__":
    main()
