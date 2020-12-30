# https://leetcode.com/problems/product-of-array-except-self/

# https://leetcode.com/submissions/detail/436375447/
# 12/30/2020 02:39  

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n^2
        # prod = 1
        # for n in nums:
        #     prod *= n
        # result = len(nums) * [0]
        # for i in range(len(nums)):
        #     n = nums[i]
        #     if n != 0:
        #         result[i] = prod // n
        #     else:
        #         result[i] = prod
        # return result
        
        # result = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             prod *= nums[j]
        #     result.append(prod)
        # return result
    
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             nums[left] =  
            
#             left += 1
#             right -= 1

        result = []
        prod = 1
        for i in range(len(nums)):
            result.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * prod
            prod *= nums[i] 
        return result
        
        