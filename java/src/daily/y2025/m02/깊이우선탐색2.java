package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

public class 깊이우선탐색2 {

    static int N;
    static int M;
    static int R;
    static ArrayList<ArrayList<Integer>> G = new ArrayList<>();
    static int[] visited;
    static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        visited = new int[N+1];
        for (int i = 0; i < N+1; i++) {
            G.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            G.get(a).add(b);
            G.get(b).add(a);
        }

        for (int i = 1; i < N + 1; i++) {
            G.get(i).sort(Comparator.reverseOrder());
        }

        dfs(R);
        for (int i = 1; i < N + 1; i++) {
            sb.append(visited[i]).append('\n');
        }
        System.out.println(sb);
    }

    private static void dfs(int here) {
        if (visited[here] == 0) {
            visited[here] = ++cnt;
            for (int nxt : G.get(here)) {
                dfs(nxt);
            }
        }
    }
}
