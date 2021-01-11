# https://leetcode.com/problems/count-the-number-of-consistent-strings/

# https://leetcode.com/submissions/detail/441565288/
# 01/11/2021 03:18  

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for w in words:
            passed = True
            for c in w:
                if c not in allowed:
                    passed = False
                    break
            count += int(passed)
        return count
                    