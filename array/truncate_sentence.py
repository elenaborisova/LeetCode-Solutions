def truncate_sentence(s, k):
    return ' '.join(s.split()[:k])


print(truncate_sentence('Hello how are you Contestant', 4))
print(truncate_sentence('What is the solution to this problem', 4))
