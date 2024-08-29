import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class P25305_커트라인 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        Integer[] scores = new Integer[N];
        for (int i = 0; i < N; i++)
            scores[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(scores, Comparator.reverseOrder());
        System.out.println(scores[K-1]);
    }
}