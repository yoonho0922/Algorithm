package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 주식 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            int[] nums = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                nums[i] = Integer.parseInt(st.nextToken());
            }

            long answer = 0;
            int[] dp = new int[N];
            dp[N-1] = nums[N-1];
            for (int i = N - 2; i > -1; i--) {
                dp[i] = Math.max(nums[i], dp[i+1]);
                answer += dp[i] - nums[i];
            }
            sb.append(answer).append('\n');
        }
        System.out.println(sb);
    }
}
