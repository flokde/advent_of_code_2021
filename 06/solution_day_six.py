import copy


def evolve_population_x_days(population: dict, days: int = 80) -> dict:
    """TODO: Docstring for evolve_population_x_days.

    :days: TODO
    :returns: TODO

    """
    for i in range(9):
        if i not in population.keys():
            population[i] = 0

    for day in range(days):
        new_population = {}
        # new_population = copy.deepcopy(population)
        for i in population.keys():
            # FIXME: Make this less hacky. Maybe with modulo.
            if i == 6 and 7 in population.keys():
                new_population[6] = population[7] + population[0]
            elif i == 6:
                new_population[6] = population[0]
            elif i == 8:
                new_population[8] = population[0]
            else:
                new_population[i] = population[(i+1)]
        population = new_population

    return population


if __name__ == "__main__":
    days = 256
    with open('input', 'r') as f:
        in_ages = f.read()

    fish_population = {}
    for i in range(1, 6):
        fish_population[i] = in_ages.count(str(i))

    final_fish_population = evolve_population_x_days(fish_population, days=days)
    print(sum(final_fish_population.values()))
