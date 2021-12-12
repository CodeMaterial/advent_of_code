import lib.helpers as helpers


class Point:

    def __init__(self, xy):
        self.x = int(xy[0])
        self.y = int(xy[1])

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))


class Line:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_diagonal(self):
        return self.start.x != self.end.x and self.start.y != self.end.y

    def interpolate(self):

        step = Point((0, 0))

        if self.start.x != self.end.x:
            step.x = 1 if self.end.x > self.start.x else -1

        if self.start.y != self.end.y:
            step.y = 1 if self.end.y > self.start.y else -1

        p = self.start

        yield p

        while p != self.end:
            p += step
            yield p


class Grid:

    def __init__(self, width, height):
        self.data = []
        self.overlaps = 0
        self.reset(width, height)

    def reset(self, width, height):
        self.data = [[0] * width for h in range(height)]
        self.overlaps = 0

    def increment(self, point):
        self.data[point.y][point.x] += 1

        if self.data[point.y][point.x] == 2:
            self.overlaps += 1


if __name__ == "__main__":

    data = helpers.clean_input_data("../data/day5.txt")

    lines = []

    for d in data:
        start, end = d.split(" -> ")
        start_point = Point(start.split(','))
        end_point = Point(end.split(','))
        lines.append(Line(start_point, end_point))

    grid = Grid(1000, 1000)

    for line in lines:
        if line.is_diagonal():
            continue
        for point in line.interpolate():
            grid.increment(point)

    print("Puzzle input 1: %i" % grid.overlaps)

    grid.reset(1000, 1000)

    for line in lines:
        for point in line.interpolate():
            grid.increment(point)

    print("Puzzle input 2: %i" % grid.overlaps)
