import lib.helpers as helpers


def count_increase(array_data):
    c = 0
    for d in array_data:
        c += (d > 0)

    return c


if __name__ == "__main__":
    depths = helpers.load_ints("../data/day1.txt")

    depths_count = len(depths)

    depth_deltas = [0]*depths_count

    for i in range(1, depths_count):
        depth_deltas[i] = depths[i] - depths[i-1]

    print("raw depth increases: ", count_increase(depth_deltas))

    depth_deltas_smooth = [0] * depths_count
    sliding_window = 3

    for i in range(1, depths_count):
        depth_deltas_smooth[i] = sum(depths[i:i+sliding_window]) - sum(depths[i-1:i+sliding_window-1])

    print("smooth depth increases: ", count_increase(depth_deltas_smooth))