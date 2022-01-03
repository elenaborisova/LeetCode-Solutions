"""
0. create a variable - list of size N to hold the boolean values
1. loop through the queries
2. if we find a set query, set the boolean it index (value) to true;
3. if we find a get query, check the values from the right of the index (value) -> if true -> put the index of the nearest true value
"""


def answer_queries(queries, n):
    answer = [False for _ in range(n)]
    output = []

    for i in range(len(queries)):  # n
        q = queries[i]
        if q[0] == 1:  # set
            idx = q[1]
            answer[idx] = True
        elif q[0] == 2:  # get
            idx = q[1]
            for j in range(idx + 1, len(queries)):  # n
                if answer[j] is True:
                    output.append(idx)
                    break
            else:
                output.append(-1)

    return output
