# https://leetcode.com/problems/first-unique-character-in-a-string/

# https://leetcode.com/submissions/detail/291880975/
# 01/06/2020 17:11  

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        cache = {}
        for i in range(len(s)):
            if s[i] in cache:
                cache[s[i]] = len(s)
            else:
                cache[s[i]] = i
        minimum = min(cache.values())
        if minimum == len(s):
            return -1
        return minimum