// https://www.acmicpc.net/problem/2470

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 두용액 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] nums = new long[N];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++){
            nums[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(nums);

        int left = 0;
        int right = N - 1;
        long[] answer = {nums[left], nums[right]};

        while (left < right) {
            long sum = nums[left] + nums[right];
            if (Math.abs(sum) < Math.abs(answer[0] + answer[1])) {
                answer[0] = nums[left];
                answer[1] = nums[right];
            }

            if (sum == 0) {
                break;
            } else if (sum > 0) {
                right --;
            } else {
                left ++;
            }
        }

        System.out.println(answer[0] + " " + answer[1]);
    }
}
