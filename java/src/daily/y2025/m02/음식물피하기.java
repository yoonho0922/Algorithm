package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 음식물피하기 {

    static int N;
    static int M;
    static int K;
    static boolean[][] G;
    static boolean[][] visited;
    static int[] dy = {0, 0, 1, -1};
    static int[] dx = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        G = new boolean[N+1][M+1];
        visited = new boolean[N+1][M+1];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            G[r][c] = true;
        }

        int answer = 0;

        for (int i = 0; i < N + 1; i++) {
            for (int j = 0; j < M + 1; j++) {
                if (G[i][j] && !visited[i][j]) {
                    int size = bfs(i, j);
                    answer = Math.max(answer, size);
                }
            }
        }

        System.out.println(answer);
    }

    private static int bfs(int r, int c) {
        int size = 1;
        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(r, c));
        visited[r][c] = true;
        while (!q.isEmpty()) {
            Point cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int ny = cur.y + dy[i];
                int nx = cur.x + dx[i];
                if (0 < ny && ny <= N && 0 < nx && nx <= M && G[ny][nx] && !visited[ny][nx]) {
                    visited[ny][nx] = true;
                    q.offer(new Point(ny,nx));
                    size++;
                }
            }
        }
        return size;
    }

    static class Point {
        int y;
        int x;
        Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}