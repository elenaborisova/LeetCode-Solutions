def reverse_array(arr):
    # Time: O(n) even though we loop through half of the array
    for i in range(len(arr) // 2):
        other = len(arr) - i - 1
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp
