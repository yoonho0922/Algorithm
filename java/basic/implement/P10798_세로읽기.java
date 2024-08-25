import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        int N = 5;
        int M = 15;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] words = new String[5];
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }

        StringBuilder answer = new StringBuilder();

        for (int c = 0; c < M; c++) {
            for (int r = 0; r < N; r++) {
                if (c < words[r].length()) {
                    answer.append(words[r].charAt(c));
                }
            }
        }

        System.out.println(answer);
        br.close();
    }

}
