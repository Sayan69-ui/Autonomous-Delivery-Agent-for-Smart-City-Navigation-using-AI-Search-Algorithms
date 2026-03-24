import tkinter as tk
from agent import Agent
from environment import Environment

CELL_SIZE = 25
ROWS = 25
COLS = 25

class App:
    def __init__(self, root):
        self.root = root
        self.grid = self.generate_complex_map()

        self.env = Environment(self.grid)
        self.start = None
        self.goal = None
        self.agent = None

        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
        self.canvas.grid(row=0, column=0)

        # RIGHT PANEL (EXPLANATION)
        self.info_panel = tk.Text(root, width=40, height=30)
        self.info_panel.grid(row=0, column=1)

        # Buttons
        frame = tk.Frame(root)
        frame.grid(row=1, column=0)

        tk.Button(frame, text="BFS", command=lambda: self.run("BFS")).pack(side=tk.LEFT)
        tk.Button(frame, text="UCS", command=lambda: self.run("UCS")).pack(side=tk.LEFT)
        tk.Button(frame, text="A*", command=lambda: self.run("A*")).pack(side=tk.LEFT)
        tk.Button(frame, text="Reset", command=self.reset).pack(side=tk.LEFT)

        self.canvas.bind("<Button-1>", self.click)

        self.draw()

    def generate_complex_map(self):
        grid = [['.' for _ in range(COLS)] for _ in range(ROWS)]

        # Large buildings
        for i in range(5,20):
            grid[i][8] = '#'
            grid[i][15] = '#'

        for j in range(3,22):
            grid[10][j] = '#'

        # Narrow gaps
        grid[10][12] = '.'
        grid[15][8] = '.'

        # Traffic zones
        for i in range(ROWS):
            if i % 2 == 0:
                grid[i][5] = 'W'

        return grid

    def click(self, e):
        r = e.y // CELL_SIZE
        c = e.x // CELL_SIZE

        if not self.start:
            self.start = (r,c)
        elif not self.goal:
            self.goal = (r,c)

        self.draw()

    def run(self, algo):
        if not self.start or not self.goal:
            return

        self.agent = Agent(self.env, self.start, self.goal)
        self.agent.plan(algo)

        self.show_info()
        self.animate()

    def show_info(self):
        self.info_panel.delete(1.0, tk.END)
        info = self.agent.info

        text = f"""
Algorithm: {info['algo']}

Total Cost: {info['cost']}
Nodes Explored: {info['explored']}

Why this path?
{info['explanation']}
        """

        self.info_panel.insert(tk.END, text)

    def draw(self):
        self.canvas.delete("all")

        for i in range(ROWS):
            for j in range(COLS):
                color = "white"
                if self.grid[i][j] == '#':
                    color = "black"
                elif self.grid[i][j] == 'W':
                    color = "orange"

                if self.start == (i,j):
                    color = "green"
                elif self.goal == (i,j):
                    color = "red"

                self.canvas.create_rectangle(
                    j*CELL_SIZE, i*CELL_SIZE,
                    (j+1)*CELL_SIZE, (i+1)*CELL_SIZE,
                    fill=color, outline="gray"
                )

    def animate(self):
        pos = self.agent.step()
        if pos:
            self.draw()
            r,c = pos
            self.canvas.create_rectangle(
                c*CELL_SIZE, r*CELL_SIZE,
                (c+1)*CELL_SIZE, (r+1)*CELL_SIZE,
                fill="blue"
            )
            self.root.after(50, self.animate)

    def reset(self):
        self.grid = self.generate_complex_map()
        self.env = Environment(self.grid)
        self.start = None
        self.goal = None
        self.agent = None
        self.info_panel.delete(1.0, tk.END)
        self.draw()