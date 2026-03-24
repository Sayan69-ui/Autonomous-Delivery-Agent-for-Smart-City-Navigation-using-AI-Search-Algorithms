def reconstruct_path(came_from, start, goal):
    cur = goal
    path = []
    while cur != start:
        path.append(cur)
        cur = came_from[cur]
    path.append(start)
    path.reverse()
    return path