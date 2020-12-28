# https://leetcode.com/problems/longest-common-subsequence/

# https://leetcode.com/submissions/detail/434224336/
# 12/24/2020 15:51  
# Time Limit Exceeded

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        if text1[0] == text2[0]:
            return max(1 + self.longestCommonSubsequence(text1[1:], text2[1:]), self.longestCommonSubsequence(text1[1:], text2[:]), self.longestCommonSubsequence(text1[:], text2[1:]))
        return max(self.longestCommonSubsequence(text1[1:], text2[:]), self.longestCommonSubsequence(text1[:], text2[1:]))