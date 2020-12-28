# https://leetcode.com/problems/maximum-product-of-three-numbers/

# https://leetcode.com/submissions/detail/292021538/
# 01/07/2020 02:54  

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        negs = []
        negs += [min(nums)]
        dupe = nums[:]
        dupe.remove(negs[0])
        negs += [min(dupe)]
        
        maxs = [max(nums)]
        dupe = nums[:]
        dupe.remove(maxs[0])
        maxs += [max(dupe)]
        dupe = nums[:]
        dupe.remove(maxs[0])
        dupe.remove(maxs[1])
        maxs += [(max(dupe))]
        
        result = [maxs[0]]
        if negs[0] < 0 and negs[1] < 0:
            if negs[0] * negs[1] > maxs[1] * maxs[2]:
                print(result)
                print(negs)
                result += negs
            else:
                result = maxs
        else:
            result = maxs
        return result[0] * result[1] * result[2]