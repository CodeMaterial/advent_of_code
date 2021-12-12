import lib.helpers as helpers

if __name__ == "__main__":

    data = helpers.clean_input_data("../data/day6.txt")[0].split(",")

    fish_ages = [data.count(str(age)) for age in range(9)]

    for day in range(256):

        fish_ages.append(fish_ages[0])

        fish_ages = fish_ages[1:]

        fish_ages[6] += fish_ages[8]

    print("Puzzle input:", sum(fish_ages))