# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

# https://leetcode.com/submissions/detail/442284622/
# 01/12/2021 19:13  

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = second = None
        for n in nums:
            if largest is None:
                largest = n
            elif second is None:
                if n > largest:
                    second = largest
                    largest = n
                else:
                    second = n
            else:
                if n > largest:
                    second = largest
                    largest = n
                elif n > second:
                    second = n
        # print(largest, second)
        return (largest - 1) * (second - 1)