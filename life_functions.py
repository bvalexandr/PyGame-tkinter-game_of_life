import random
import copy


def generate_field(rows: int, cols: int) -> list[list[int]]:
    """
    Генерация заполненной 0 двумерной матрицы.

    Arguments:
        rows - число строк
        cols - число столбцов

    Return:
        field - двумерная матрица
    """
    field: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]
    return field

def clear_field(rows: int, cols: int) -> list[list[int]]:
    """
    Очистка двумерной матрицы.

    Arguments:
        rows - число строк
        cols - число столбцов

    Return:
        field - двумерная матрица
    """
    field = generate_field(rows, cols)
    return field

def randomize_field(rows: int, cols: int) -> list[list[int]]:
    """
    Генерация заполненной случайным образом [0..1] двумерной матрицы.

    Arguments:
        rows - число строк
        cols - число столбцов

    Return:
        field - двумерная матрица
    """
    field = generate_field(rows, cols)
    for row in range(rows):
        for col in range(cols):
            field[row][col] = random.randint(0, 1)
    return field

def check_field(game_field: list[list[int]]) -> list[list[int]]:
    """
    Проверка двумерной матрицы согласно правилам игры Game of Life.

    Arguments:
        game_field - исходная матрица

    Return:
        field - итоговая матрица
    """
    copy_game_field = copy.deepcopy(game_field)
    neighborts_count: int = 0

    rows = len(game_field)
    cols = len(game_field[0])

    for row, _ in enumerate(copy_game_field):
        for col, _ in enumerate(copy_game_field[0]):
            # Подсчет соседей
            # Матрица замкнута на себя
            neighborts_count = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    if game_field[(row + i) % rows][(col + j) % cols]:
                        neighborts_count += 1
            cell_state = game_field[row][col]

            #Обновление ячеек
            if cell_state and (neighborts_count == 2 or neighborts_count == 3):
                copy_game_field[row][col] = 1
            elif cell_state and (neighborts_count < 2 or neighborts_count > 3):
                copy_game_field[row][col] = 0
            if not cell_state and neighborts_count == 3:
                copy_game_field[row][col] = 1

    return copy_game_field