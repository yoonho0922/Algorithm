package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

public class 추월 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Queue<String> q = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            q.offer(br.readLine());
        }

        String[] outCars = new String[N];
        for (int i = 0; i < N; i++) {
            outCars[i] = br.readLine();
        }

        int answer = 0;
        int idx = 0;
        Set<String> hs = new HashSet<>();
        while (!q.isEmpty() && idx < N) {
            if (q.peek().equals(outCars[idx])) {
                q.poll();
                idx++;
            } else {
                if (hs.contains(q.peek())) {
                    hs.remove(q.poll());
                } else {
                    hs.add(outCars[idx]);
                    idx++;
                    answer ++;
                }
            }
        }

        System.out.println(answer);
    }
}
