def is_balanced(s):
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    opening_stack = []

    for br in s:
        if br in brackets:  # br is opening
            opening_stack.append(br)
        else:  # br is closing
            if not opening_stack:
                return False

            opening_bracket = opening_stack.pop()
            if br != brackets[opening_bracket]:
                return False

    if opening_stack:
        return False
    return True


print(is_balanced('{[()]}'))
print(is_balanced('{}()'))
print(is_balanced('{(})'))
print(is_balanced(')'))
print(is_balanced('('))
