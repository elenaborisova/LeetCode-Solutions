def last_stone_weight(stones):
    while len(stones) > 1:
        stones.sort()
        if stones[-1] == stones[-2]:
            stones.pop()
            stones.pop()
        else:
            last = stones.pop(-2)
            stones[-1] -= last

    return stones[0] if stones else 0


print(last_stone_weight([2, 7, 4, 1, 8, 1]))
print(last_stone_weight([1]))
