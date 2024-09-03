import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;

public class P5568_카드놓기 {

    static int N;
    static int K;
    static String cards[];
    static boolean visited[];
    static HashSet<String> hs = new HashSet<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());
        visited = new boolean[N];
        cards = new String[N];

        for (int i = 0; i < N; i++) {
            cards[i] = br.readLine();
        }

        dfs(0, "");
        System.out.println(hs.size());
    }

    private static void dfs(int cnt, String selectedNumber) {
        if (cnt == K) {
            hs.add(selectedNumber);
            return;
        }
        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(cnt + 1, selectedNumber + cards[i]);
                visited[i] = false;
            }
        }
    }
}