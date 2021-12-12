import re
import copy


class CaveSystem:
    """"""
    def __init__(self, vertices, edges):
        self.V = vertices
        self.E = edges
        self.adj_dict = {key: [] for key in vertices}

        for e in edges:
            self.add_edge(e[0], e[1])
            self.add_edge(e[1], e[0])

    def add_edge(self, u, v):
        self.adj_dict[u].append(v)

    def count_number_of_unique_paths(self, allow_one_double=False):
        path_start = ['start']
        identified_paths = []

        if allow_one_double:
            self._recurse_helper_one_double_allowed(path_start, identified_paths)
        else:
            self._recurse_helper(path_start, identified_paths)

        return len(identified_paths), identified_paths

    def _recurse_helper(self, current_path, identified_paths):

        for cave in self.adj_dict[current_path[-1]]:
            if cave == 'end':
                current_path.append(cave)
                identified_paths.append(copy.copy(current_path))
                current_path.pop()
                continue

            if cave in current_path and cave.islower():
                continue

            current_path.append(cave)
            self._recurse_helper(current_path, identified_paths)
            current_path.pop()

    def _recurse_helper_one_double_allowed(self, current_path, identified_paths):
        for cave in self.adj_dict[current_path[-1]]:
            if cave == 'end':
                current_path.append(cave)
                # This is super hacky. Currently we get duplicate paths, which
                # this prevents. But something makes the algorithm super slow.
                # Likel if we find this bug, this won't be needed anymore.
                if current_path not in identified_paths:
                    identified_paths.append(copy.copy(current_path))
                current_path.pop()
                continue

            elif cave == 'start':
                continue

            elif cave.islower():
                lowers_in_path = [i for i in current_path if i.islower() and i not in ['start', 'end']]
                if cave not in lowers_in_path:
                    current_path.append(cave)
                    self._recurse_helper_one_double_allowed(current_path, identified_paths)
                    current_path.pop()

                if len(lowers_in_path) == len(set(lowers_in_path)):
                    current_path.append(cave)
                    self._recurse_helper_one_double_allowed(current_path, identified_paths)
                    current_path.pop()
                else:
                    continue

            else:
                current_path.append(cave)
                self._recurse_helper_one_double_allowed(current_path, identified_paths)
                current_path.pop()


if __name__ == "__main__":
    in_name = 'mini_input'
    with open(in_name, 'r') as f:
        in_lines = f.readlines()
    with open(in_name, 'r') as f:
        in_all = f.read()

    edges = [re.findall(r'[a-zA-Z]+', instruct[:-1]) for instruct in in_lines]
    vertices = set(re.findall(r'[a-zA-Z]+', in_all))

    caves = CaveSystem(vertices, edges)
    print(caves.count_number_of_unique_paths(allow_one_double=True)[0])
