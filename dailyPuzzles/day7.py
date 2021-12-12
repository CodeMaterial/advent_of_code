import lib.helpers as helpers


def dist_to_fuel_simple(crab1, crab2):
    return abs(crab1 - crab2)


def dist_to_fuel(crab1, crab2):
    dist = abs(crab1 - crab2)
    return sum(range(dist+1))


if __name__ == "__main__":

    crabs = [int(i) for i in helpers.clean_input_data("../data/day7.txt")[0].split(",")]

    fuel_simple = []
    fuel = []
    for location in range(0, max(crabs)):
        fuel_simple.append(sum([dist_to_fuel_simple(location, crab) for crab in crabs]))
        fuel.append(sum([dist_to_fuel(location, crab) for crab in crabs]))

    print("Puzzle input 1:", min(fuel_simple))
    print("Puzzle input 2:", min(fuel))