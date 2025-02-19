package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 지름길 {

    static int N;
    static int D;
    static int[] dists;
    static Path[] paths;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        paths = new Path[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int length = Integer.parseInt(st.nextToken());
            paths[i] = new Path(start, end, length);
        }

        dists = new int[D + 1];
        for (int i = 1; i < D + 1; i++) {
            dists[i] = dists[i-1] + 1;
            for (Path p : paths) {
                if (p.end == i) {
                    dists[i] = Math.min(dists[i], dists[p.start] + p.length);
                }
            }
        }

        System.out.println(dists[D]);
    }

    public static class Path {
        int start;
        int end;
        int length;

        public Path(int start, int end, int length) {
            this.start = start;
            this.end = end;
            this.length = length;
        }
    }
}
