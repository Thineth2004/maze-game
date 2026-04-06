from models.queue import Queue

def bfs(graph, start, end):
    queue = Queue()
    queue.enqueue(start)

    visited = set()
    visited.add(start)

    parent = {}

    while not queue.is_empty():
        current = queue.dequeue()

        if current == end:
            break

        for neighbor, weight in graph.adj_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.enqueue(neighbor)

    # Reconstructing the path
    path = []
    node = end

    while node != start:
        path.append(node)
        node = parent.get(node)

        if node is None:
            return None

    path.append(start)
    path.reverse()

    return path