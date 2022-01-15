class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Time: O(m); Space: O(m) where m is the length of word
    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True

    def get_longest_prefix(self, number):
        cur = self.root
        longest = ''

        for c in number:
            if c not in cur.children:
                return longest
            longest += c
            cur = cur.children[c]

        return longest


def get_longest_prefixes(numbers, prefixes):
    trie = Trie()
    for prefix in prefixes:
        trie.insert(prefix)

    res = []
    for num in numbers:
        longest_prefix = trie.get_longest_prefix(num)
        res.append(longest_prefix)

    return res


# Test cases:
phone_numbers = ['21349049', '1204539492', '123490485904']
prefixes = ['213', '21358', '1234', '12']

print(get_longest_prefixes(phone_numbers, prefixes))
