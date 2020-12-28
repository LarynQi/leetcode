# https://leetcode.com/problems/lru-cache/

# https://leetcode.com/submissions/detail/435333043/
# 12/27/2020 15:57

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
        return super().get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self:
            self[key] = value
            self.move_to_end(key)
        else:
            if len(self) < self.capacity:
                self[key] = value
            else:
                self.popitem(last=False)
                self[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# https://leetcode.com/submissions/detail/435108766/
# 12/27/2020 01:40
# Time Limit Exceeded
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.reorder(self.cache[key][1], True)
            self.cache[key] = [self.cache[key][0], 0]
            self.lru[0] = key
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.reorder(self.cache[key][1], True)
            self.lru[0] = key
            self.cache[key] = [value, 0]
        else:
            if len(self.lru) < self.capacity:
                self.reorder(len(self.lru) - 1, False)
                self.lru = [key] + self.lru
                self.cache[key] = [value, 0]
            else:
                self.cache.pop(self.lru.pop())
                self.reorder(len(self.lru) - 1, False)
                self.lru = [key] + self.lru
                self.cache[key] = [value, 0]

    def reorder(self, end, relabel):
        if self.lru:
            prev = self.lru[0]
            self.cache[prev][1] += 1
            for i in range(end):
                self.cache[self.lru[i + 1]][1] += 1
                curr = self.lru[i + 1]
                if relabel:
                    self.lru[i + 1] = prev
                prev = curr
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# https://leetcode.com/submissions/detail/421213630/
# 11/17/2020 01:07
# Accepted but slow

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            # i = self.lru.index(key)
            # self.lru = self.lru[:i] + self.lru[i + 1:] + [key]
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.lru.remove(key)
            self.lru.append(key)
            # i = self.lru.index(key)
            # self.lru = self.lru[:i] + self.lru[i + 1:] + [key]
        elif len(self.lru) < self.capacity:
            self.cache[key] = value
            self.lru.append(key)
        else:
            self.cache.pop(self.lru[0])
            self.cache[key] = value
            self.lru.pop(0)
            # self.lru = self.lru[1:]
            self.lru.append(key)

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)