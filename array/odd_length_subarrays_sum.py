def sum_odd_length_subarrays(arr):
    subarrays_sum = 0

    for i in range(len(arr)):
        for j in range(i, len(arr) + 1):
            curr_subarray = arr[i:j]
            if len(curr_subarray) % 2 == 1:
                subarrays_sum += sum(curr_subarray)

    return subarrays_sum


print(sum_odd_length_subarrays([1, 4, 2, 5, 3]))
print(sum_odd_length_subarrays([1, 2]))
print(sum_odd_length_subarrays([10, 11, 12]))
