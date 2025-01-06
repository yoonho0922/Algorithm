package algorithm;

public class Interview209 {

    public static void main(String[] args) {
        minSubArrayLen(7, new int[]{2,3,1,2,4,3});
    }

    public static int minSubArrayLen(int target, int[] nums) {
        int start = 0, end = 0, sum = 0, answer = Integer.MAX_VALUE;

        while (end < nums.length) {
            sum = nums[end];
            end ++;

            while (sum >= target) {
                answer = Math.min(answer, end - start);
                sum -= nums[start];
                start ++;
            }
        }

        return answer == Integer.MAX_VALUE ? 0 : answer;
    }
}
