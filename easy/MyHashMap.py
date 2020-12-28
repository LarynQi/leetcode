# https://leetcode.com/problems/design-hashmap/

# https://leetcode.com/submissions/detail/269409251/
# 10/12/2019 22:41  
# Time Limit Exceeded

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = []
        self.values = []
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.remove(key)
        self.keys += [key]
        self.values += [value]
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = len(self.keys) - 1
        while i >= 0:
            if self.keys[i] == key:
                return self.values[i]
            i -= 1
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        copy = self.keys[:]
        for i in range(len(copy)):
            if copy[i] == key:
                self.keys[i] = None
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)