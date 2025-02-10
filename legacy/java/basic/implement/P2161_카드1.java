import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder answer = new StringBuilder();

        Queue<Integer> queue = new LinkedList<>();

        for (int i = 1; i < N + 1; i++) {
            queue.add(i);
        }

        for (int i = 0; i < N; i++) {
            Integer number = queue.poll();
            answer.append(number).append(" ");
            queue.add(queue.poll());
        }

        System.out.println(answer);
    }
}