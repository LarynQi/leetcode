# https://leetcode.com/problems/is-subsequence/

# https://leetcode.com/submissions/detail/291897812/
# 01/06/2020 18:17  

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for letter in s:
            if letter not in t:
                return False
            t = t[t.index(letter) + 1:]
        return True