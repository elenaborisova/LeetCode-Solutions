def func1(a, b, A, B):
    # Time: O(2n)
    for a in A:
        print(a)

    for b in B:
        print(b)


def func2(a, b, A, B):
    # Time: O(n*n)
    for a in A:
        for b in B:
            print(a + ', ' + b)
