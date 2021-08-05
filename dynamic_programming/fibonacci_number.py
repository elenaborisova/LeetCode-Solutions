def fib(n):
    prev_num1 = 0
    prev_num2 = 1
    curr_num = 0

    if n == 1:
        return 1

    if n == 2:
        return 1

    for i in range(2, n+1):
        curr_num = prev_num1 + prev_num2
        prev_num1 = prev_num2
        prev_num2 = curr_num

    return curr_num


print(fib(6))
