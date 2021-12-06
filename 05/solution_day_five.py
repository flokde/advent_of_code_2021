import collections
import itertools
import re


class Board:
    """Playing board for the lines game."""
    def __init__(self, safety_threshold):
        self.node_dict = collections.defaultdict(int)
        self.safety_threshold = safety_threshold

    def update_dict(self, in_line: list, straight_lines_only=True):
        """TODO: Docstring for update_dict.

        :in_line: TODO
        :returns: TODO

        """
        x1, x2 = int(in_line[0]), int(in_line[2])
        y1, y2 = int(in_line[1]), int(in_line[3])
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        if straight_lines_only:
            assert in_line[0] == in_line[2] or in_line[1] == in_line[3]
        else:
            assert in_line[0] == in_line[2] or in_line[1] == in_line[3] or (max_x - min_x) == (max_y - min_y)

        # straight lines: (0,1) -> (0,2) -> (0,3) -> ...
        if min_x == max_x or min_y == max_y:
            list_of_nodes = list(itertools.product(range(min_x, max_x+1), range(min_y, max_y+1)))
        # diagonal lines orthogonal to (0,0) -> (1,1):
        # (0,6) -> (1,5) -> (2,4) -> ...
        elif (min_x, min_y) not in {(x1, y1), (x2, y2)}:
            list_of_nodes = [(x, y) for x, y in zip(range(min_x, max_x+1), reversed(range(min_y, max_y+1)))]

        # diagonal lines parrallel (0,0) -> (1,1):
        # (1,3) -> (2,4) -> (3,5) -> ...
        else:
            list_of_nodes = [(x, y) for x, y in zip(range(min_x, max_x+1), range(min_y, max_y+1))]

        for node in list_of_nodes:
            self.node_dict[node] += 1

    def return_safety_number(self):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        safety_number = 0
        for key in self.node_dict.keys():
            if self.node_dict[key] >= 2:
                safety_number +=1

        return safety_number


if __name__ == "__main__":
    with open('input', 'r') as file:
        in_txt = file.readlines()
        
    p = re.compile(r'\d+')
    lines = [p.findall(line) for line in in_txt]

    playing_board = Board(2)
    for line in lines:
        if line[0] == line[2] or line[1] == line[3]:
            playing_board.update_dict(in_line=line)

    playing_board_diag = Board(2)
    for line in lines:
        playing_board_diag.update_dict(in_line=line, straight_lines_only=False)

    print(playing_board.return_safety_number())
    print(playing_board_diag.return_safety_number())

