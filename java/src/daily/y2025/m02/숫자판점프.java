package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class 숫자판점프 {

    static int N = 5;
    static int[][] G = new int[N][N];
    static Set<String> hs = new HashSet<>();
    static int[] dy = {0, 0, 1, -1};
    static int[] dx = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                G[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                dfs(i, j, new StringBuilder(String.valueOf(G[i][j])));
            }
        }

        System.out.println(hs.size());
    }

    private static void dfs(int r, int c, StringBuilder sb) {
        if (sb.length() == 6) {
            hs.add(sb.toString());
            return;
        }

        for (int i = 0; i < 4; i++) {
            int ny = r + dy[i];
            int nx = c + dx[i];
            if (0 <= ny && ny < N && 0 <= nx && nx < N) {
                sb.append(G[ny][nx]);
                dfs(ny, nx, sb);
                sb.deleteCharAt(sb.length() - 1);
            }
        }
    }

}
