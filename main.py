import pygame as pg

class Game:
    def __init__(self, width: int = 800, height: int = 600):
        self.init_game()
        self.width: int = width
        self.height: int = height
        self.fps: int = 60
        self.clock: pg.time.Clock = pg.time.Clock()
        self.screen: pg.Surface = pg.display.set_mode((self.width, self.height))
        self.exit_game = False

    def init_game(self):
        pg.init()
        pg.display.set_caption("Game of Life")
    
    def run(self):
        # Game Loop
        while not self.exit_game:
            for event in pg.event.get():
                match event.type:
                    case pg.QUIT:
                        self.exit_game = True
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pg.quit()
    
    def update(self):
        pass

    def draw(self):
        pass

if __name__ == "__main__":
    game: Game = Game()
    game.run()