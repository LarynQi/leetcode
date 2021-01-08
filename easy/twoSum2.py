# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# https://leetcode.com/submissions/detail/439965708/
# 01/07/2021 13:17  

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                break
            elif curr < target:
                left += 1
            else:
                right -= 1
        return [left + 1, right + 1]