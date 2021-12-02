import lib.helpers as helpers


def count_positive(array_data):
    return sum(d > 0 for d in array_data)


if __name__ == "__main__":
    depths = helpers.load_ints("../data/day1.txt")

    depths_count = len(depths)

    depth_deltas = [0]*depths_count

    for i in range(1, depths_count):
        depth_deltas[i] = depths[i] - depths[i-1]

    print("raw depth increases: ", count_positive(depth_deltas))

    depth_deltas_smooth = [0] * depths_count
    sliding_window = 3

    for i in range(1, depths_count):
        depth_deltas_smooth[i] = sum(depths[i:i+sliding_window]) - sum(depths[i-1:i+sliding_window-1])

    print("smooth depth increases: ", count_positive(depth_deltas_smooth))