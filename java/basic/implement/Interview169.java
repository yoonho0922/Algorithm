package algorithm;

import java.util.Arrays;
import java.util.HashMap;

/**
 * https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
 */
public class Interview169 {

    public static int majorityElement(int[] nums) throws Exception {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            int cnt = map.getOrDefault(num, 0);
            if (cnt + 1 > nums.length / 2)
                return num;
            else
                map.put(num, cnt + 1);
        }
        throw new Exception("No majority element");
    }
}
