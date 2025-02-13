package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 결혼식 {

    static int N;
    static int M;
    static ArrayList<ArrayList<Integer>> G = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
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

        System.out.println(bfs(1));

    }
    private static int bfs(int start) {
        int cnt = 0;
        Queue<Integer> q = new LinkedList<>();
        int[] visited = new int[N+1];
        q.offer(start);
        visited[start] = 1;
        while (!q.isEmpty()) {
            int cur = q.poll();
            if (visited[cur] < 3) {
                for (int nxt : G.get(cur)) {
                    if (visited[nxt] == 0) {
                        visited[nxt] = visited[cur] + 1;
                        q.offer(nxt);
                        cnt++;
                    }
                }
            }
        }
        return cnt;
    }
}
