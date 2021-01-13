# https://leetcode.com/problems/determine-if-string-halves-are-alike/

# https://leetcode.com/submissions/detail/442270918/
# 01/12/2021 18:35  

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        half = len(s) // 2
        s0, s1 = s[:half], s[half:]
        count0 = count1 = 0
        for c in s0:
            count0 += int(c in vowels)
        for c in s1:
            count1 += int(c in vowels)
        return count0 == count1