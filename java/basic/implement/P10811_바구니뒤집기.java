import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] bucket = new int[N];

        for (int i = 0; i < N; i++) {
            bucket[i] = i + 1;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            reverse(bucket, a-1, b-1);
        }

        for (int ball : bucket) {
            System.out.print(ball + " ");
        }
        br.close();
    }

    private static void reverse(int[] bucket, int a, int b) {
        for (int i = a; i <= (a + b - 1) / 2; i++) {
            int tmp = bucket[i];
            bucket[i] = bucket[b + a - i];
            bucket[a + b-i] = tmp;
        }
    }
}
