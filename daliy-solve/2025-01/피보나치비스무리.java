package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 피보나치비스무리 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        long[] dp = new long[116 + 1];
        dp[1] = dp[2] = dp[3] = 1;

        for (int i = 4; i < n + 1; i ++) {
            dp[i] = dp[i-3] + dp[i-1];
        }

        System.out.println(dp[n]);
    }

}
