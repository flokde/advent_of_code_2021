def find_viable_start_values(target_range: list, x_range: list, y_range: list) -> int:
    """Docstring for find_viable_start_values
    ::
    """
    count = 0
    for x_ini in range(x_range[0], x_range[1] + 1):
        for y_ini in range(y_range[0], y_range[1] + 1):
            if check_initial_pair(target_range, x_ini, y_ini):
                count += 1

    return count


def check_initial_pair(target_range: list, x_ini: int, y_ini: int) -> bool:
    """Docstring for check_initial_pair
    ::
    """
    damp = 0
    x_pos = 0
    y_pos = 0

    while x_pos <= target_range[0][1] and y_pos >= target_range[1][0]:
        x_pos += max(0, (x_ini - damp))
        y_pos += y_ini - damp

        if (
            target_range[0][0] <= x_pos <= target_range[0][1]
            and target_range[1][0] <= y_pos <= target_range[1][1]
        ):
            return True
        damp += 1

    return False


if __name__ == "__main__":
    # FIXME: Could be nicer with reading of input
    x_range_sample = [6, 30]
    y_range_sample = [-10, 9]
    target_x_range_sample = [20, 30]
    target_y_range_sample = [-10, -5]

    target_x_range = [265, 287]
    target_y_range = [-103, -58]
    x_range = [23, 287]
    y_range = [-103, 102]

    # Part one done without code - was just Gauss formula twice.
    print(find_viable_start_values([target_x_range, target_y_range], x_range, y_range))
