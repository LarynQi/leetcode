# https://leetcode.com/problems/shuffle-the-array/

# https://leetcode.com/submissions/detail/440996038/
# 01/09/2021 20:51  

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # x = nums[:n]
        # y = nums[n:]
        # result = []
        # print(x, y)
        # for p in zip(x, y):
        #     x_i, y_i = p[0], p[1]
        #     result.append(x_i)
        #     result.append(y_i)
        # return result
        result = []
        for i in range(n):
            j = n + i
            result.append(nums[i])
            result.append(nums[j])
        return result