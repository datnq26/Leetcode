class Solution {
    public int numSub(String s) {
        int mod = 1_000_000_007;
        long count = 0;  // dùng long để tránh tràn số
        int consecutive = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                consecutive++;
                count = (count + consecutive) % mod;
            } else {
                consecutive = 0;
            }
        }

        return (int) count;
    }
}
