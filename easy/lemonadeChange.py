# https://leetcode.com/problems/lemonade-change/

# https://leetcode.com/submissions/detail/291911253/
# 01/06/2020 19:05  

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                fives -= 1
                tens += 1
            else:
                if tens:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            if fives < 0:
                return False
        return True