def count_chars(words, chars):
    good_strs_lengths = 0

    for word in words:
        temp = chars
        for char in word:
            if char not in temp:
                break
            temp = temp.replace(char, '', 1)
        else:
            good_strs_lengths += len(word)

    return good_strs_lengths


print(count_chars(["cat", "bt", "hat", "tree"], "atach"))
print(count_chars(["hello", "world", "leetcode"], "welldonehoneyr"))
print(count_chars(["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
                   "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb", "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl",
                   "boygirdlggnh", "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
                   "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
                   "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
                   "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr",
                   "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo", "oxgaskztzroxuntiwlfyufddl",
                   "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
                   "qnagrpfzlyrouolqquytwnwnsqnmuzphne", "eeilfdaookieawrrbvtnqfzcricvhpiv",
                   "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz", "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
                   "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
                   "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo", "teyygdmmyadppuopvqdodaczob",
                   "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs",
                   "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"],
                  "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"))
