def fair_candy_swap(alice_sizes, bob_sizes):
    alice_total_sum = sum(alice_sizes)
    bob_total_sum = sum(bob_sizes)

    for i in range(len(alice_sizes)):
        bob_total_sum += alice_sizes[i]

        for j in range(len(bob_sizes)):
            if bob_sizes[j] + alice_total_sum - alice_sizes[i] == bob_total_sum - bob_sizes[j]:
                return [alice_sizes[i], bob_sizes[j]]

        bob_total_sum -= alice_sizes[i]


print(fair_candy_swap([1, 1], [2, 2]))
print(fair_candy_swap([1, 2], [2, 3]))
print(fair_candy_swap([2], [1, 3]))
print(fair_candy_swap([1, 2, 5], [2, 4]))