import numpy as np

STEPS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


def interpret_pixel(in_matrix, i, j) -> int:
    binary_code = ""
    for ix, jx in STEPS:
        new_i = i + ix
        new_j = j + jx
        binary_code += str(int(in_matrix[new_i][new_j]))

    return DICT_STRING[int(binary_code, 2)]


def enhance_pic(in_matrix: list, background: int) -> list:
    """Docstring for enhance_pic_n_times
    ::
    """

    padded_matrix = np.pad(
        in_matrix,
        [(2, 2), (2, 2)],
        "constant",
        constant_values=(background, background),
    )
    out_matrix = np.zeros(padded_matrix.shape)

    for ix, row in enumerate(padded_matrix[1:-1]):
        for jx, element in enumerate(row[1:-1]):
            out_matrix[ix + 1][jx + 1] = interpret_pixel(padded_matrix, ix + 1, jx + 1)

    out_matrix[-1, :] = abs(1 - background)
    out_matrix[:, -1] = abs(1 - background)

    return out_matrix


if __name__ == "__main__":
    num_enhancements = 50
    with open("input", "r") as f:
        in_lines = f.readlines()

    DICT_STRING = [1 if element == "#" else 0 for element in in_lines[0][:-1]]
    in_matrix = [
        [1 if element == "#" else 0 for element in row[:-1]] for row in in_lines[2:]
    ]

    if DICT_STRING[0] == 1 and DICT_STRING[-1] == 0:
        blinkin_on = True
    else:
        blinkin_on = False

    background = 0

    for _ in range(num_enhancements):
        in_matrix = enhance_pic(in_matrix, background)
        if blinkin_on:
            background = abs(background - 1)

    print(np.sum(in_matrix))
