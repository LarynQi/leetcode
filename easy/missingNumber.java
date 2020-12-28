// https://leetcode.com/problems/missing-number/

// https://leetcode.com/submissions/detail/434340203/
// 12/25/2020 00:17

class Solution {
    public int missingNumber(int[] nums) {
        HashSet s = new HashSet();
        for (int i = 0; i < nums.length + 1; i += 1) {
            s.add(i);
        }
        for (int n : nums) {
            s.remove(n);
        }
        return (Integer) s.toArray()[0];
    }
}