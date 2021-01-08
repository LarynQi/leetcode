# https://leetcode.com/problems/third-maximum-number/

# https://leetcode.com/submissions/detail/440244760/
# 01/08/2021 03:00  

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None
        maxs = [first, second, third]
        for n in nums:
            if first is None:
                first = n
            elif second is None and n != first:
                first, second = max(first, n), min(first, n)
            elif third is None and n != second and n != first:
                if n > first:
                    third = second
                    second = first
                    first = n
                elif n > second:
                    third = second
                    second = n
                else:
                    third = n
            else:
                if second is None or third is None:
                    maxs = [first, second, third]
                    continue
                if n not in maxs:
                    if n > third:
                        if n > second:
                            if n > first:
                                third = second
                                second = first
                                first = n
                            else:
                                third = second
                                second = n
                        else:
                            third = n
            maxs = [first, second, third]
        if third is None:
            return first
        return third
        