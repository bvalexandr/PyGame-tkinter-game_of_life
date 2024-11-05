import pygame as pg
import random
import copy

class Game:
    def __init__(self, width: int = 800, height: int = 600):
        self.width: int = width
        self.height: int = height
        self.fps: int = 60
        self.tile_size: int = 20
        self.clock: pg.time.Clock = pg.time.Clock()
        self.screen: pg.Surface = pg.display.set_mode((self.width, self.height))
        self.exit_game = False
        self.stop_game = True
        self.game_speed = 10
        self.game_field: list[list[int]] = [[0 for _ in range(self.width // self.tile_size)] for _ in range(self.height // self.tile_size)]
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
                            for row in self.game_field:
                                for col in range(len(row)):
                                    row[col] = 0
                        if keys[pg.K_r]:
                            for row in self.game_field:
                                for col in range(len(row)):
                                    row[col] = random.randint(0, 1)
                        if keys[pg.K_SPACE]:
                            self.stop_game = not self.stop_game
                    case pg.MOUSEBUTTONDOWN:
                        pos = pg.mouse.get_pos()
                        col = int(pos[0] // self.tile_size)
                        row = int(pos[1] // self.tile_size)
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
        copy_game_field = copy.deepcopy(self.game_field)
        neighborts_count: int = 0
        for row, _ in enumerate(copy_game_field):
            for col, _ in enumerate(copy_game_field[0]):
                neighborts_count = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if i == 0 and j == 0:
                            continue
                        if self.game_field[(row + i) % (self.height // self.tile_size)][(col + j) % (self.width // self.tile_size)]:
                            neighborts_count += 1
                cell_state = self.game_field[row][col]
                 #Обновление ячеек
                if cell_state and (neighborts_count == 2 or neighborts_count == 3):
                    copy_game_field[row][col] = 1
                elif cell_state and (neighborts_count < 2 or neighborts_count > 3):
                    copy_game_field[row][col] = 0
                if not cell_state and neighborts_count == 3:
                    copy_game_field[row][col] = 1
        self.game_field = copy.deepcopy(copy_game_field)

    def draw(self):
        pg.display.set_caption(f"Game of Life, {'play' if not self.stop_game else 'stop'}")
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