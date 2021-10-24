def reorder_log_files(logs):
    digits = []
    letters = []

    for log in logs:
        if log[-1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))

    return letters + digits


print(reorder_log_files(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
print(reorder_log_files(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
print(reorder_log_files(
    ["27 85717 7", "2 y xyr fc", "52 314 99", "d 046099 0", "m azv x f", "7e apw c y", "8 hyyq z p", "6 3272401",
     "c otdk cl", "8 ksif m u"]))
