# https://leetcode.com/problems/relative-sort-array/

# https://leetcode.com/submissions/detail/440535859/
# 01/08/2021 20:23  

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        occurrences = {}
        seen2 = set(arr2)
        seen1 = set()
        remainder = []
        for n in arr1:
            occurrences[n] = occurrences.get(n, 0) + 1
            if n not in seen2 and n not in seen1:
                seen1.add(n)
                remainder.append(n)
        result = []
        for n in arr2:
            result.extend(occurrences[n] * [n])
        for n in sorted(remainder):
            result.extend(occurrences[n] * [n])
        return result