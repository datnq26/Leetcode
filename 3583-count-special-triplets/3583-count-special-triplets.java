import java.util.HashMap;

class Solution {
    public int specialTriplets(int[] nums) {
        final long MOD = 1_000_000_007L;

        HashMap<Integer, Long> left = new HashMap<>();
        HashMap<Integer, Long> right = new HashMap<>();

        // Đếm toàn bộ right ban đầu
        for (int x : nums) {
            right.put(x, right.getOrDefault(x, 0L) + 1);
        }

        long ans = 0;

        for (int j = 0; j < nums.length; j++) {
            int val = nums[j];

            // j không còn ở bên phải nữa
            right.put(val, right.get(val) - 1);

            long need = (long) val * 2;

            long leftCnt  = left.getOrDefault((int)need, 0L);
            long rightCnt = right.getOrDefault((int)need, 0L);

            ans = (ans + (leftCnt * rightCnt) % MOD) % MOD;

            // đưa nums[j] vào left
            left.put(val, left.getOrDefault(val, 0L) + 1);
        }

        return (int)ans;
    }
}
