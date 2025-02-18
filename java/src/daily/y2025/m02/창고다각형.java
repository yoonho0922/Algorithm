package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 창고다각형 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int[] p = new int[1001];
        int maxH = -1;
        int checkPoint = -1;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int L = Integer.parseInt(st.nextToken());
            int H = Integer.parseInt(st.nextToken());
            p[L] = H;
            if (H > maxH) {
                maxH = H;
                checkPoint = L;
            }
        }

        int answer = 0;
        int[] left = new int[1001];
        for (int i = 1; i < checkPoint; i++) {
            answer += left[i] = Math.max(p[i], left[i-1]);
        }
        int[] right = new int[1002];
        for (int i = 1000; i > checkPoint; i--) {
            answer += right[i] = Math.max(p[i], right[i+1]);
        }
        System.out.println(answer + maxH);
    }
}
