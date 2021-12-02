import pandas as pd
from numpy import loadtxt


def calculate_position(initial_position=tuple, navigation_input=list):
    """Calculates the final position after navigation instructions and outputs
    product of depth and forward position.

    :initial_position: initial position as tuple (x, y)
    :navigation_input: pandas dataframe with two columns direction and
                       magnitude
    :returns: product of final x and y coordinate

    """
    direction, magnitude = navigation_input.columns

    total_magnitudes = navigation_input.groupby("direction")["magnitude"].sum()

    return (total_magnitudes["down"] - total_magnitudes["up"]) * total_magnitudes["forward"]


def calculate_position_aim(initial_position: tuple, navigation_input: list):
    """Calculates the final position after navigation instructions and outputs
    product of depth and forward position.

    :initial_position: initial position as tuple (x, y, z), where z is the
                       aim.
    :navigation_input: pandas dataframe with two columns direction and
                       magnitude.
    :returns: product of final x and y coordinate

    """
    current_position = {
        "horizontal": initial_position[0],
        "depth": initial_position[1],
        "aim": initial_position[2],
    }

    for index, row in navigation_input.iterrows():
        direction, magnitude = row
        if direction == "down":
            current_position["aim"] += magnitude
        elif direction == "up":
            current_position["aim"] -= magnitude
        else:
            current_position["horizontal"] += magnitude
            current_position["depth"] += magnitude * current_position["aim"]

    return current_position["horizontal"] * current_position["depth"]


if __name__ == "__main__":
    input_data = pd.read_csv("input", sep=" ", header=None)
    input_data.columns = ["direction", "magnitude"]

    print(calculate_position(initial_position=(0, 0), navigation_input=input_data))
    print(calculate_position_aim(initial_position=(0, 0, 0), navigation_input=input_data))
