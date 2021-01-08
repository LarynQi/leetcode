# https://leetcode.com/problems/majority-element/

# https://leetcode.com/submissions/detail/440022210/
# 01/07/2021 16:14  

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ### Boyer-Moore Voting Algorithm ###
        candidate = None
        count = 0
        for n in nums:
            if not candidate:
                candidate = n
                count = 1
            elif n == candidate:
                count += 1
            else:
                count -= 1
                if count < 0:
                    candidate = n
                    count = 1
        return candidate
        
        ### HashMap ###
        # counts = {}
        # majority = len(nums) / 2
        # for n in nums:
        #     temp = counts[n] = counts.get(n, 0) + 1
        #     if temp > majority:
        #         return n

# https://leetcode.com/submissions/detail/440010912/
# 01/07/2021 15:38  

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        majority = len(nums) / 2
        for n in nums:
            temp = counts[n] = counts.get(n, 0) + 1
            if temp > majority:
                return n
