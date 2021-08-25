def cal_points(ops):
    score = []

    for op in ops:
        if op == '+':
            score.append(score[-1] + score[-2])
        elif op == 'D':
            score.append(score[-1] * 2)
        elif op == 'C':
            score.pop()
        else:
            score.append(int(op))

    return sum(score)


print(cal_points(["5", "2", "C", "D", "+"]))
print(cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(cal_points(["1"]))
