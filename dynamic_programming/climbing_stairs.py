def climb_stairs(n):
        n1 = 0
        n2 = 1

        if n == n1 or n == n2:
            return n

        for i in range(n):
            nums_sum = n1 + n2
            n1 = n2
            n2 = nums_sum

        return n2


print(climb_stairs(5))
