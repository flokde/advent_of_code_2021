def check_board_for_bingo(board):
    """TODO: Docstring for check_board for Bingo.

    :board: TODO
    :returns: TODO

    """
    for index, row in enumerate(board):
        column = [board[row_temp][index] for row_temp in range(len(board))]
        if len(row) in [row.count('X'), column.count('X')]:
            return True
    
    return False



def update_board(board, number):
    """TODO: Docstring for set_position_as_marked.

    :board: TODO
    :coord: TODO
    :returns: TODO

    """
    for row_index, row in enumerate(board):
        for element_index, element in enumerate(row):
            if element == number:
                board[row_index][element_index] = 'X'
                return board
    return board



def calculate_final_number(board):
    """TODO: Docstring for calculate_final_number.

    :board: TODO
    :last drawn_number: TODO
    :returns: TODO

    """
    score = 0
    for row_index, row in enumerate(board['winning_board']):
        for element_index, element in enumerate(row):
            if element != 'X':
                score += int(element)
    return score * int(board['last_drawn_number'])


def find_winning_board(instructs, list_boards):
    """

    :instructs: TODO
    :list_boards: TODO
    :returns: TODO

    """
    for number in instructs:
        for index, board in enumerate(list_boards):
            board = update_board(board, number)
            is_bingo = check_board_for_bingo(board)
            list_boards[index] = board
            if is_bingo:
                return {'winning_board': board, 'last_drawn_number': number}


def find_losing_board(instructs, list_boards):
    """TODO: Docstring for find_losing_board.

    :instructs: TODO
    :list_boards: TODO
    :returns: TODO

    """
    list_boards = [{'board': board, 'is_bingo': False} for board in list_boards]

    num_winning_boards = 0
    for number in instructs:
        for index, board in enumerate(list_boards):
            if not board['is_bingo']:
                board = update_board(board['board'], number)
                # list_boards[index]['board'] = board
                is_bingo = check_board_for_bingo(board)
                if is_bingo:
                    list_boards[index]['is_bingo'] = True
                    num_winning_boards += 1
                    print('called_number: ' + number)
                    print('number_of_winning_boards: '+str(num_winning_boards))
                    print(board)
                    if num_winning_boards == len(list_boards):
                        highlander = board
                        final_num = number
                        break
                    

    return {'winning_board': highlander, 'last_drawn_number': final_num}


if __name__ == "__main__":
    # input_path = 'sample_input'
    input_path = 'input'
    with open(input_path) as file:
        in_string = file.read()[:-1]

    list_boards = in_string.split('\n\n')
    instructs = list_boards[0].split(','); list_boards.pop(0)

    for index, board in enumerate(list_boards):
        intermediate_board = board.split('\n')
        list_boards[index] = [row.split() for row in intermediate_board]

    # winning_board = find_winning_board(instructs, list_boards)
    # print(calculate_final_number(winning_board))

    losing_board = find_losing_board(instructs, list_boards)
    print(calculate_final_number(losing_board))
