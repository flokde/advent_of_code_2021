import pandas as pd

from math import ceil

def adjust_data_format(data):
    """

    :file_name: TODO
    :returns: TODO

    """
    # data = pd.read_csv(file_name)
    data.columns = ['bit_input']

    dat = [list(map(int, str(x).zfill(12))) for x in data.bit_input]
    d = pd.DataFrame(dat, data.index).rename(columns=lambda x: f'x{x + 1}')
    output = data.join(d)

    output.drop(columns=['bit_input'], inplace=True)
    return output

def calculate_gamme_and_eps_rate(input_dataframe):
    """TODO: Docstring for calculate_gamme_and_eps_rate.

    :arg1: TODO
    :returns: TODO

    """
    sums = input_dataframe.sum()

    bigger_bits = sums.apply(lambda x: 1 if x >= ceil(len(input_dataframe)/2) else 0)
    smaller_bits = sums.apply(lambda x: 1 if x < ceil(len(input_dataframe)/2) else 0)

    gamma_bits = ''.join(map(str, bigger_bits))
    eps_bits = ''.join(map(str, smaller_bits))

    return int(gamma_bits, 2) * int(eps_bits, 2)


def calculate_oxygen_co2_values(input_dataframe):
    """d

    :input_dataframe: TODO
    :returns: TODO

    """
    oxy_dataframe = input_dataframe
    co2_dataframe = oxy_dataframe.copy()
    for index, col in enumerate(oxy_dataframe):
        major_bit = int(oxy_dataframe[col].sum() >= ceil(len(oxy_dataframe)/2))
        oxy_dataframe = oxy_dataframe[oxy_dataframe['x'+str(index+1)] == major_bit]
        # check if we have reduced the inputs to one number
        if len(oxy_dataframe) == 1:
            break

    for index, col in enumerate(co2_dataframe):
        minor_bit = int(co2_dataframe[col].sum() < ceil(len(co2_dataframe)/2))
        co2_dataframe = co2_dataframe[co2_dataframe['x'+str(index+1)] == minor_bit]
        # check if we have reduced the inputs to one number
        if len(co2_dataframe) == 1:
            break
    
    assert len(oxy_dataframe) == 1
    assert len(co2_dataframe) == 1

    oxy_bit = ''.join(map(str, oxy_dataframe.iloc[0]))
    co2_bit = ''.join(map(str, co2_dataframe.iloc[0]))

    return int(oxy_bit, 2) * int(co2_bit, 2)


if __name__ == "__main__":
    input_data = pd.read_csv('input', header=None)
    converted_input = adjust_data_format(input_data)
    print(calculate_gamme_and_eps_rate(converted_input))
    print(calculate_oxygen_co2_values(converted_input))

    # lst = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    # converted_input = adjust_data_format(pd.DataFrame(lst))
    # print(calculate_oxygen_co2_values(converted_input))
    # print(calculate_gamme_and_eps_rate(converted_input))
