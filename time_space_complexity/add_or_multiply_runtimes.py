def func1(a, b, A, B):
    # Time: O(2n) = O(n)
    for a in A:
        print(a)

    for b in B:
        print(b)


def func2(a, b, A, B):
    # Time: O(AxB)
    for a in A:
        for b in B:
            print(a + ', ' + b)


def func3(A, B):
    # Time: O(AxB)
    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(10000):
                print()
