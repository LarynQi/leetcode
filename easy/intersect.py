# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# https://leetcode.com/submissions/detail/440524265/
# 01/08/2021 19:43  

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # seen_1 = set()
        # seen_2 = set()
        # for arr, seen in [(nums1, seen_1), (nums2, seen_2)]:
        #     for n in arr:
        #         seen.add(n)
        # return list(seen_1 & seen_2)
        
        occurrences_1 = {}
        for n in nums1:
            occurrences_1[n] = occurrences_1.get(n, 0) + 1
        occurrences_2 = {}
        for n in nums2:
            if n in occurrences_1:
                occurrences_2[n] = occurrences_2.get(n, 0) + 1
        result = []
        for n in occurrences_2:
            for _ in range(min(occurrences_1[n], occurrences_2[n])):
                result.append(n)
        return result