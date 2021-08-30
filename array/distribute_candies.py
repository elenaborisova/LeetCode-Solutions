def distribute_candies(candy_type):
    max_could_eat = len(candy_type) // 2
    available_types = len(set(candy_type))

    return min(max_could_eat, available_types)


print(distribute_candies([1, 1, 2, 2, 3, 3]))
print(distribute_candies([1, 1, 2, 3]))
print(distribute_candies([6, 6, 6, 6]))
