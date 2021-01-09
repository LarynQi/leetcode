# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# https://leetcode.com/submissions/detail/440528892/
# 01/08/2021 19:59  

class Solution:
    def removeDuplicates(self, S: str) -> str:
        result = ""
        prev = None
        for c in S:
            # print(result)
            if prev is None:
                prev = c
                result += c
            else:
                if prev == c:
                    result = result[:-1]
                    prev = result[-1] if result else None
                else:
                    prev = c
                    result += c
        return result
            