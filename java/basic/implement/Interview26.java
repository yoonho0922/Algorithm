package algorithm;

import java.util.Arrays;

/**
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
 */
public class Interview26 {

    public static int removeDuplicates(int[] nums) {
        int[] distinctive = Arrays.stream(nums).distinct().toArray();
        for (int i = 0; i < distinctive.length; i++) {
            nums[i] = distinctive[i];
        }
        return distinctive.length;
    }
}
