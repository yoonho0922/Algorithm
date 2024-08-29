import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    static int N = 10;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            Integer[] arr = new Integer[N];
            for (int i = 0; i < N; i++)
                arr[i] = Integer.parseInt(st.nextToken());
            Arrays.sort(arr, Collections.reverseOrder());
            System.out.println(arr[2]);
        }
    }
}