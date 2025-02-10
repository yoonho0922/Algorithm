import java.io.BufferedReader;
import java.io.InputStreamReader;

public class P5597_과제안내신분 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = 30;
        int M = 28;
        boolean[] submit = new boolean[N + 1];
        for (int i = 0; i < M; i++)
            submit[Integer.parseInt(br.readLine())] = true;
        for (int i = 1; i < N + 1; i++){
            if (!submit[i])
                System.out.println(i);
        }
    }
}