# https://leetcode.com/problems/binary-search/

# https://leetcode.com/submissions/detail/435360551/
# 12/27/2020 17:29  

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (end + start) // 2
            curr = nums[mid]
            if curr == target:
                return mid
            if target < curr:
                if end == mid:
                    break
                end = mid
            else:
                mid = mid + (end + start) % 2
                if start == mid:
                    break
                start = mid
        return -1