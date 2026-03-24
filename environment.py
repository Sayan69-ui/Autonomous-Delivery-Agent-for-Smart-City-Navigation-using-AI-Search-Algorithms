import random

class Environment:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.dynamic_obstacles = []

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.rows and 0 <= y < self.cols

    def passable(self, pos):
        x, y = pos
        return self.grid[x][y] != '#'

    def neighbors(self, pos):
        x, y = pos
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        result = []
        for dx, dy in moves:
            nxt = (x+dx, y+dy)
            if self.in_bounds(nxt) and self.passable(nxt):
                result.append(nxt)
        return result

    def cost(self, pos):
        x, y = pos
        if self.grid[x][y] == 'W':
            return 5
        return 1

    def add_dynamic_obstacle(self, path):
        self.dynamic_obstacles.append({"path": path, "index": 0})

    def update_dynamic_obstacles(self):
        for obs in self.dynamic_obstacles:
            obs["index"] = (obs["index"] + 1) % len(obs["path"])

    def get_dynamic_positions(self):
        return [obs["path"][obs["index"]] for obs in self.dynamic_obstacles]