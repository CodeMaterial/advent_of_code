
def load_ints(filepath):
    data = clean_input_data(filepath)

    return [int(d) for d in data]


def clean_input_data(filepath):
    output_array = []

    with open(filepath, 'r') as data:
        for line in data:
            clean_line = line.strip().replace("  ", " ")
            if clean_line != "":
                output_array.append(clean_line)

    return output_array
