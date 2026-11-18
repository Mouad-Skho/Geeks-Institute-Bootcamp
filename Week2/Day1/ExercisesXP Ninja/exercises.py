# import matplotlib.animation as animation
# import matplotlib.pyplot as plt
# import numpy as np

# # 1. Define the grid (mesh) size
# GRID_SIZE = 30
# grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# # 2. Define famous patterns as small 2D arrays
# glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

# blinker = np.array([[1, 1, 1]])

# # 3. Place the patterns onto the main mesh
# grid[2:5, 2:5] = glider
# grid[15:16, 15:18] = blinker


# # 4. Function to compute the next generation
# def update(frame, img, grid):
#   # Count live neighbors using array slicing/rolling (wraps around edges)
#   neighbors = (
#       np.roll(grid, 1, axis=0)
#       + np.roll(grid, -1, axis=0)
#       + np.roll(grid, 1, axis=1)
#       + np.roll(grid, -1, axis=1)
#       + np.roll(np.roll(grid, 1, axis=0), 1, axis=1)
#       + np.roll(np.roll(grid, 1, axis=0), -1, axis=1)
#       + np.roll(np.roll(grid, -1, axis=0), 1, axis=1)
#       + np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
#   )

#   # Apply Conway's rules
#   new_grid = np.zeros_like(grid)
#   # Rule 1 & 2: Live cell with 2 or 3 neighbors survives
#   new_grid[(grid == 1) & ((neighbors == 2) | (neighbors == 3))] = 1
#   # Rule 3: Dead cell with exactly 3 neighbors becomes alive
#   new_grid[(grid == 0) & (neighbors == 3)] = 1

#   # Update the grid and the visual plot
#   grid[:] = new_grid[:]
#   img.set_data(grid)
#   return (img,)


# # 5. Set up the visualization
# fig, ax = plt.subplots()
# img = ax.imshow(grid, interpolation='nearest', cmap='binary')
# ax.set_title("Conway's Game of Life")
# plt.axis('off')

# ani = animation.FuncAnimation(
#     fig, update, fargs=(img, grid), frames=100, interval=100, save_count=50
# )
# plt.show()

# import time
# from itertools import product

# MAX_SIZE = 10_000  # maximum border size for the expandable universe


# class FixedGrid:
#     """Universe with fixed borders. Live cells going out of the border die."""

#     def __init__(self, rows, cols, alive=()):
#         self.rows, self.cols = rows, cols
#         self.cells = {(r, c) for r, c in alive if 0 <= r < rows and 0 <= c < cols}

#     def neighbours(self, r, c):
#         return sum(
#             (r + dr, c + dc) in self.cells
#             for dr, dc in product((-1, 0, 1), repeat=2)
#             if (dr, dc) != (0, 0)
#         )

#     def step(self):
#         new = set()
#         for r in range(self.rows):
#             for c in range(self.cols):
#                 n = self.neighbours(r, c)
#                 if (r, c) in self.cells and n in (2, 3):
#                     new.add((r, c))
#                 elif (r, c) not in self.cells and n == 3:
#                     new.add((r, c))
#         self.cells = new

#     def state(self):
#         return frozenset(self.cells)

#     def render(self):
#         return "\n".join(
#             "".join("█" if (r, c) in self.cells else "·" for c in range(self.cols))
#             for r in range(self.rows)
#         )


# class ExpandableGrid(FixedGrid):
#     """Universe whose borders expand to fit the live cells (up to MAX_SIZE).

#     Only live cells are stored, so memory depends on the population and not
#     on the size of the board. Cells that would leave the MAX_SIZE x MAX_SIZE
#     area exit the game.
#     """

#     def __init__(self, alive=(), max_size=MAX_SIZE):
#         super().__init__(0, 0, ())
#         self.max_size = max_size
#         self.cells = set(alive)
#         self._fit_to_cells()

#     def _fit_to_cells(self):
#         if not self.cells:
#             self.min_r = self.min_c = 0
#             self.rows = self.cols = 0
#             return
#         rs = [r for r, _ in self.cells]
#         cs = [c for _, c in self.cells]
#         self.min_r, self.min_c = min(rs), min(cs)
#         self.rows = min(max(rs) - self.min_r + 1, self.max_size)
#         self.cols = min(max(cs) - self.min_c + 1, self.max_size)

#     def step(self):
#         counts = {}
#         for r, c in self.cells:
#             for dr, dc in product((-1, 0, 1), repeat=2):
#                 if (dr, dc) != (0, 0):
#                     key = (r + dr, c + dc)
#                     counts[key] = counts.get(key, 0) + 1
#         self.cells = {
#             pos
#             for pos, n in counts.items()
#             if n == 3 or (n == 2 and pos in self.cells)
#         }
#         self._fit_to_cells()
#         # enforce the maximum border size
#         self.cells = {
#             (r, c)
#             for r, c in self.cells
#             if r - self.min_r < self.max_size and c - self.min_c < self.max_size
#         }

#     def render(self):
#         if not self.cells:
#             return "(empty universe)"
#         # add a 1-cell margin so the growth is visible
#         return "\n".join(
#             "".join(
#                 "█" if (r, c) in self.cells else "·"
#                 for c in range(self.min_c - 1, self.min_c + self.cols + 1)
#             )
#             for r in range(self.min_r - 1, self.min_r + self.rows + 1)
#         )


# class Game:
#     """Runs a universe, displays each generation and detects the ending."""

#     def __init__(self, universe, max_generations=100, delay=0.0):
#         self.universe = universe
#         self.max_generations = max_generations
#         self.delay = delay
#         self.history = [universe.state()]
#         self.generation = 0

#     def display(self):
#         print(f"\nGeneration {self.generation}  "
#               f"(alive: {len(self.universe.cells)})")
#         print(self.universe.render())

#     def run(self):
#         self.display()
#         while self.generation < self.max_generations:
#             self.universe.step()
#             self.generation += 1
#             self.display()
#             time.sleep(self.delay)

#             state = self.universe.state()
#             if not state:
#                 return f"Extinction after {self.generation} generations."
#             if state in self.history:
#                 period = len(self.history) - self.history.index(state)
#                 if period == 1:
#                     return f"Stable pattern reached at generation {self.generation}."
#                 return (f"Oscillator of period {period} reached at "
#                         f"generation {self.generation}.")
#             self.history.append(state)
#         return f"Still evolving after {self.max_generations} generations."


# # ----------------------------- initial states -----------------------------
# PATTERNS = {
#     "block":   [(1, 1), (1, 2), (2, 1), (2, 2)],
#     "blinker": [(2, 1), (2, 2), (2, 3)],
#     "glider":  [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
#     "lonely":  [(3, 3), (3, 4)],
#     "r-pentomino": [(1, 2), (1, 3), (2, 1), (2, 2), (3, 2)],
# }


# def main():
#     print("=== FIXED BORDERS ===")
#     for name in ("block", "blinker", "lonely", "glider"):
#         print(f"\n##### {name} #####")
#         game = Game(FixedGrid(8, 8, PATTERNS[name]), max_generations=30)
#         print("\nResult:", game.run())

#     print("\n\n=== EXPANDABLE BORDERS (bonus) ===")
#     game = Game(ExpandableGrid(PATTERNS["glider"]), max_generations=8)
#     print("\nResult:", game.run())


# if __name__ == "__main__":
#     main()