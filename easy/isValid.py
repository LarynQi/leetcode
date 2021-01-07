# https://leetcode.com/problems/valid-parentheses/

# https://leetcode.com/submissions/detail/439598486/
# 01/06/2021 18:15  

class Solution:
    def isValid(self, s: str) -> bool:
        counts = 6 * [0]
        mapping = {
            "(": 0,
            ")": 1,
            "{": 2,
            "}": 3,
            "[": 4,
            "]": 5
        }
        last = []
        for c in s:
            curr = mapping[c]
            counts[curr] += 1
            if curr % 2 == 1:
                if counts[curr] > counts[curr - 1]:
                    return False
                elif mapping[c] != mapping[last[-1]] + 1:
                    return False
                last.pop()
            else:
                last.append(c)
        for i in range(0, len(counts), 2):
            j = i + 1
            if counts[i] != counts[j]:
                return False
        return True