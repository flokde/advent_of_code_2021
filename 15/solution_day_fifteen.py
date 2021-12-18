import copy
import math
import numpy as np


class RiskMap:
    """description"""

    def __init__(self, in_array: list):
        self.map = in_array
        self.allowed_steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        self.top_left = (0, 0)
        self.bottom_right = (len(self.map[-1]) - 1, len(self.map) - 1)

    def search_shortest_path(self, start_point: tuple = None, end_point: tuple = None):

        if not start_point:
            start_point = self.top_left
        if not end_point:
            end_point = self.bottom_right

        cost_dict = {}
        visited_dict = {}
        # Set cost to infinite as per Dijkstra algorithm.
        for jx, row in enumerate(self.map):
            for ix, element in enumerate(row):
                cost_dict[(ix, jx)] = math.inf
                visited_dict[(ix, jx)] = False

        cost_dict[start_point] = 0

        algorithm_finished = False
        queue = [(start_point)]

        while not algorithm_finished:
            self._make_dijkstra_step(cost_dict, visited_dict, queue)
            queue.sort(key=lambda x: cost_dict[x])
            if queue[0] == end_point:
                algorithm_finished = True

        return cost_dict[end_point]

    def _make_dijkstra_step(self, cost_dict: dict, visited_dict: dict, queue: list):
        current_point = queue[0]
        queue.pop(0)
        for ix, jx in self.allowed_steps:
            new_i = current_point[0] + ix
            new_j = current_point[1] + jx

            if self._is_outside_of_matrix(new_i, new_j, self.map):
                continue

            proposed_cost = cost_dict[current_point] + self.map[new_j][new_i]
            if proposed_cost < cost_dict[(new_i, new_j)]:
                cost_dict[(new_i, new_j)] = proposed_cost

            if not visited_dict[(new_i, new_j)] and (new_i, new_j) not in queue:
                queue.append((new_i, new_j))

        visited_dict[current_point] = True

    # FIXME: Don't need self here
    def _is_outside_of_matrix(self, i: int, j: int, matrix: list):
        return i < 0 or j < 0 or j > len(matrix[0]) - 1 or i > len(matrix) - 1


def increase_array_by_x(in_array: list, num_x) -> list:
    update_dict = {1: 2, 2: 3, 3:4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 1}
    for i in range(num_x):
        in_array = [[update_dict[x] for x in row] for row in in_array]

    return in_array

if __name__ == "__main__":
    with open("input", "r") as f:
        in_lines = f.readlines()

    in_array = [[int(el) for el in line[:-1]] for line in in_lines]

    in_array_np = np.array(in_array)
    in_array_np_untouched = copy.deepcopy(in_array_np)

    for index in range(1,5):
        in_array_np = np.hstack((in_array_np, increase_array_by_x(in_array_np_untouched, index)))
    in_array_np_untouched = copy.deepcopy(in_array_np)
    for index in range(1, 5):
        in_array_np = np.vstack((in_array_np, increase_array_by_x(in_array_np_untouched, index)))

    rmap = RiskMap(in_array)
    print(rmap.search_shortest_path())

    rmap_large = RiskMap(in_array_np)
    print(rmap_large.search_shortest_path())
