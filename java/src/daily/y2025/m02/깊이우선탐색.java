package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class 깊이우선탐색 {

    static int N;
    static int count;
    static int[] visited;
    static List<List<Integer>> G = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N + 1; i++) {
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
            Collections.sort(G.get(i));
        }

        visited = new int[N + 1];
        dfs(R);

        for (int i = 1; i < N + 1; i++) {
            sb.append(visited[i]).append('\n');
        }
        System.out.println(sb);
    }

    private static void dfs(int here) {
        visited[here] = ++count;
        for (int nxt : G.get(here)) {
            if (visited[nxt] == 0) {
                dfs(nxt);
            }
        }
    }

}
