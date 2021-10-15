def maximum_population(logs):
    years_population = {}

    for person in range(len(logs)):
        birth = logs[person][0]
        death = logs[person][1]

        for year in range(birth, death):
            if year not in years_population:
                years_population[year] = 0
            years_population[year] += 1

    print(years_population)

    max_population = max(years_population.values())
    earliest_year = min([year for year, pop in years_population.items() if pop == max_population])

    return earliest_year


print(maximum_population([[1993, 1999], [2000, 2010]]))
print(maximum_population([[1950, 1961], [1960, 1971], [1970, 1981]]))
print(maximum_population([[1982, 1998], [2013, 2042], [2010, 2035], [2022, 2050], [2047, 2048]]))
