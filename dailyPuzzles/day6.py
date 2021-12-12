import lib.helpers as helpers

if __name__ == "__main__":

    data = helpers.clean_input_data("../data/day6.txt")[0]

    fish_ages = [0]*9
    for f in data.split(","):
        fish_ages[int(f)] += 1

    for day in range(256):

        at_zero = fish_ages[0]

        for i in range(len(fish_ages)-1):
            fish_ages[i] = fish_ages[i+1]

        fish_ages[8] = at_zero
        fish_ages[6] += at_zero

    print("Puzzle input:", sum(fish_ages))