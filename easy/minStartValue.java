// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

// https://leetcode.com/submissions/detail/434338515/
// 12/25/2020 00:09  

class Solution {
    public int minStartValue(int[] nums) {
        int lowest = Integer.MAX_VALUE;
        int sum = 0;
        for (int n : nums) {
            sum += n;
            lowest = Math.min(lowest, sum);
        }
        if (lowest <= 0) {
            return -lowest + 1;
        } else {
            return 1;
        }
    }
}