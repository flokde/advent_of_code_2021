import re


class CaveMap:
    def __init__(self, dots):
        self.dots = dots

    def perform_fold(self, fold_instruct) -> None:
        dimension, position = fold_instruct
        if dimension == 'x':
            self._perform_x_fold(position)
        elif dimension == 'y':
            self._perform_y_fold(position)
        else:
            raise ValueError("Only x and y folds supported")

    #FIXME: x, y fold don't need to be separate methods, one fold method
    # would suffice.
    def _perform_x_fold(self, x_position) -> None:
        new_dots = []
        for dot in self.dots: 
            if dot[0] < x_position:
                new_dots.append(dot)
            else:
                folded_dot = (x_position - (dot[0] - x_position), dot[1])
                new_dots.append(folded_dot)

        self.dots = list(set(new_dots))

    def _perform_y_fold(self, y_position) -> None:
        new_dots = []
        for dot in self.dots: 
            if dot[1] < y_position:
                new_dots.append(dot)
            else:
                folded_dot = (dot[0], y_position - (dot[1] - y_position))
                new_dots.append(folded_dot)

        self.dots = list(set(new_dots))

    def print_map(self) -> None:
        out_string = ''
        max_x = max([dot[0] for dot in self.dots])
        max_y = max([dot[1] for dot in self.dots])

        for jx in range(max_y + 1):
            for ix in range(max_x + 1):
                if (ix, jx) in self.dots:
                    out_string += ('#')
                else:
                    out_string += (' ')
            out_string += ('\n')
        print(out_string)


if __name__ == "__main__":
    with open('input', 'r') as f:
        in_lines = f.readlines()

    dots = []
    folding_instr = []

    for index, element in enumerate(in_lines):
        if element != '\n':
            match = re.findall(r'\d+', element)
            dots.append((int(match[0]), int(match[1])))
        else:
            break

    for element in in_lines[index+1:]:
        match = re.search(r'([x,y])=(\d+)$', element)
        folding_instr.append((match.groups()[0], int(match.groups()[1])))

    cmap = CaveMap(dots)
    for index, fold in enumerate(folding_instr):
        cmap.perform_fold(fold)
        if index == 0:
            print(len(cmap.dots))

    cmap.print_map()
