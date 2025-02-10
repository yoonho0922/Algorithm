import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int n = N;
        StringBuilder answer = new StringBuilder();

        while (n != 0) {
            int mod = n % B;
            if (mod < 10) {
                answer.append(mod);
            } else {
                char c = (char) ((int) 'A' + (mod - 10));
                answer.append(c);
            }
            n = n / B;
        }

        System.out.println(answer.reverse());
    }
}
