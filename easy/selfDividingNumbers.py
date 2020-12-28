# https://leetcode.com/problems/self-dividing-numbers/

# https://leetcode.com/submissions/detail/268994464/
# 10/11/2019 12:57  

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst = []
        while left <= right:
            num = left
            while num > 0:
                if num % 10 == 0:
                    break
                elif (left % (num % 10)) == 0:
                    if num < 10:
                        lst += [left]
                        num //= 10
                    else:
                        num //= 10
                else:
                    break
            left += 1
        return lst