# https://leetcode.com/problems/self-dividing-numbers/

# https://leetcode.com/submissions/detail/442013410/
# 01/12/2021 03:42  

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for n in range(left, right + 1):
            curr = n
            failed = False
            while curr > 0:
                last = curr % 10
                if last == 0 or n % last != 0:
                    failed = True
                    break
                curr //= 10
            if not failed:
                result.append(n)
        return result