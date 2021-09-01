class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []

    def add(self, key: int) -> None:
        if key not in self.set:
            self.set.append(key)

    def remove(self, key: int) -> None:
        if key in self.set:
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.set:
            return True
        return False

