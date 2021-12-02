import lib.helpers as helpers


class Position:

    def __init__(self, x=0, y=0, aim=0):
        self.x = x
        self.y = y
        self.aim = aim

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y + other.x * self.aim, self.aim + other.aim)

    def __mul__(self, scalar):
        return Position(self.x * scalar, self.y * scalar, self.aim * scalar)


if __name__ == "__main__":

    commands = helpers.clean_input_data("../data/day2.txt")

    directionMap = {"forward": Position(1, 0), "up": Position(0, -1), "down": Position(0, 1)}
    sub_position = Position(0, 0)

    for command in commands:
        direction, distance = command.split(" ")
        sub_position += directionMap[direction] * int(distance)

    print("sub horizontal position: ", sub_position.x)
    print("sub depth: ", sub_position.y)
    print("puzzle answer (depth*horizontal position): ", sub_position.x * sub_position.y)


    directionMapWithAim = {"forward": Position(1, 0), "up": Position(0, 0, -1), "down": Position(0, 0, 1)}
    sub_position = Position(0, 0)

    for command in commands:
        direction, distance = command.split(" ")
        sub_position += directionMapWithAim[direction] * int(distance)

    print("sub horizontal position with aim: ", sub_position.x)
    print("sub depth with aim: ", sub_position.y)
    print("puzzle answer with aim (depth*horizontal position): ", sub_position.x * sub_position.y)

