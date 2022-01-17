class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.is_end = True

    def search(self, word):
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.is_end

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
d = WordDictionary()
d.addWord("bad")
d.addWord("dad")
d.addWord("mad")
print(d.search("pad"))
print(d.search("bad"))
print(d.search(".ad"))
print(d.search("b.."))
