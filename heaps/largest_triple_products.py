import heapq


def find_max_product_optimized(arr):
    # Time: O(n log n)
    heap = []  # constant space as maintaining 3 elements
    result = []

    for el in arr:  # O(n)
        heapq.heappush(heap, el)  # O(log n)

        if len(heap) < 3:
            result.append(-1)
        else:
            if len(heap) > 3:
                heapq.heappop(heap)  # pops and returns the smallest element O(log n)
            result.append(heap[0] * heap[1] * heap[2])

    return result


def find_max_product2(arr):
    # Brute Force; Time: O(n)

    # When array length is 1 or 2
    if len(arr) < 3:
        for i in range(len(arr)):
            arr[i] = -1
        return arr

    # When array length is 3 or more
    three_largest_elem = arr[:3]
    result = []

    for i in range(2):
        result.append(-1)

    product = three_largest_elem[0] * three_largest_elem[1] * three_largest_elem[2]
    result.append(product)

    for i in range(3, len(arr)):  # O(n)
        three_largest_elem.append(arr[i])
        three_largest_elem.sort()  # O(1) as we always sort fixed number of elements (4)
        three_largest_elem = three_largest_elem[1:4]

        product = three_largest_elem[0] * three_largest_elem[1] * three_largest_elem[2]
        result.append(product)

    return result


def find_max_product1(arr):
    # Brute Force; Time: O(n * n log n)
    elements = []
    result = []

    for i, n in enumerate(arr):  # n
        elements.append(n)

        if i < 2:
            result.append(-1)
        else:
            elements.sort(reverse=True)  # n log n
            product = elements[0] * elements[1] * elements[2]
            result.append(product)

    return result


# Test cases:
print(find_max_product_optimized([1, 2, 3, 4, 5]) == [-1, -1, 6, 24, 60])
print(find_max_product_optimized([2, 1, 2, 1, 2]) == [-1, -1, 4, 4, 8])
print(find_max_product_optimized([2, 4, 7, 1, 5, 3]) == [-1, -1, 56, 56, 140, 140])
print(find_max_product_optimized([999, 999, 12, 2]) == [-1, -1, 11976012, 11976012])
print(find_max_product_optimized([743, 286, 480, 949, 320, 488]) == [-1, -1, 101999040, 338451360, 338451360, 344092216])
print(find_max_product_optimized([633, 595, 586, 465, 141, 232]) == [-1, -1, 220708110, 220708110, 220708110, 220708110])
print(find_max_product_optimized([30, 39, 97, 1, 79, 52]) == [-1, -1, 113490, 113490, 298857, 398476])
print(find_max_product_optimized([13, 9, 12, 20, 19, 16]) == [-1, -1, 1404, 3120, 4940, 6080])
