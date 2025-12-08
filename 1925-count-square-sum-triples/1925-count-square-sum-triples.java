import java.lang.Math;
import java.util.HashMap;

public class Solution {
    public int countTriples(int n) {
        int count = 0;
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        for (int i = 1; i <= n; i++) {
            hashMap.put(i*i, i);
        }
        for (int i = 1; i <= n; i ++) {
            for (int j = 1; j <= n; j ++) {
                if (i != j) {
                    int sum = i * i + j *j;
                    if (hashMap.containsKey(sum)) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
