package daily.y2025.m03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 막대기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] sticks = new int[N];

        for (int i = 0; i < N; i++) {
            sticks[i] = Integer.parseInt(br.readLine());
        }

        int cnt = 1;
        int here = sticks[N-1];

        for (int i = N - 2; i >= 0; i--) {
            if (sticks[i] > here) {
                here = sticks[i];
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}
