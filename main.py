import pygame as pg

class Game:
    def __init__(self, width: int = 800, height: int = 600):
        self.init_game()
        self.width: int = width
        self.height: int = height
        self.fps: int = 60
        self.tile_size: int = 10
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
        self.screen.fill((255, 255, 255))
        # Рисуем сетку
        line_color: pg.Color = (100, 200, 100)
        for row in range(self.height // self.tile_size):
            pg.draw.line(self.screen, line_color, (0, row * self.tile_size), (self.width, row * self.tile_size))
        for col in range(self.width // self.tile_size):
            pg.draw.line(self.screen, line_color, (col * self.tile_size, 0), (col * self.tile_size, self.height))
        pg.display.update()

if __name__ == "__main__":
    game: Game = Game()
    game.run()