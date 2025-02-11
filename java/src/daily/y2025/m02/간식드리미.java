package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class 간식드리미 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Queue<Integer> mainWaiting = new LinkedList<>();
        Stack<Integer> subWaiting = new Stack<>();

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            mainWaiting.add(Integer.parseInt(st.nextToken()));
        }

        int expected = 1;
        while (expected < N) {
            if (!mainWaiting.isEmpty() && expected == mainWaiting.peek()) {
                mainWaiting.poll();
                expected++;
            } else if (!subWaiting.isEmpty() && expected == subWaiting.peek()) {
                subWaiting.pop();
                expected++;
            } else if (!mainWaiting.isEmpty()) {
                subWaiting.push(mainWaiting.poll());
            } else {
                break;
            }
        }

        System.out.println(expected == N ? "Nice" : "Sad");
    }
}
