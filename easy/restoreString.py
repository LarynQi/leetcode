# https://leetcode.com/problems/shuffle-string/

# https://leetcode.com/submissions/detail/441564707/
# 01/11/2021 03:15  

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = len(s) * [None]
        for p in zip(s, indices):
            i = p[1]
            c = p[0]
            result[i] = c
        ret = ""
        for c in result:
            ret += c
        return ret