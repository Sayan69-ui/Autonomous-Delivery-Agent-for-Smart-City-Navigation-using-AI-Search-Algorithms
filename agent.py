from search.bfs import bfs
from search.ucs import ucs
from search.astar import astar

class Agent:
    def __init__(self, env, start, goal):
        self.env = env
        self.start = start
        self.goal = goal
        self.path = []
        self.current_index = 0
        self.info = {}

    def plan(self, method):
        if method == "BFS":
            path, cost, explored = bfs(self.env, self.start, self.goal)
            explanation = "BFS finds shortest path in steps, ignores terrain cost."

        elif method == "UCS":
            path, cost, explored = ucs(self.env, self.start, self.goal)
            explanation = "UCS finds lowest cost path considering terrain weights."

        elif method == "A*":
            path, cost, explored = astar(self.env, self.start, self.goal)
            explanation = "A* uses heuristic (Manhattan distance) + cost to find optimal path faster."

        self.path = path
        self.current_index = 0

        self.info = {
            "algo": method,
            "cost": cost,
            "explored": explored,
            "explanation": explanation
        }

    def step(self):
        if self.path and self.current_index < len(self.path):
            pos = self.path[self.current_index]
            self.current_index += 1
            return pos
        return None