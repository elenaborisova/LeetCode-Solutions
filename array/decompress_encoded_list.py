def decompress_rle_list(nums):
    decompressed = []

    for i in range(0, len(nums), 2):
        freq = nums[i]
        val = nums[i + 1]
        current = [val for _ in range(freq)]
        decompressed.extend(current)

    return decompressed


print(decompress_rle_list([1, 2, 3, 4]))
print(decompress_rle_list([1, 1, 2, 3]))
