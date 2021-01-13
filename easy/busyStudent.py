# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

# https://leetcode.com/submissions/detail/442286555/
# 01/12/2021 19:18  

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n = len(startTime)
        i = 0
        count = 0
        while i < n:
            s = startTime[i]
            e = endTime[i]
            if queryTime >= s and queryTime <= e:
                count += 1
            i += 1
        return count