# https://leetcode.com/problems/shortest-word-distance/

# * https://leetcode.com/submissions/detail/440251952/
# 01/08/2021 03:36  

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1 = i2 = None
        lowest = float("inf")
        for i in range(len(words)):
            curr = words[i]
            if curr != word1 and curr != word2:
                continue
            if curr == word1:
                i1 = i
                if i2 is not None:
                    lowest = min(lowest, abs(i1 - i2))
            if curr == word2:
                i2 = i
                if i1 is not None:
                    lowest = min(lowest, abs(i1 - i2))
        return lowest