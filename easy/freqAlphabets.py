# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

# https://leetcode.com/submissions/detail/442256001/
# 01/12/2021 17:51  

class Solution:
    def freqAlphabets(self, s: str) -> str:
        s = s.split("#")
        result = ""
        n = len(s)
        for i in range(n):
            c = s[i]
            if i == n - 1 and "#" not in c:
                for ch in c:
                    result += chr(int(ch) + 96)
            else:
                while len(c) >= 3:
                    result += chr(int(c[0]) + 96)
                    c = c[1:]
                result += chr(int(c[:2]) + 96)
        return result