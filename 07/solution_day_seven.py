import numpy as np

from statistics import median


def part_one(in_list: list):
    """ Simply calculates the median of the given list of integers. Minimizing
    the absolute residuals gives us the median in this special case, so we
    don't need to loop through twice. After we sum the residuals to return
    the amount of fuel needed.
    :in_list: List of integers (in this case the horizontal position of the 
              crabs.
    :returns: number of residuals or total fuel needed.
    """
    medi = median(in_list)
    residuals = 0
    for i in in_list:
        residuals += abs(i - medi)

    return residuals

def part_two(in_list: list):
    """Finds the best position and calculates the residuals in the vase of 
    linearly increasing residuals.
    E.g. if position 4 is chosen, we get the following residuals:
        5 -> 1
        6 -> 1 + 2
        7 -> 1 + 2 + 3
        ...

    :in_list: List of integers (in this case the horizontal position of the 
              crabs.
    :returns: number of residuals or total fuel needed.
    """
    # FIXME: This has complexity O(n**2), maybe there is something more elegant
    # similar the median in part one.
    min_coord = min(in_list)
    max_coord = max(in_list)

    distance_vects = []
    for element in in_list:
        # FIXME: Clean up this line.
        distance_vects.append(np.array([(abs(x-element)**2 + abs(x-element))/2 for x in range(min_coord, max_coord + 1)]))

    cost_vector_positions = np.zeros(len(range(min_coord, max_coord +1)))
    for vect in distance_vects:
        cost_vector_positions += vect

    return min(cost_vector_positions)


if __name__ == "__main__":
    with open('input', 'r') as f:
        in_string = f.read()[:-1]
    in_list = [int(x) for x in in_string.split(',')]

    print(part_one(in_list))
    print(part_two(in_list))

