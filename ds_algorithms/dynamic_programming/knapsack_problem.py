# Time complexity: O(2 ^ n)
def recursive_knapsack(weight_cap, weights, values, i):
    if weight_cap == 0 or i == 0:
        return 0
    elif weights[i - 1] > weight_cap:
        return recursive_knapsack(weight_cap, weights, values, i - 1)
    else:
        include_item = values[i - 1] + recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1)

        exclude_item = recursive_knapsack(weight_cap, weights, values, i - 1)

        return max(include_item, exclude_item)


# Time complexity: O(n * weight_cap)
def dynamic_knapsack(weight_cap, weights, values):
    rows = len(weights) + 1
    cols = weight_cap + 1
    matrix = [[] for _ in range(rows)]

    for index in range(rows):
        # Initialize columns for this row
        matrix[index] = [-1 for _ in range(cols)]

        for weight in range(cols):
            if index == 0 or weight == 0:
                matrix[index][weight] = 0
            # If weight at previous row is less than or equal to current weight
            elif weights[index - 1] <= weight:
                # Calculate item to include
                include_item = values[index - 1] + matrix[index - 1][weight - weights[index - 1]]

                # Calculate item to exclude
                exclude_item = matrix[index - 1][weight]

                # Calculate the value of current cell
                matrix[index][weight] = max(include_item, exclude_item)
            else:
                # Calculate the value of current cell
                matrix[index][weight] = matrix[index - 1][weight]
    # Return the value of the bottom right of matrix
    return matrix[rows - 1][weight_cap]


weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(dynamic_knapsack(weight_cap, weights, values))

weight_cap = 5
weights = [1, 3, 5]
values = [250, 300, 500]
i = len(values) - 1
print(recursive_knapsack(weight_cap, weights, values, i))
