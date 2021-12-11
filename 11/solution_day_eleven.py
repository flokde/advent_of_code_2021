from pprint import pprint

GRID_STEPS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def is_outside_of_matrix(i: int, j: int, matrix: list):
    return i < 0 or j < 0 or j > len(matrix[0]) - 1 or i > len(matrix) - 1


def blink_helper(i: int, j: int, octopus_map: list, blinked_this_step: set) -> None:
    """Docstring for blink_helper
    ::
    """
    octopus_map[i][j] += 1
    if (i, j) not in blinked_this_step and octopus_map[i][j] > 9:
        octopus_map[i][j] = 0
        blinked_this_step.add((i, j))
        recurse_blink(i, j, octopus_map, blinked_this_step)


def recurse_blink(i: int, j: int, octopus_map: list, blinked_this_step: set) -> list:
    """Docstring for recurse_blink
    ::
    """

    for (ix, jx) in GRID_STEPS:
        new_i = i + ix
        new_j = j + jx

        if is_outside_of_matrix(new_i, new_j, octopus_map):
            continue

        blink_helper(new_i, new_j, octopus_map, blinked_this_step)


def calculate_number_of_blinks(octopus_map, is_fixed_number_of_steps: bool = True, number_of_steps: int = 100) -> int:
    """Docstring for calculate_number_of_flashes
    ::
    """
    if not is_fixed_number_of_steps:
        number_of_steps = float('inf')

    total_blinks = 0
    all_blinked = None
    time_step = 0

    while time_step < number_of_steps:
        blinked_this_step = set({})

        for ix, row in enumerate(octopus_map):
            for jx, element in enumerate(row):
                blink_helper(ix, jx, octopus_map, blinked_this_step)

        for ix, jx in blinked_this_step:
            octopus_map[ix][jx] = 0

        total_blinks += len(blinked_this_step)
        if not all_blinked and len(blinked_this_step) == len(octopus_map) * len(octopus_map[0]):
            all_blinked = time_step + 1
            if not is_fixed_number_of_steps:
                return {'total_blinks': total_blinks, 'first_synchronized_step': all_blinked}

        time_step += 1

    return {'total_blinks': total_blinks, 'first_synchronized_step': all_blinked}


if __name__ == "__main__":
    with open("input") as f:
        in_lines = [line.strip("\n") for line in f.readlines()]

    in_lines = [[int(x) for x in line] for line in in_lines]

    print(calculate_number_of_blinks(in_lines, is_fixed_number_of_steps=False))
