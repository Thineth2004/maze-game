import pygame
import sys
from maze_logic import build_graph, find_start_end, maze
from algorithms.dijkstra import dijkstra

pygame.init()

CELL_SIZE = 80
ROWS = len(maze)
COLS = len(maze[0])

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver: Logic to Visuals")

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
BLUE = (52, 152, 219)
YELLOW = (241, 196, 15)


def draw_maze(path=None):
    path_set = set(path) if path else set()

    for r in range(ROWS):
        for c in range(COLS):
            x = c * CELL_SIZE
            y = r * CELL_SIZE

            if maze[r][c] == '#':
                color = BLACK
            elif maze[r][c] == 'S':
                color = GREEN
            elif maze[r][c] == 'E':
                color = RED
            elif (r, c) in path_set:
                color = YELLOW
            else:
                color = WHITE

            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE), 1)


def run_game():
    graph = build_graph()
    start, end = find_start_end()

    dijkstra_result = dijkstra(graph, start, end)
    path_to_draw = dijkstra_result[0] if dijkstra_result else None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)

        draw_maze(path=path_to_draw)

        pygame.display.update()


if __name__ == "__main__":
    run_game()