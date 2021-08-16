def sort_by_bits(arr):
    bits = [bin(num).count('1') for num in arr]
    sorted_pairs = sorted(list(zip(bits, arr)))
    sorted_nums = [pair[1] for pair in sorted_pairs]
    return sorted_nums


print(sort_by_bits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(sort_by_bits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
print(sort_by_bits([10000, 10000]))
