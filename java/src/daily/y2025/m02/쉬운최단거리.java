package daily.y2025.m02;

import java.io.*;
import java.util.*;

public class 쉬운최단거리 {

    static int N;
    static int M;
    static int[][] G;
    static int[][] visited;
    static int[] dy = {0, 0, -1, 1};
    static int[] dx = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        G = new int[N][M];
        visited = new int[N][M];
        int[] start = {-1, -1};
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                G[i][j] = Integer.parseInt(st.nextToken());
                if (G[i][j] == 2) {
                    start = new int[]{i, j};
                }
                visited[i][j] = G[i][j] == 0 ? 0 : -1;
            }
        }

        bfs(start[0], start[1]);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(visited[i][j]).append(' ');
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }

    public static void bfs(int y, int x) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{y, x});
        visited[y][x] = 0;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int ny = cur[0] + dy[i];
                int nx = cur[1] + dx[i];
                if (0 <= ny && ny < N && 0 <= nx && nx < M && visited[ny][nx] == -1) {
                    if (G[ny][nx] == 1) {
                        visited[ny][nx] = visited[cur[0]][cur[1]] + 1;
                        q.add(new int[]{ny, nx});
                    }
                }
            }
        }
    }
}
