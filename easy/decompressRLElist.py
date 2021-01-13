# https://leetcode.com/problems/decompress-run-length-encoded-list/

# https://leetcode.com/submissions/detail/442269757/
# 01/12/2021 18:31  

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        n = len(nums)
        while i < n:
            freq, val = nums[i], nums[i + 1]
            result.extend(freq * [val])
            i += 2
        return result