package daily.y2025.m03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 평범한배낭 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] weights = new int[N+1];
        int[] values = new int[N+1];

        for (int i = 1; i < N+1; i++) {
            st = new StringTokenizer(br.readLine());
            weights[i] = Integer.parseInt(st.nextToken());
            values[i] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[N+1][K+1];

        for (int item = 1; item < N+1; item++) {
            for (int weight = 1; weight < K + 1; weight++) {
                if (weight - weights[item] >= 0) {
                    dp[item][weight] = Math.max(dp[item-1][weight], values[item] + dp[item-1][weight - weights[item]]);
                } else {
                    dp[item][weight] = dp[item-1][weight];
                }
            }
        }

        System.out.println(dp[N][K]);
    }
}
