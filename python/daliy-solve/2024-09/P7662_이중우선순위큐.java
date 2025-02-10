import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P7662_이중우선순위큐 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int K = Integer.parseInt(br.readLine());
            PriorityQueue<Integer> maxQ = new PriorityQueue<>(Comparator.reverseOrder());
            PriorityQueue<Integer> minQ = new PriorityQueue<>();
            HashMap<Integer, Integer> hm = new HashMap<>();

            while (K-- > 0) {
                StringTokenizer st = new StringTokenizer(br.readLine(), " ");
                String command = st.nextToken();
                int number = Integer.parseInt(st.nextToken());

                if (command.equals("I")) {
                    maxQ.add(number);
                    minQ.add(number);
                    hm.put(number, hm.getOrDefault(number, 0) + 1);
                } else {
                    if (number == 1) { // 최댓값 삭제
                        poll(maxQ, hm);
                    } else { // 최솟값 삭제
                        poll(minQ, hm);
                    }
                }
            }

            // 출력
            if (hm.values().stream().anyMatch(v -> v > 0)) {
                System.out.print(poll(maxQ, hm));
                System.out.print(poll(minQ, hm));
            } else {
                System.out.println("EMPTY");
            }
        }
    }

    private static Integer poll(PriorityQueue<Integer> q, HashMap<Integer, Integer> hm) {
        while (true) {
            Integer number = q.poll();
            if (number == null) return 0;
            if (hm.getOrDefault(number, 0) > 0) {
                hm.put(number, hm.get(number) - 1);
                return number;
            }
        }
    }
}