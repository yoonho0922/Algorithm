package algorithm;

import java.util.HashMap;

/**
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
 */
public class Interview80 {

    public int removeDuplicates(int[] nums) {
        int cnt = 1;
        int index = 1; // new array index
        int here = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (here == nums[i]) {
                if (cnt < 2) {
                    nums[index] = nums[i];
                    index ++;
                }
                cnt++;
            } else {
                nums[index] = nums[i];
                here = nums[i];

                cnt = 1;
                index++;
            }
        }
        return index;
    }
}
