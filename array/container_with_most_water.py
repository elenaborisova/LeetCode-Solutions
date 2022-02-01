# Time: O(n); Space: O(1)
def max_area(height):
    max_a, n = 0, len(height) - 1

    l, r = 0, n
    while l < r:

        while l < r and height[l] <= height[r]:
            max_a = max(max_a, height[l] * n)
            l += 1
            n -= 1

        while l < r and height[r] <= height[l]:
            max_a = max(max_a, height[r] * n)
            r -= 1
            n -= 1

    return max_a


# Test cases:
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area([1, 8, 6, 2, 5, 4, 8, 25, 7]))
print(max_area([1, 1]))
print(max_area([1, 3, 2, 5, 25, 24, 5]))
