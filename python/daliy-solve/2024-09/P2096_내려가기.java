import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        int[][] minDP = new int[N][3];
        int[][] maxDP = new int[N][3];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < 3; j++) {
                int num = Integer.parseInt(st.nextToken());
                if (i == 0) {
                    minDP[i][j] = num;
                    maxDP[i][j] = num;
                } else {
                    minDP[i][j] = Collections.min(getCandis(minDP[i-1], j)) + num;
                    maxDP[i][j] = Collections.max(getCandis(maxDP[i-1], j)) + num;
                }
            }
        }

        System.out.print(Arrays.stream(maxDP[N-1]).max().getAsInt() + " ");
        System.out.print(Arrays.stream(minDP[N-1]).min().getAsInt());
    }

    private static List<Integer> getCandis(int[] array, int index) {
        if (index == 0)
            return List.of(array[0], array[1]);
        else if (index == 1)
            return List.of(array[0], array[1], array[2]);
        else
            return List.of(array[1], array[2]);
    }
}