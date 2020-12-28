# https://leetcode.com/problems/roman-to-integer/

# https://leetcode.com/submissions/detail/268610231/
# 10/10/2019 02:45

class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        sym = 0
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while sym < len(s):
            if sym + 1 < len(s):
                if s[sym] == 'I' and s[sym + 1] == 'V':
                    value += 4
                    sym += 2
                elif s[sym] == 'I' and s[sym + 1] == 'X':
                    value += 9
                    sym += 2
                elif s[sym] == 'X' and s[sym + 1] == 'L':
                    value += 40
                    sym += 2
                elif s[sym] == 'X' and s[sym + 1] == 'C':
                    value += 90
                    sym += 2
                elif s[sym] == 'C' and s[sym + 1] == 'D':
                    value += 400
                    sym += 2
                elif s[sym] == 'C' and s[sym + 1] == 'M':
                    value += 900
                    sym += 2
                else:
                    value += values[s[sym]]
                    sym += 1
            else:
                value += values[s[sym]]
                sym += 1
        return value