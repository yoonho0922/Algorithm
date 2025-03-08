package daily.y2025.m03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 다음소수 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            long num = Long.parseLong(br.readLine());

            if (num <= 1) {
                sb.append(2).append('\n');
            } else {
                while (!isPrime(num)) {
                    num++;
                }
                sb.append(num).append('\n');
            }
        }
        System.out.print(sb);
    }

    private static boolean isPrime(long num) {
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
