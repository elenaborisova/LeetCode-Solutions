def div(a, b):
    count = 0
    total_sum = b

    while total_sum <= a:
        total_sum += b
        count += 1

    return count
