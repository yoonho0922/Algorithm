import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class 너비우선탐색1 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();
        int[] visited = new int[N + 1];

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            graph.get(A).add(B);
            graph.get(B).add(A);
        }

        for(int i = 1; i<=N; i++) {
            Collections.sort(graph.get(i));
        }

        int sequence = 1;
        Queue<Integer> q = new LinkedList<>();
        visited[R] = sequence++;
        q.offer(R);

        while (!q.isEmpty()) {
            Integer here = q.poll();
            for (int next : graph.get(here)) {
                if (visited[next] == 0) {
                    visited[next] = sequence++;
                    q.offer(next);
                }
            }
        }

        for (int i = 1; i < N + 1; i ++) {
            System.out.println(visited[i]);
        }
    }

}
