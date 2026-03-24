from collections import deque
from search.utils import reconstruct_path

def bfs(env, start, goal):
    queue = deque([start])
    came_from = {start: None}
    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            return path, len(path), nodes_explored

        for nxt in env.neighbors(current):
            if nxt not in came_from:
                queue.append(nxt)
                came_from[nxt] = current

    return None, None, nodes_explored