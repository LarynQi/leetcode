# https://leetcode.com/problems/maximum-number-of-balloons/

# https://leetcode.com/submissions/detail/292013650/
# 01/07/2020 01:51  

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cache = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for letter in text:
            if letter in cache:
                if letter == "l" or letter == "o":
                    cache[letter] += 0.5
                else:
                    cache[letter] += 1
        return int(min(cache.values()))