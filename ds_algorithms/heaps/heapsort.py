from ds_algorithms.heaps.max_heap import MaxHeap


def heapsort(lst):
    # Time: O(n log n)
    sort = []
    max_heap = MaxHeap()
    for idx in lst:
        max_heap.add(idx)

    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.insert(0, max_value)

    return sort


my_list = [22, 21, 61, 13, 10, 23, 99]
sorted_list = heapsort(my_list)
