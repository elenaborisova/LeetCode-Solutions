def wrap_string(s, n):
    result = ''
    if n <= 0:
        return s
    result += '<'
    result += wrap_string(s, n - 1)
    result += '>'

    return result


print(wrap_string('hello', 3))
