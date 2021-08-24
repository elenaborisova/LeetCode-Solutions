def shortest_to_char(s, c):
    answer = []
    c_indices = [i for i in range(len(s)) if s[i] == c]

    for i in range(len(s)):
        distance = min([abs(j - i) for j in c_indices])
        answer.append(distance)

    return answer


print(shortest_to_char('loveleetcode', 'e'))
print(shortest_to_char('aaab', 'b'))
