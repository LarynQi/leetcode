# https://leetcode.com/problems/longest-palindromic-substring/

# https://leetcode.com/submissions/detail/446925091/
# 01/23/2021 16:30  

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ### Solution ###
        if not s:
            return ""
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        start = stop = 0
        for i in range(len(s)):
            odd = helper(s, i, i)
            even = helper(s, i, i + 1)
            best = max(odd, even)
            if best > stop - start:
                start = i - ((best - 1) // 2)
                stop = i + best // 2
            

        return s[start:stop + 1]
        ### Naive ###
        # seen = {}
        # def is_palindrome(s):
        #     if not s or len(s) == 1:
        #         seen[s] = True
        #         return True
        #     left = s[0]
        #     right = s[-1]
        #     middle = s[1:-1]
        #     if middle in seen:
        #         if seen[middle]:
        #             if left == right:
        #                 seen[s] = True
        #                 return True
        #             else:
        #                 seen[s] = False
        #                 return False
        #         else:
        #             seen[s] = False
        #             return False
        #     else:
        #         if left == right:
        #             result = is_palindrome(middle)
        #             seen[s] = result
        #             return result
        #         else:
        #             seen[s] = False
        #             return False
        # if is_palindrome(s):
        #     return s
        # longest = 0
        # best = ""
        # for i in range(len(s)):
        #     for j in range(i + 1, len(s) + 1):
        #         curr = s[i:j]
        #         if is_palindrome(curr):
        #             if len(curr) > longest:
        #                 longest = len(curr)
        #                 best = curr
        # return best

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