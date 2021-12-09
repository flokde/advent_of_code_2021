import numpy as np
import scipy.ndimage


def is_outside_of_matrix(i: int, j: int, matrix: list):
    return i < 0 or j < 0 or j > len(matrix[0]) - 1 or i > len(matrix) - 1


# FIXME: The visited_positions is not really necessary here, I think.
def recurse_check_neighbors(
    i: int, j: int, in_landscape: list, basin: dict, visited_positions: dict
):
    """Recursively checks the neighbors of a position if they fulfill the 
    conditions of belonging to the same basin. Doing this recursively gives
    all positions that belong to the same basin as the starting position.

    :i: i position (which row) of starting position.
    :j: j position (which column) of starting position.
    :in_landscape: the terrain in which the starting position is located.
    :basin: basin (dict), only filled with the starting position.
    :visited_positions: Dictionary of  previously visited positions in the
                        basin search.
    :returns: The basin filled with all position {(i, j): x} that were
              identified during the recursive search.

    """
    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for (ix, jx) in steps:
        new_i = i + ix
        new_j = j + jx

        if (
            is_outside_of_matrix(new_i, new_j, in_landscape)
            or (new_i, new_j) in visited_positions.keys()
        ):
            continue

        neigh = in_landscape[new_i][new_j]
        visited_positions[(new_i, new_j)] = neigh
        if neigh != 9:
            basin[(new_i, new_j)] = neigh
            recurse_check_neighbors(new_i, new_j, in_landscape, basin, visited_positions)

    return basin


def find_basins(terrain_map: list) -> dict:
    """Finds all basins in a terrain. A basin is a number of connected 
    positions, which are not equal to 9. The connections are only horizontal
    or vertical, but not diagonally. Therefore every non-9 position will
    belong to exactly one basin.

    :terrain_map: 2D array that is a map of the terrain.
    :returns: list of all basins. 

    """
    visited_positions = {}
    all_basins = []

    for ix, row in enumerate(terrain_map):
        for jx, entry in enumerate(row):
            if entry != 9 and (ix, jx) not in visited_positions:
                new_basin = {(ix, jx): entry}
                visited_positions[(ix, jx)] = entry
                finished_basin = recurse_check_neighbors(
                    ix, jx, terrain_map, new_basin, visited_positions
                )
                all_basins.append(finished_basin)

    return all_basins

def calculate_basin_number(basin_list: list) -> int:
    """Given an input list of basins [{(i1, j1): 4, (i2, j2): 6}, ...] this
    finds the three biggest basins and calculates the product of their sizes.

    :basin_list: list of basins as described above.
    :returns: Final product of the sizes of the three biggest basins.

    """
    sizes_basins = [len(x) for x in basin_list]
    sizes_basins.sort()
    return sizes_basins[-1] * sizes_basins[-2] * sizes_basins[-3]
    


def calculate_risk_number(in_array: np.array, risk_value: int = 1) -> int:
    """Calculates the risk number of a terrain, which is the sum of values at
    local minima plus the risk value for each local minimum.

    :risk_value: risk value per low_point. This value is added on top of each
                 low point value.
    :returns: Total risk value. E.g. if low point values are
                 1, 3, 5 and risk_value is 1: 
                 total risk = (1 + 1) + (3 + 1) + (5 + 1)
    """
    # Set filter, for where to look (up, down, left, right)
    min_filter = np.asarray([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

    # Apply filter to every entry in the matrix and find minimum in filter.
    # Then compare to actual entry to find local minima.
    identified_positions = in_array < scipy.ndimage.minimum_filter(
        in_array, footprint=min_filter, mode="constant", cval=9
    )

    return sum(in_array[identified_positions]) + len(in_array[identified_positions])


if __name__ == "__main__":
    with open("input", "r") as f:
        input_string = f.readlines()

    innmatrix = [x[:-1] for x in input_string]
    in_array = [[int(x) for x in y] for y in innmatrix]
    in_array_np = np.asarray([[int(x) for x in y] for y in innmatrix])

    print(calculate_risk_number(in_array_np))
    all_basins = find_basins(in_array)
    print(calculate_basin_number(all_basins))
