package daily.y2025.m02;

import java.io.*;
import java.util.*;

public class 골드바흐파티션 {

    static int MAX_VALUE = 1_000_000;
    static boolean[] isPrime;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        isPrime = new boolean[MAX_VALUE + 1];

        updatePrime();

        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            int cnt = 0;
            for (int p = 2; p <= N/2; p++) {
                if (isPrime[p] && isPrime[N-p]) {
                    cnt++;
                }
            }
            sb.append(cnt).append('\n');
        }

        System.out.println(sb);
    }

    private static void updatePrime() {
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i <= Math.sqrt(MAX_VALUE); i++) {
            if (isPrime[i]) {
                for (int j = i * 2; j < MAX_VALUE + 1; j += i) {
                    isPrime[j] = false;
                }
            }
        }
    }
}
