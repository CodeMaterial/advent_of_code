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

    print("gamma value in decimal: %i" % int(gamma_bits, 2))
    print("epsilon value in decimal: %i" % int(epsilon_bits, 2))
    print("Puzzle input (episilon * gamma): %i" % (int(gamma_bits, 2) * int(epsilon_bits, 2)))

    # part 2

    for rating in ["oxygen", "CO2"]:

        # Initialise an array depicting which values in the data are valid and which aren't
        valid_bytes = [True]*len(data)

        # Loop over all bits
        for bit_index in range(byte_length):

            # Sum all valid bits in said bit position
            bit_count = 0
            for value_index, value in enumerate(data):
                bit_count += int(value[bit_index]) * valid_bytes[value_index]

            # Create a filter based on whether the bit sum is above or below the average
            bit_filter = bit_count >= sum(valid_bytes)/2 if rating == "oxygen" else bit_count < sum(valid_bytes)/2

            # Invalidate any data that doesn't match the above filter
            for value_index, value in enumerate(data):
                if value[bit_index] != str(int(bit_filter)):
                    valid_bytes[value_index] = False

            # If there is only 1 valid byte remaining, we've found our solution
            if sum(valid_bytes) == 1:
                valid_byte = data[valid_bytes.index(True)]
                print("%s value in decimal: %i" % (rating, int(valid_byte, 2)))
                break
