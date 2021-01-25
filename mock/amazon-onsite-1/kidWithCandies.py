# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# https://leetcode.com/interview/reports/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6MTUwNzg5OA==

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Scan 1: find maximum candy value
        # Scan 2: fill up result list with whether extraCandies >= difference of candies[i] and max value
        # Runtime analysis: O(2N) = O(N)
        highest = max(candies)
        result = []
        for c in candies:
            if highest - c <= extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result
        