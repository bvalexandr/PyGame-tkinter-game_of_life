import pygame as pg
import random

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
        self.game_field: list[list[int]] = [[random.randint(0, 1) for _ in range(self.width // self.tile_size)] for _ in range(self.height // self.tile_size)]

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
                    case pg.KEYDOWN:
                        keys = pg.key.get_pressed()
                        if keys[pg.K_c]:
                            for row in self.game_field:
                                for col in range(len(row)):
                                    row[col] = 0
                        if keys[pg.K_r]:
                            for row in self.game_field:
                                for col in range(len(row)):
                                    row[col] = random.randint(0, 1)
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pg.quit()
    
    def update(self):
        pass

    def draw(self):
        # Заливаем задний фон
        self.screen.fill((255, 255, 255))
        
        # Рисуем сетку
        line_color: pg.Color = (100, 200, 100)
        for row in range(self.height // self.tile_size):
            pg.draw.line(self.screen, line_color, (0, row * self.tile_size), (self.width, row * self.tile_size))
        for col in range(self.width // self.tile_size):
            pg.draw.line(self.screen, line_color, (col * self.tile_size, 0), (col * self.tile_size, self.height))
        
        # Рисуем ячейки
        cell_color: pg.Color = (255, 0, 0)
        for i, row in enumerate(self.game_field):
            for j, col in enumerate(row):
                if col:
                    pg.draw.rect(self.screen, cell_color, (j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size))

        pg.display.update()

if __name__ == "__main__":
    game: Game = Game()
    game.run()