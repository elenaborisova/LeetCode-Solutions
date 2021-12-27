import math
import heapq


def max_candies_optimized(arr, k):
    heap = [-1 * n for n in arr]
    heapq.heapify(heap)  # O(n)
    candies_count = 0

    while k:
        max_bag = heapq.heappop(heap) * -1  # will return the negative largest element
        candies_count += max_bag

        max_bag = math.floor(max_bag / 2)
        heapq.heappush(heap, max_bag * -1)

        k -= 1

    return candies_count


def max_candies(arr, k):
    # Brute Force; Time: O(k * n log n)
    arr.sort()
    candies_count = 0

    while k:
        max_bag = arr.pop()
        candies_count += max_bag

        max_bag = math.floor(max_bag / 2)
        arr.append(max_bag)
        arr.sort()

        k -= 1

    return candies_count


# Test cases:
print(max_candies_optimized([2, 1, 7, 4, 2], 3) == 14)
print(max_candies_optimized([19, 78, 76, 72, 48, 8, 24, 74, 29], 3) == 228)
print(max_candies_optimized([136120699, 675464321, 262606628, 78381914, 845538549], 2093) == 3996224157)
print(max_candies_optimized([11691841, 657719590, 998119095, 278602549, 6255378], 1816) == 3904776838)
print(max_candies_optimized([965689668, 37220003, 58396314, 217381081, 266833901], 1364) == 3091041852)
print(max_candies_optimized([596304821, 123652827, 498688039, 57140046, 858215077], 1123) == 4268001540)
print(max_candies_optimized([549953320, 939734274, 901266109, 547850345, 487898284], 2327) == 6853404595)
print(max_candies_optimized([708051013, 465222651, 537415105, 839647354, 902604158], 3703) == 6905880494)
print(max_candies_optimized([293570508, 696546977, 513671040, 808133416, 283191606], 7706) == 5190227023)
print(max_candies_optimized([56947285, 6178719, 895542109, 956643976, 291045423], 7965) == 4412714956)
print(max_candies_optimized([677396178, 969219274, 63310084, 357059777, 522773324], 7778) == 5179517211)
print(max_candies_optimized([979474204, 324566924, 545391644, 933162372, 513560358], 409) == 6592310932)
