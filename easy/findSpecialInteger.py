# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

# https://leetcode.com/submissions/detail/440624734/
# 01/09/2021 01:22  

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        ### O(N): Non-optimal ###
        
        curr = None
        count = 0
        threshold = len(arr) / 4
        for n in arr:
            if curr is None or n != curr:
                curr = n
                count = 1
            else:
                count += 1
                if count > threshold:
                    return curr
        return curr