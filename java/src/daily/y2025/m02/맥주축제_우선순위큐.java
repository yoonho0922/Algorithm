package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 맥주축제_우선순위큐 {

    static int N;
    static int M;
    static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        int[][] beers = new int[K][2];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            beers[i][0] = Integer.parseInt(st.nextToken());
            beers[i][1] = Integer.parseInt(st.nextToken());
        }

        // 도수 오름차순, 선호도 내림차순 정렬
        Arrays.sort(beers, (a, b) -> a[1] != b[1] ? a[1] - b[1] : b[0] - a[0]);

        // 선호도 오름차순
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int totalLike = 0;
        for (int[] beer : beers) {
            pq.add(new int[]{beer[0], -beer[1]});
            totalLike += beer[0];
            if (pq.size() == N) {
                if (totalLike >= M) {
                    System.out.println(beer[1]);
                    return;
                } else {
                    totalLike -= pq.poll()[0];
                }
            }
        }
        System.out.println(-1);
    }
}
