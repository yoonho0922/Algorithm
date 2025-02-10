import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class 삼각그래프 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N;
        int tc = 0;
        int MAX_WEIGHT = 1_000_000;
        while ((N = Integer.parseInt(br.readLine())) != 0) {
            tc++;
            int[][] dp = new int[N][3];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                if (i==0) {
                    dp[i][0] = Integer.parseInt(st.nextToken()) + MAX_WEIGHT;
                    dp[i][1] = Integer.parseInt(st.nextToken());
                    dp[i][2] = Integer.parseInt(st.nextToken()) + dp[i][1];
                } else {
                    dp[i][0] = Integer.parseInt(st.nextToken()) + IntStream.of(dp[i-1][0], dp[i-1][1]).min().getAsInt();
                    dp[i][1] = Integer.parseInt(st.nextToken()) + IntStream.of(dp[i][0], dp[i-1][0], dp[i-1][1], dp[i-1][2]).min().getAsInt();
                    dp[i][2] = Integer.parseInt(st.nextToken()) + IntStream.of(dp[i][1], dp[i-1][1], dp[i-1][2]).min().getAsInt();
                }
            }
            System.out.println(tc + ". " + dp[N-1][1]);
        }
    }
}
