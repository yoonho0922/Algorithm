package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 평범한배낭 {

    public static void main(String[] rags) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] weights = new int[N+1];
        int[] values = new int[N+1];
        int[][] dp = new int[N+1][K+1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            weights[i] = Integer.parseInt(st.nextToken());
            values[i] = Integer.parseInt(st.nextToken());
        }


        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= K; j++) {
                if (j >= weights[i]) {
                    dp[i][j] = Math.max(dp[i-1][j], values[i] + dp[i-1][j - weights[i]]);
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }

//        for (int[] row : dp) {
//            for (int col : row) {
//                System.out.print(col + " ");
//            }
//            System.out.println();
//        }

        System.out.println(dp[N][K]);
    }

}
