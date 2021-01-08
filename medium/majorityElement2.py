# https://leetcode.com/problems/majority-element-ii/

# https://leetcode.com/submissions/detail/440028865/
# 01/07/2021 16:35  

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        ### Solution: Boyer-Moore Voting Algorithm ###
        if not nums:
            return []
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            # print(candidate1, count1, candidate2, count2)
            # if n == candidate1 or n == candidate2:
            #     if n == candidate1:
            #         count1 += 1
            #         count2 -= 1
            #     if n == candidate2:
            #         count2 += 1
            #         count1 -= 1
            # elif candidate1 is None or count1 < 0:
            #     candidate1 = n
            #     count1 = 1
            #     count2 -= 1
            # elif candidate2 is None or count2 < 0:
            #     candidate2 = n
            #     count2 = 1
            #     count1 -= 1
            # else:
            #     count1 -= 1
            #     count2 -= 1
            #     if count1 < 0:
            #         candidate1 = n
            #     elif count2 < 0:
            #         candidate2 = n
        result = []
        for c in (candidate1, candidate2):
            if nums.count(c) > len(nums) / 3:
                result.append(c)
        return result
        
        
        ### HashMap (> O(1) space) ###
        occurrences = {}
        threshold = len(nums) / 3
        result = []
        seen = set()
        for n in nums:
            temp = occurrences[n] = occurrences.get(n, 0) + 1
            if temp > threshold and n not in seen:
                result.append(n)
                seen.add(n)
        return result

# https://leetcode.com/submissions/detail/440022889/
# 01/07/2021 16:16  

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ### HashMap (> O(1) space) ###
        occurrences = {}
        threshold = len(nums) / 3
        result = []
        seen = set()
        for n in nums:
            temp = occurrences[n] = occurrences.get(n, 0) + 1
            if temp > threshold and n not in seen:
                result.append(n)
                seen.add(n)
        return result