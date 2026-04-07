from models.graph import Graph
# Maze representation

# S = Start
# E = End
# . = Walkable
# # = Wall

maze = [
    ['S', '.', '.', '#'],
    ['.', '#', '.', '.'],
    ['.', '.', '.', 'E']
]

rows = len(maze)
cols = len(maze[0])

def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols and maze[r][c] != '#'

def find_start_end():
    start = None
    end = None

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    return start, end

def build_graph():
    graph = Graph()

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != '#':
                current = (r, c)
                graph.add_node(current)

                # directions
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if is_valid(nr, nc):
                        neighbor = (nr, nc)

                        # Weight logic
                        if maze[nr][nc] == '.':
                            weight = 1
                        elif maze[nr][nc] == 'E':
                            weight = 1
                        else:
                            weight = 1

                        graph.add_edge(current, neighbor, weight)

    return graph
