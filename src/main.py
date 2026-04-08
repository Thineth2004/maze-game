from maze_logic import build_graph, find_start_end, display_maze, maze
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra

def main():
    graph = build_graph()
    start, end = find_start_end()

    print("--- MAZE SOLVER ---")
    print(f"Start: {start} | End: {end}")

    print("\nOriginal Maze:")
    display_maze(maze)

    bfs_path = bfs(graph, start, end)
    if bfs_path:
        print("\nBFS Solved Maze (Shortest Steps):")
        display_maze(maze, bfs_path)
        print(f"Steps: {len(bfs_path) - 1}")

    print("Debug - Start Node Neighbors:", graph.adj_list.get(start))

    dijkstra_result = dijkstra(graph, start, end)
    if dijkstra_result:
        dijkstra_path, cost = dijkstra_result
        print("\nDijkstra Solved Maze (Lowest Cost):")
        display_maze(maze, dijkstra_path)
        print(f"Total Cost: {cost}")
    else:
        print("\nDijkstra failed to find a path.")

if __name__ == "__main__":
    main()