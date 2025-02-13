package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 빌런호석 {

    static int N;
    static int K;
    static int P;
    static int X;

    static int[][] display = {{1, 1, 1, 0, 1, 1, 1}, //0
        {0, 0, 1, 0, 0, 0, 1}, //1
        {0, 1, 1, 1, 1, 1, 0}, //2
        {0, 1, 1, 1, 0, 1, 1}, //3
        {1, 0, 1, 1, 0, 0, 1}, //4
        {1, 1, 0, 1, 0, 1, 1}, //5
        {1, 1, 0, 1, 1, 1, 1}, //6
        {0, 1, 1, 0, 0, 0, 1}, //7
        {1, 1, 1, 1, 1, 1, 1}, //8
        {1, 1, 1, 1, 0, 1, 1}}; //9

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        int answer = 0;
        int[] actualDigits = toDigits(X);

        for (int i = 1; i < N + 1; i++) {
            if (i == X) continue;

            int[] targetDigits = toDigits(i);
            int diffCnt = 0;
            for (int j = 0; j < K; j++) {
                diffCnt += compareDigit(actualDigits[j], targetDigits[j]);
            }
            if (diffCnt <= P) {
                answer++;
            }
        }

        System.out.println(answer);
    }

    private static int compareDigit(Integer digitA, Integer digitB) {
        int cnt = 0;
        for (int i = 0; i < display[0].length; i++) {
            if (display[digitA][i] != display[digitB][i]) {
                cnt++;
            }
        }
        return cnt;
    }

    private static int[] toDigits(int num) {
        int[] digits = new int[K];
        for (int i = K - 1; i > - 1; i--) {
            digits[i] = num%10;
            num /= 10;
        }
        return digits;
    }
}
