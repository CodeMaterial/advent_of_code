import lib.helpers as helpers


if __name__ == "__main__":
    data = helpers.clean_input_data("../data/day3.txt")

    byte_length = len(data[0])

    average = [0]*byte_length

    for byte in data:
        for bit_index in range(byte_length):
            average[bit_index] += float(byte[bit_index])/len(data)

    gamma_bits =   ''.join([str(round(a)) for a in average])
    epsilon_bits = ''.join([str(1-round(a)) for a in average])

    print("gamma value in decimal: ", int(gamma_bits, 2))
    print("epsilon value in decimal: ", int(epsilon_bits, 2))
    print("Puzzle input (episilon * gamma): ", int(gamma_bits, 2) * int(epsilon_bits, 2))