import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class P16928_뱀과사다리게임 {
    static int N;
    static int M;
    static int[] board;
    static int START = 1;
    static int END = 100;
    static int[] dice = {1,2,3,4,5,6};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[END + 1];
        for (int i = 0; i < N + M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int before = Integer.parseInt(st.nextToken());
            int after = Integer.parseInt(st.nextToken());
            board[before] = after;
        }

        System.out.println(bfs());
    }

    private static int bfs() throws Exception {
        int cnt = 0;
        ArrayDeque<Integer> q = new ArrayDeque<>();
        boolean[] visited = new boolean[END + 1];

        q.add(START);
        visited[START] = true;

        while (!q.isEmpty()) {
            int len = q.size();

            while (len-- > 0) {
                int now = q.pollFirst();

                if (now == END)
                    return cnt;

                for (int d : dice) {
                    int next = now + d;
                    if (next > END)
                        continue;
                    if (board[next] != 0)
                        next = board[next];
                    if (!visited[next]) {
                        q.add(next);
                        visited[next] = true;
                    }
                }
            }
            cnt++;
        }

        throw new Exception(END + "에 도달할 수 없습니다.");
    }
}