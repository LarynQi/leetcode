# https://leetcode.com/problems/distribute-candies/

# https://leetcode.com/submissions/detail/440510180/
# 01/08/2021 18:53  

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies = len(candyType) // 2
        d = set()
        for c in candyType:
            d.add(c)
        return min(candies, len(d))