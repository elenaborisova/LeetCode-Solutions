def count_subarrays(arr):
    subarrays_count = []

    for i in range(len(arr)):
        current_subarray = [arr[i]]

        j = i - 1
        while j >= 0 and arr[j] < arr[i]:
            current_subarray.append(arr[j:i + 1])
            j -= 1

        j = i + 1
        while j < len(arr) and arr[j] < arr[i]:
            current_subarray.append(arr[i:j + 1])
            j += 1

        subarrays_count.append(len(current_subarray))

    return subarrays_count


def count_subarrays2(arr):
    n = len(arr)
    res = [1] * n
    stack = [-1]
    # left
    for i in range(n):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        res[i] += i - stack[-1] - 1
        stack.append(i)

    # from right
    stack = [n]
    for i in range(n - 1, -1, -1):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        res[i] += stack[-1] - i - 1
        stack.append(i)
    return res


print(count_subarrays2([3, 4, 1, 6, 2]))
print(count_subarrays([2, 4, 7, 1, 5, 3]))
print(count_subarrays([3, 2, 5, 4, 9, 6, 8]))
