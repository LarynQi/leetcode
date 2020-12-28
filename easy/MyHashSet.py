# https://leetcode.com/problems/design-hashset/

# https://leetcode.com/submissions/detail/275571751/
# 11/03/2019 02:26  

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}

    def add(self, key: int) -> None:
        self.cache[key] = True

    def remove(self, key: int) -> None:
        self.cache[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.cache and self.cache[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)