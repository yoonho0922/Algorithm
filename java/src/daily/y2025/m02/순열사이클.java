package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 순열사이클 {
    static int N;
    static int[] matrix;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            N = Integer.parseInt(br.readLine());
            matrix = new int[N+1];
            visited = new boolean[N+1];
            st = new StringTokenizer(br.readLine());
            for (int i = 1; i < N + 1; i++) {
                matrix[i] = Integer.parseInt(st.nextToken());
            }

            int answer = 0;
            for (int i = 1; i < N+1; i++) {
                if (!visited[i]) {
                    dfs(i);
                    answer++;
                }
            }
            sb.append(answer).append('\n');
        }
        System.out.println(sb);
    }

    private static void dfs(int here) {
        if (!visited[here]) {
            visited[here] = true;
            dfs(matrix[here]);
        }
    }
}
