# https://leetcode.com/problems/intersection-of-two-arrays/

# https://leetcode.com/submissions/detail/275567396/
# 11/03/2019 01:42  

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) <= len (nums2):
            smallest = nums1
            other = nums2
        else:
            smallest = nums2
            other = nums1
        intersects = []
        cache = {}
        for x in smallest:
            if x in other and x not in cache:
                intersects += [x]
                cache[x] = True
        return intersects