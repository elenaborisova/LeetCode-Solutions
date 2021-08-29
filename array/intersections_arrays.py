def intersection(nums1, nums2):
    smaller = nums1 if len(nums2) > len(nums1) else nums2
    bigger = nums2 if len(nums2) > len(nums1) else nums1
    inters = set()

    for i in range(len(smaller)):
        if smaller[i] in bigger:
            inters.add(smaller[i])

    return list(inters)


print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
