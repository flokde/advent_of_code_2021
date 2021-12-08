def decode_digit_input(list_in_strings: list):
    """Takes list of 10 digits and ouputs a dictionary to decode other, similar
    strings.

    :list_in_strings: list of strings that are encoded digits
    :returns: dictionary that maps code to proper digit. Keys are the sorted
              strings, values are the digits as int.

    """
    decoder_dict = {}
    # Filter out 1: Only entry with len == 2
    index = [i for i in range(len(list_in_strings)) if len(list_in_strings[i]) == 2][0]
    decoder_dict[1] = list_in_strings[index]
    list_in_strings.pop(index)

    # Filter out 7: Only entry wit len == 3
    index = [i for i in range(len(list_in_strings)) if len(list_in_strings[i]) == 3][0]
    decoder_dict[7] = list_in_strings[index]
    list_in_strings.pop(index)

    # Filter out 4: Only entry with len == 4
    index = [i for i in range(len(list_in_strings)) if len(list_in_strings[i]) == 4][0]
    decoder_dict[4] = list_in_strings[index]
    list_in_strings.pop(index)

    # Filter out 8: Only entry with len == 7
    index = [i for i in range(len(list_in_strings)) if len(list_in_strings[i]) == 7][0]
    decoder_dict[8] = list_in_strings[index]
    list_in_strings.pop(index)

    # Filter out 9: Only entry that contains the "4" string and len == 6
    index = [
        i
        for i in range(len(list_in_strings))
        if len(list_in_strings[i]) == 6
        and set(list_in_strings[i]) >= set(decoder_dict[4])
    ][0]
    decoder_dict[9] = list_in_strings[index]
    list_in_strings.pop(index)

    # Filter out 3: Only entry that contains "1" string and is contained in "9"
    # string and len == 5
    index = [
        i
        for i in range(len(list_in_strings))
        if len(list_in_strings[i]) == 5
        and set(list_in_strings[i]) >= set(decoder_dict[1])
        and set(list_in_strings[i]) <= set(decoder_dict[9])
    ][0]
    decoder_dict[3] = list_in_strings[index]
    list_in_strings.pop(index)

    # Filter out 5: Only entry that is contained in "9" string and len == 5
    index = [
        i
        for i in range(len(list_in_strings))
        if len(list_in_strings[i]) == 5
        and set(list_in_strings[i]) <= set(decoder_dict[9])
    ][0]
    decoder_dict[5] = list_in_strings[index]
    list_in_strings.pop(index)

    # Filter out 2 Only entry left with len == 5
    index = [i for i in range(len(list_in_strings)) if len(list_in_strings[i]) == 5][0]
    decoder_dict[2] = list_in_strings[index]
    list_in_strings.pop(index)

    # Filter out 0: Only entry left that contains "1" digit
    index = [
        i
        for i in range(len(list_in_strings))
        if set(list_in_strings[i]) >= set(decoder_dict[1])
    ][0]
    decoder_dict[0] = list_in_strings[index]
    list_in_strings.pop(index)

    # Set 6: Last remaining entry
    decoder_dict[6] = list_in_strings[0]
    list_in_strings.pop(0)
    assert not list_in_strings

    return {"".join(sorted(v)): k for k, v in decoder_dict.items()}


def decode_output_file(out_line: list, decoder_dict: dict) -> int:
    """Takes a line of output and a decoder dict to decode the output.

    :out_line: list of outout digits (one display!)
    :decoder_dict: dictionary that has sorted strings as keys and the
                   corresponding digits as values (int).
    :returns: decoded output number as int

    """
    out_number = ""
    for digit in out_line:
        out_number += str(decoder_dict["".join(sorted(digit))])

    return int(out_number)


def calculate_final_number(input_list: list, output_list: list) -> int:
    """Takes inputs to decode and then calculates the outputs.

    :input_list: list of input strings.
    :output_list: list of output strings
    :returns: final number

    """
    count = 0
    for in_line, out_line in zip(input_list, output_list):
        decoder_dict = decode_digit_input(in_line)
        count += decode_output_file(out_line, decoder_dict)

    return count


def split_input(in_string: str) -> tuple:
    """Takes input string 'ab cad ... eafb | cef ... ab
    and outputs tuple ['ab', 'cad' ... , 'eafb'], ['cef', ... , 'ab']

    :in_string: one line from input as string
    :returns: tuple (list of input strings, list of output_strings)

    """
    in_strings = [line.split("|")[0][:-1].split() for line in in_lines]
    out_strings = [line.split("|")[1][:-1].split() for line in in_lines]

    return (in_strings, out_strings)


def count_unique_digits(in_outputs: list) -> int:
    """Counts all strings that can be assigned to a digit without doubt.
    These are 1 (uses two segments), 4 (uses 4 segments), 7 (uses 3 segments)
    and 8 (uses all 7 segments)
    :in_outputs: list of strings, that correspond to outputs of displays
    :returns: number of identified digits

    """
    count = 0
    for output in in_outputs:
        count += len([digit for digit in output if len(digit) in {2, 3, 4, 7}])

    return count


if __name__ == "__main__":
    with open("input", "r") as f:
        in_lines = f.readlines()

    in_strings, out_strings = split_input(in_lines)

    print(count_unique_digits(out_strings))
    print(calculate_final_number(in_strings, out_strings))
