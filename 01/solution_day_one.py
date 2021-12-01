from numpy import loadtxt


def measure_depth_increases(input=list) -> int:
    """Takes a list and measures the number of times there is an increase
    from one element to another.

    :input: list of integers
    :returns: number of increases in the list

    """
    count = 0
    prev = None
    for depth_measure in input:
        if prev:
            if depth_measure > prev:
                count += 1
        prev = depth_measure

    return count


def measure_depth_increase_robust(input=list, step=3):
    """Takes a list and looks for the increase from point to point when
    calculating the averages over the desired subsequent entries.
    Example: list = [1, 2, 3, 2, 5, 1], step = 3
    SUM_1 = 1+2+3 = 6
    SUM_2 = 2+3+2 = 7 (increase)
    SUM_3 = 3+2+5 = 10 (increase)
    SUM_4 = 2+5+1 = 8

    :input: list of integers
    :returns: number of increases

    """

    pad = [None] * step
    padded_input = [None] * step
    count = 0
    padded_input.extend(input)
    padded_input.extend(pad)

    for i, current_el in enumerate(padded_input):
        if current_el and padded_input[i+step]:
            if current_el < padded_input[i+step]:
                count += 1

    return count


def measure_depth_increase_robust_alt(input=list, step=3):
    return sum([b > a for (a, b) in zip(input[:-step], input[step:])])


if __name__ == "__main__":
    input_array = loadtxt("input", delimiter="\n")

    print(measure_depth_increases(input_array))
    print(measure_depth_increase_robust(input_array, 3))
    print(measure_depth_increase_robust_alt(input_array, 3))
