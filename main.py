
from random import randint
import pygame
import numpy as np
import sys


COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 10


def update(screen: pygame.Surface, cells: np.ndarray, with_progress: bool = False) -> np.ndarray:
    updated_cells = np.zeros(cells.shape)

    for row, col in np.ndindex(cells.shape):
        alive_neighbours = np.sum(cells[row - 1: row + 2, col - 1: col + 2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive_neighbours == 2 or alive_neighbours == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
            else:
                if with_progress:
                    color = COLOR_DIE_NEXT
        else:
            if alive_neighbours == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
    return updated_cells


def get_random_board() -> np.ndarray:
    cells = np.zeros((WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE))

    for row, col in np.ndindex(cells.shape):
        cells[row][col] = 0 if randint(0, 2) in [0, 1] else 1

    return cells

def get_gun() -> np.ndarray:
    cells = np.zeros((WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE))

    cells


def main(refresh=10):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Game of life | running: False")

    cells = np.zeros((WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE))
    screen.fill(COLOR_GRID)
    update(screen, cells)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    running = not running
                    pygame.display.set_caption("Game of life | running: " + str(running))
                elif event.key == pygame.K_c:
                    cells = np.zeros((WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE))
                elif event.key == pygame.K_r:
                    cells = get_random_board()
                update(screen, cells)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = x // TILE_SIZE, y // TILE_SIZE
                cells[col, row] = 1 if cells[col, row] == 0 else 0
                update(screen, cells)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, True)
            pygame.display.update()

        clock.tick(refresh)




if __name__ == "__main__":
    main() if len(sys.argv) == 1 else main(int(sys.argv[1]))

