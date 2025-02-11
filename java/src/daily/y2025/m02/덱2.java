package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class 덱2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        Deque<Integer> q = new LinkedList<>();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int type = Integer.parseInt(st.nextToken());
            switch (type) {
                case 1:
                    q.addFirst(Integer.parseInt(st.nextToken()));
                    break;
                case 2:
                    q.addLast(Integer.parseInt(st.nextToken()));
                    break;
                case 3:
                    sb.append((q.isEmpty() ? -1 : q.pollFirst())).append('\n');
                    break;
                case 4:
                    sb.append((q.isEmpty() ? -1 : q.pollLast())).append('\n');
                    break;
                case 5:
                    sb.append((q.size())).append('\n');
                    break;
                case 6:
                    sb.append((q.isEmpty() ? 1 : 0)).append('\n');
                    break;
                case 7:
                    sb.append((q.isEmpty() ? -1 : q.peekFirst())).append('\n');
                    break;
                case 8:
                    sb.append((q.isEmpty() ? -1 : q.peekLast())).append('\n');
                    break;
            }
        }
        System.out.println(sb);
    }
}
