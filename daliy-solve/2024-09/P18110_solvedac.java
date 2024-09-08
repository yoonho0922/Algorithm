import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class P18110_solvedac {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] difficulties = new long[N];
        for (int i = 0; i < N; i++)
            difficulties[i] = Long.parseLong(br.readLine());
        Arrays.sort(difficulties);

        long sum = 0;
        int excludedCount = (int) Math.round(N * 0.15);
        for (int i = excludedCount; i < N - excludedCount; i++)
            sum += difficulties[i];

        System.out.println(Math.round((float) sum / (N - excludedCount * 2)));
    }
}