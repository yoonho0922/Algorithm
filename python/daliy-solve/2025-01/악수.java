import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 악수 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int MAX_SIZE = 10_000_000;
        int[] dp = new int[MAX_SIZE + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < N + 1; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) % 10;
        }
        System.out.println(dp[N]);
    }
}
