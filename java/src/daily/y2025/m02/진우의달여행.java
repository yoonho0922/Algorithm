package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 진우의달여행 {

    static int[] BLOCK = new int[]{999, 999, 999};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int answer = 999;
        int[][][] dp = new int[N+1][M+2][3];
        for (int i = 1; i < N+1; i++) {
            dp[i][0] = BLOCK;
            dp[i][M+1] = BLOCK;
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j < M+1; j++) {
                int num = Integer.parseInt(st.nextToken());
                dp[i][j][0] = num + Math.min(dp[i-1][j-1][1], dp[i-1][j-1][2]); // from left
                dp[i][j][1] = num + Math.min(dp[i-1][j][0], dp[i-1][j][2]); // from middle
                dp[i][j][2] = num + Math.min(dp[i-1][j+1][0], dp[i-1][j+1][1]); // from right
                if (i == N) {
                    for (int k = 0; k < 3; k++)
                        answer = Math.min(answer, dp[i][j][k]);
                }
            }
        }
        System.out.println(answer);
    }
}
