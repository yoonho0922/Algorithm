// https://www.acmicpc.net/problem/1793

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class 타일링 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int MAX_VALUE = 250;
        BigInteger[] dp = new BigInteger[MAX_VALUE + 1];

        dp[0] = BigInteger.ONE;
        dp[1] = BigInteger.ONE;
        dp[2] = BigInteger.valueOf(3);

        for (int i = 3; i < MAX_VALUE + 1; i++) {
            dp[i] = dp[i-1].add(dp[i-2].multiply(BigInteger.TWO));
        }

        String line;
        while ((line=br.readLine())!=null) {
            int N = Integer.parseInt(line);
            System.out.println(dp[N]);
        }
        br.close();
    }
}
