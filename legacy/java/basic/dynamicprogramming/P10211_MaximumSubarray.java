import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P10211_MaximumSubarray {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int[] array = new int[N];
            for (int i = 0; i < N; i++)
                array[i] = Integer.parseInt(st.nextToken());
            System.out.println(getMaximumSubArraySum(N, array));
        }
    }

    private static int getMaximumSubArraySum(int n, int[] array) {
        int[] dp = new int[n];
        dp[0] = array[0];
        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(array[i], dp[i-1] + array[i]);
        }
        return Arrays.stream(dp).max().getAsInt();
    }
}