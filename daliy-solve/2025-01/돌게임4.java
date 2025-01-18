import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 돌게임4 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        boolean[] dp = new boolean[1001];
        dp[2] = true; dp[3] = false; dp[4] = true;

        for (int i = 4; i < N + 1; i++) {
            dp[i] = (!dp[i-1]) || (!dp[i-3]) || (!dp[i-4]);
        }

        if (dp[N])
            System.out.println("SK");
        else {
            System.out.println("CY");
        }
    }

}
