import lib.helpers as helpers


class Grid:

    def __init__(self, grid_data, size):
        self.grid_size = size
        self.grid_nums = []
        self.nums_drawn = []

        for row in range(self.grid_size):
            self.grid_nums.append([int(a) for a in grid_data[row].split(" ")])
            self.nums_drawn.append([False for _ in range(self.grid_size)])

    def draw(self, value):
        for row in range(self.grid_size):
            for column in range(self.grid_size):
                if self.grid_nums[row][column] == value:
                    self.nums_drawn[row][column] = True

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
        for row in range(self.grid_size):
            for column in range(self.grid_size):
                score += self.grid_nums[row][column] * (not self.nums_drawn[row][column])
        return score


if __name__ == "__main__":

    data = helpers.clean_input_data("../data/day4.txt")

    number_call = [int(n) for n in data[0].split(",")]
    grid_data_raw = data[1:]

    grid_size = 5

    grids = []

    for i in range(0, len(grid_data_raw), grid_size):
        grid = Grid(grid_data_raw[i:], grid_size)
        grids.append(grid)

    for number in number_call:
        for grid_id, grid in enumerate(grids):
            grid.draw(number)
            if grid.has_won():
                print("won:", grid_id, grid.score())
                print("puzzle input:", grid.score() * number)
                quit()
