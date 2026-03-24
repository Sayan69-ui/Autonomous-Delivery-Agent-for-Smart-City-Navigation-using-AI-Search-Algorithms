import heapq
from search.utils import reconstruct_path

def ucs(env, start, goal):
    pq = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    nodes_explored = 0

    while pq:
        cost, current = heapq.heappop(pq)
        nodes_explored += 1

        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            return path, cost_so_far[goal], nodes_explored

        for nxt in env.neighbors(current):
            new_cost = cost_so_far[current] + env.cost(nxt)
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
                came_from[nxt] = current

    return None, None, nodes_explored