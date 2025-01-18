import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 줄어들지않아 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        int MAX_VALUE = 64;
        long[][] dp = new long[MAX_VALUE + 2][10];

        for (int i = 1; i < MAX_VALUE + 2; i++) {
            for (int j = 0; j < 10; j++) {
                if (i == 1) {
                    dp[i][j] = 1;
                } else {
                    for (int k = j; k < 10; k++) {
                        dp[i][j] += dp[i-1][k];
                    }
                }
            }
        }

        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            System.out.println(dp[N+1][0]);
        }
    }

}
