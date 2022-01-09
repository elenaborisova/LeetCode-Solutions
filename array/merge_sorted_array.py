# Time: O(m + n); Space: O(1)
def merge(nums1, m, nums2, n):
    while m and n:
        if nums1[m - 1] < nums2[n - 1]:
            nums1[(m + n) - 1] = nums2[n - 1]
            n -= 1
        else:
            nums1[(m + n) - 1] = nums1[m - 1]
            m -= 1

    if n > 0:
        nums1[:n] = nums2[:n]

    return nums1


# Test cases:
print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6])
print(merge(nums1=[1], m=1, nums2=[], n=0) == [1])
print(merge(nums1=[0], m=0, nums2=[1], n=1) == [1])
