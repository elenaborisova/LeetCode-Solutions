"""
0. declare a variable result which is an empty array
1. loop through the array of integers
2. take a new subarray every time until we got all elements
3. compare the sum of subarray to the sum of the rest of elements
4. if the subarray sum is bigger, put the start and end indices into the result array
5. return the result

"""


def above_average_subarrays(a):
    subarrays = []
    average_total_sum = sum(a) / len(a)

    l, r = 0, 0

    while l < r:
        while r < len(a):
            subarray = a[l:r + 1]
            average_subarray_sum = sum(subarray) / len(subarray)
            average_rem_sum = average_total_sum - average_subarray_sum

            if average_subarray_sum > average_rem_sum:
                subarrays.append([l + 1, r + 1])

            r += 1

        l += 1
        r = l

    return subarrays
