# https://leetcode.com/problems/longest-palindromic-substring/

# https://leetcode.com/submissions/detail/436149913/
# 12/29/2020 14:33  
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 45 min in
        # Brute Force
        def isPalindrome(s):
            if len(s) % 2 == 0:
                return s[:len(s) // 2] == s[len(s) // 2:][::-1]
            return s[:len(s) // 2] == s[(len(s) // 2) + 1:][::-1]
        best = ""
        for i in range(len(s)):
            if len(best) > len(s) - i:
                break
            curr = s[i:]
            while not isPalindrome(curr) and len(curr) > len(best):
                curr = curr[:-1]
            if len(curr) > len(best):
                best = curr
        return best

# earlier
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 30 min in
        # Brute Force
        def isPalindrome(s):
            print(s)
            if len(s) % 2 == 0:
                return s[:len(s) // 2] == s[len(s) // 2:][::-1]
            return s[:len(s) // 2] == s[(len(s) // 2) + 1:][::-1]
        best = ""
        for i in range(len(s)):
            curr = s[i]
            count = 1
            last = False
            while isPalindrome(curr):
                curr = s[i:i + count]
                if i + count >= len(s[i:]):
                    if isPalindrome(curr):
                        last = True
                    break
                count += 1
            if last:
                if len(curr) > len(best):
                    best = curr
            elif len(curr) - 1 > len(best):
                best = curr[:-1]
        return best

def isPalindrome(s):
    if len(s) % 2 == 0:
        return s[:len(s) // 2] == s[len(s) // 2:][::-1]
    return s[:len(s) // 2] == s[(len(s) // 2) + 1:][::-1]