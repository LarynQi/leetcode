# https://leetcode.com/problems/asteroid-collision/

# https://leetcode.com/submissions/detail/427912884/
# 12/06/2020 12:10  

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        while i < len(asteroids) - 1:
            left, right = asteroids[i], asteroids[i + 1]
            if left > 0 and right < 0:
                if abs(right) > left:
                    asteroids.pop(i)
                    i = max(0, i - 1)
                elif left > abs(right):
                    asteroids.pop(i + 1)
                else:
                    asteroids.pop(i)
                    asteroids.pop(i)
                    i = max(0, i - 1)
                i -= 1
            i += 1
        return asteroids