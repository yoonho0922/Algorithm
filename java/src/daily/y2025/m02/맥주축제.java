package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 맥주축제 {

    static int N;
    static int M;
    static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        int[][] beers = new int[K][2];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            beers[i][0] = Integer.parseInt(st.nextToken());
            beers[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(beers, (a, b) -> a[0] != b[0] ? b[0] - a[0] : a[1] - b[1]);

        long start = 0;
        long end = Integer.MAX_VALUE;
        long answer = -1;
        while (start <= end) {
            long mid = (start + end) / 2;
            if (check((int) mid, beers)) {
                answer = answer == -1 ? mid : Math.min(answer, mid);
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        System.out.println(answer);
    }

    private static boolean check(int limit, int[][] beers) {
        int cnt = 0;
        double totalV = 0;
        for (int[] beer : beers) {
            if (cnt < N) {
                if (beer[1] <= limit) {
                    totalV += beer[0];
                    cnt++;
                }
            } else {
                break;
            }
        }
        return (cnt == N && totalV >= M);
    }
}
