import pygame
import sys
from maze_logic import build_graph, find_start_end, maze, CELL_SIZE, rows, cols
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra

pygame.init()

ROWS, COLS = rows, cols
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver: Player vs AI (Arrows to Move, SPACE to Toggle)")

# --- COLORS ---
WHITE, BLACK, BLUE = (255, 255, 255), (20, 20, 20), (52, 152, 219)
GREEN, RED = (46, 204, 113), (231, 76, 60)
YELLOW, CYAN = (241, 196, 15), (52, 231, 228)
BROWN, WATER_BLUE = (139, 69, 19), (0, 105, 148)
ORANGE_PLAYER = (255, 165, 0)


def draw_maze():
    for r in range(ROWS):
        for c in range(COLS):
            x, y = c * CELL_SIZE, r * CELL_SIZE
            tile = maze[r][c]
            if tile == '#':
                color = BLACK
            elif tile == 'S':
                color = GREEN
            elif tile == 'E':
                color = RED
            elif tile == 'M':
                color = BROWN
            elif tile == 'W':
                color = WATER_BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE), 1)


def draw_path(path, color):
    if not path: return
    for (r, c) in path:
        if maze[r][c] not in ['S', 'E']:
            pad = CELL_SIZE // 4
            pygame.draw.rect(screen, color,
                             (c * CELL_SIZE + pad, r * CELL_SIZE + pad, CELL_SIZE - pad * 2, CELL_SIZE - pad * 2))


def draw_player(pos):
    r, c = pos
    center = (c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + CELL_SIZE // 2)
    pygame.draw.circle(screen, ORANGE_PLAYER, center, CELL_SIZE // 3)


def run_game():
    graph = build_graph()
    start, end = find_start_end()
    player_pos = list(start)  # [row, col]

    bfs_path = bfs(graph, start, end)
    d_res = dijkstra(graph, start, end)
    dijkstra_path = d_res[0] if d_res else None

    show_dijkstra, current_step, frame_count = True, 0, 0
    animation_speed = 8
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_dijkstra = not show_dijkstra
                    current_step = 0;
                    frame_count = 0

                # Player Movement Logic
                new_r, new_c = player_pos[0], player_pos[1]
                if event.key == pygame.K_UP:
                    new_r -= 1
                elif event.key == pygame.K_DOWN:
                    new_r += 1
                elif event.key == pygame.K_LEFT:
                    new_c -= 1
                elif event.key == pygame.K_RIGHT:
                    new_c += 1

                if 0 <= new_r < ROWS and 0 <= new_c < COLS and maze[new_r][new_c] != '#':
                    player_pos = [new_r, new_c]

        if tuple(player_pos) == end:
            pygame.display.set_caption("GOAL REACHED! Press SPACE to restart AI")

        screen.fill(WHITE)
        draw_maze()

        path = dijkstra_path if show_dijkstra else bfs_path
        if path:
            frame_count += 1
            if frame_count % animation_speed == 0 and current_step < len(path):
                current_step += 1
            draw_path(path[:current_step], YELLOW if show_dijkstra else CYAN)

        draw_player(player_pos)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run_game()