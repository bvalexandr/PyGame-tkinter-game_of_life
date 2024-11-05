import pygame as pg

import life_functions as lf

class Game:
    def __init__(self, cell_count: int = 40, cell_size: int = 20, game_speed: int = 10):

        self.cell_size: int = cell_size
        self.game_speed = game_speed
        self.cell_count = cell_count
        self.game_field: list[list[int]] = lf.generate_field(self.cell_count, self.cell_count)
        
        self.clock: pg.time.Clock = pg.time.Clock()
        
        self.fps: int = 60
        self.exit_game = False
        self.stop_game = True

        self.width: int = self.cell_count * self.cell_size
        self.height: int = self.cell_count * self.cell_size
        self.screen: pg.Surface = pg.display.set_mode((self.width, self.height))

        self.init_game()

    def init_game(self):
        pg.init()
    
    def run(self):
        ticks = 0
        # Game Loop
        while not self.exit_game:
            for event in pg.event.get():
                match event.type:
                    case pg.QUIT:
                        self.exit_game = True
                    case pg.KEYDOWN:
                        keys = pg.key.get_pressed()
                        if keys[pg.K_c]:
                            self.game_field = lf.clear_field(self.cell_count, self.cell_count)
                        if keys[pg.K_r]:
                            self.game_field = lf.randomize_field(self.cell_count, self.cell_count)
                        if keys[pg.K_SPACE]:
                            self.stop_game = not self.stop_game
                    case pg.MOUSEBUTTONDOWN:
                        pos = pg.mouse.get_pos()
                        col = int(pos[0] // self.cell_size)
                        row = int(pos[1] // self.cell_size)
                        self.game_field[row][col] = 1
            if not self.stop_game:
                ticks += 1
                if ticks >= self.game_speed:
                    self.update()
                    ticks = 0
            self.draw()
            self.clock.tick(self.fps)
        pg.quit()
    
    def update(self):
        self.game_field = lf.check_field(self.game_field)

    def draw(self):
        pg.display.set_caption(f"Game of Life, {'play' if not self.stop_game else 'stop'}")

        # Заливаем задний фон
        self.screen.fill((255, 255, 255))
        
        # Рисуем сетку
        line_color: pg.Color = (100, 200, 100)
        for row in range(self.height // self.cell_size):
            pg.draw.line(self.screen, line_color, (0, row * self.cell_size), (self.width, row * self.cell_size))
        for col in range(self.width // self.cell_size):
            pg.draw.line(self.screen, line_color, (col * self.cell_size, 0), (col * self.cell_size, self.height))
        
        # Рисуем ячейки
        cell_color: pg.Color = (255, 0, 0)
        for i, row in enumerate(self.game_field):
            for j, col in enumerate(row):
                if col:
                    pg.draw.rect(self.screen, cell_color, (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))

        pg.display.update()