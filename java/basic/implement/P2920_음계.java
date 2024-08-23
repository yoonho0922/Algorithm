import java.io.*;
import java.util.StringTokenizer;

public class P2920_음계 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int[] peaches = new int[8];

        for (int i = 0; i < 8; i++) {
            peaches[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(check(peaches));
    }

    private static String check(int[] peaches) {
        int gap = peaches[0] - peaches[1];

        for (int i = 1; i < 8; i ++) {
            if (peaches[i-1] - peaches[i] != gap) {
                return "mixed";
            }
        }

        if (gap > 0) return "descending";
        else return "ascending";
    }
}
