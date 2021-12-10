import statistics


CORRUPTION_DICT = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETION_DICT = {")": 1, "]": 2, "}": 3, ">": 4}
OPEN_CLOSE_DICT = {"(": ")", "[": "]", "{": "}", "<": ">"}


def is_input_corrupted(in_string: str) -> tuple:
    """Takes a string contain only (),[],{},<> and checks for corruption, i.e.
    if one of the closing brackets to an occurring opening bracket is 
    unfitting. It then calculates the score - the first corrupted closing
    bracket counts and has a fixed value depending on its type.

    :in_lines: String containing only (),[],{},<>
    :returns: returns a tuple of True/False value and the score, if the input
              is corrupted

    """
    check_string = ""
    for element in in_string:
        if element in {"(", "[", "{", "<"}:
            check_string += element
        elif element == OPEN_CLOSE_DICT[check_string[-1]]:
            check_string = check_string[:-1]
        else:
            return (True, CORRUPTION_DICT[element])
    return (False, None)


def calculate_corruption_score(in_lines: list) -> int:
    """Calculates the corruption score for a list of strings with the help of
    the "is_input_corrupted" function.

    :in_lines: List of strings.
    :returns: Total score, which is the sum of all individual corruption scores

    """
    score = 0
    for line in in_lines:
        corruption_check = is_input_corrupted(line)
        if corruption_check[0]:
            score += corruption_check[1]
    return score


def calculate_completion_sequence(in_string: str) -> tuple:
    """Identifies the minimal sequence necessary to complete an uncorrupted
    input. All opened brackets will get a proper closing bracket (in the right
    order. These proper closing brackets are returned along with the score.
    Score is calculated by going through identified string, multiplying by
    5 for each element and then adding a fixed value for each type of closing
    bracket.

    :in_string: String containing only (),[],{},<>.
    :returns: tuple of the completion string and its score.

    """
    check_string = ""
    for element in in_string:
        if element in {"(", "[", "{", "<"}:
            check_string += element
        elif element == OPEN_CLOSE_DICT[check_string[-1]]:
            check_string = check_string[:-1]

    score = 0
    for element in reversed(check_string):
        score *= 5
        score += COMPLETION_DICT[OPEN_CLOSE_DICT[element]]

    return (check_string, score)


def calculate_completion_score(in_lines: list) -> int:
    """Calculates the completion score for a list of strings with the help of
    the "calculate_completion_sequence" function.

    :in_lines: List of string.
    :returns: Median score of the input strings. Uneven number of incomplete,
              non-corrupted strings expected.

    """
    scores = []
    for line in in_lines:
        if not is_input_corrupted(line)[0]:
            scores.append(calculate_completion_sequence(line)[1])

    return statistics.median(scores)


if __name__ == "__main__":
    with open("input") as f:
        in_lines = [line.strip("\n") for line in f.readlines()]

    print(calculate_corruption_score(in_lines))
    print(calculate_completion_score(in_lines))
