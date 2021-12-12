import lib.helpers as helpers
from itertools import product


class Grid:

    def __init__(self, grid_data, size):
        self.grid_size = size
        self.grid_nums = []
        self.nums_drawn = []
        self.last_drawn = None

        for row in range(self.grid_size):
            self.grid_nums.append([int(a) for a in grid_data[row].split(" ")])
            self.nums_drawn.append([False for _ in range(grid_size)])


    def reset(self):
        for row, col in product(range(grid_size), range(grid_size)):
            self.nums_drawn[row][col] = False

    def draw(self, value):
        self.last_drawn = value
        for row, col in product(range(grid_size), range(grid_size)):
            if self.grid_nums[row][col] == value:
                self.nums_drawn[row][col] = True

    def has_won(self):
        grid_drawn_transposed = list(zip(*self.nums_drawn))
        return self.check_rows(self.nums_drawn) or self.check_rows(grid_drawn_transposed)

    def check_rows(self, d):

        for row in d:
            if sum(row) == len(row):
                return True
        return False

    def score(self):
        score = 0
        for row, column in product(range(grid_size), range(grid_size)):
            score += self.grid_nums[row][column] * (not self.nums_drawn[row][column])
        return score


def find_winner(grids, numbers):

    for number in numbers:
        for grid in grids:
            grid.draw(number)
            if grid.has_won():
                return grid


def find_looser(grids, numbers):
    for number in numbers:
        for grid in grids:
            grid.draw(number)
            if sum([g.has_won() for g in grids]) == len(grids):
                return grid


if __name__ == "__main__":

    data = helpers.clean_input_data("../data/day4.txt")

    number_call = [int(n) for n in data[0].split(",")]
    grid_data_raw = data[1:]

    grid_size = 5

    bingo_grids = []

    for i in range(0, len(grid_data_raw), grid_size):
        grid = Grid(grid_data_raw[i:], grid_size)
        bingo_grids.append(grid)

    winning_grid = find_winner(bingo_grids, number_call)

    print("part 1 puzzle input: ", winning_grid.score() * winning_grid.last_drawn)

    [g.reset() for g in bingo_grids]

    loosing_grid = find_looser(bingo_grids, number_call)

    print("part 2 puzzle input: ", loosing_grid.score() * loosing_grid.last_drawn)
