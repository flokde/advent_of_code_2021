from math import prod

HEXA_DICT = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def interpret_packet(in_string: list) -> str:

    # Extract version and type ID.
    version = convert_binary_str_to_literal(in_string[:3])
    in_string[:] = in_string[3:]
    type_id = convert_binary_str_to_literal(in_string[:3])
    in_string[:] = in_string[3:]

    if type_id == 4:
        content = []
        while True:
            continue_cond = in_string[0]
            in_string[:] = in_string[1:]

            content += in_string[:4]
            in_string[:] = in_string[4:]

            if continue_cond == "0":
                break
        content = convert_binary_str_to_literal(content)
        return (version, type_id, content)

    else:
        sub_packets = []
        label = in_string[0]
        in_string[:] = in_string[1:]
        if label == "0":
            total_length = convert_binary_str_to_literal(in_string[:15])
            in_string[:] = in_string[15:]
            sub_string = in_string[:total_length]
            in_string[:] = in_string[total_length:]
            while sub_string:
                sub_packets.append(interpret_packet(sub_string))

        else:
            number_of_sub_packets = convert_binary_str_to_literal(in_string[:11])
            in_string[:] = in_string[11:]

            for _ in range(number_of_sub_packets):
                sub_packets.append(interpret_packet(in_string))

        return (version, type_id, sub_packets)


def convert_hexa_string_to_binary(in_str: str) -> str:
    out_str = ""
    for element in in_str:
        out_str += HEXA_DICT[element]
    return out_str


def convert_binary_str_to_literal(in_str):
    return int("".join(in_str), 2)


def sum_version_numbers(packets: tuple) -> int:
    """Docstring for sum_version_numbers
    ::
    """
    version_num_sum = packets[0]
    if packets[1] == 4:
        return version_num_sum
    else:
        return version_num_sum + sum(map(sum_version_numbers, packets[2]))


def interpret_packet_output(packet_output: tuple) -> int:
    """Docstring for interpret_package
    ::
    """
    if packet_output[1] == 4:
        return packet_output[2]

    elif packet_output[1] == 0:
        return sum(map(interpret_packet_output, packet_output[2]))

    elif packet_output[1] == 1:
        return prod(map(interpret_packet_output, packet_output[2]))

    elif packet_output[1] == 2:
        return min(map(interpret_packet_output, packet_output[2]))

    elif packet_output[1] == 3:
        return max(map(interpret_packet_output, packet_output[2]))

    elif packet_output[1] == 5:
        if interpret_packet_output(packet_output[2][0]) > interpret_packet_output(
            packet_output[2][1]
        ):
            return 1
        else:
            return 0

    elif packet_output[1] == 6:
        if interpret_packet_output(packet_output[2][0]) < interpret_packet_output(
            packet_output[2][1]
        ):
            return 1
        else:
            return 0

    elif packet_output[1] == 7:
        if interpret_packet_output(packet_output[2][0]) == interpret_packet_output(
            packet_output[2][1]
        ):
            return 1
        else:
            return 0


if __name__ == "__main__":
    with open("input", "r") as f:
        in_string = f.read()

    in_string = [x for x in convert_hexa_string_to_binary(in_string[:-1])]
    output = interpret_packet(in_string)

    print(sum_version_numbers(output))
    print(interpret_packet_output(output))
