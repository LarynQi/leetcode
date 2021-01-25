# https://leetcode.com/problems/lru-cache/

# https://leetcode.com/interview/reports/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6MTUwNTI4Ng==

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, last=True)
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)