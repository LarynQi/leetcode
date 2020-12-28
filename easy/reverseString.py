# https://leetcode.com/problems/reverse-string/

# https://leetcode.com/submissions/detail/288753430/
# 12/26/2019 11:08  

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]