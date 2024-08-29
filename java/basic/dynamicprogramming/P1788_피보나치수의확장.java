import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    static int MODULO = 1_000_000_000;
    static int MAX_ABS = 1_000_000;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int LENGTH = MAX_ABS * 2 + 1;
        int[] fibo = new int[LENGTH];
        fibo[MAX_ABS] = 0; // N=0의 위치
        fibo[MAX_ABS + 1] = 1; // N=1의 위치

        for (int i = MAX_ABS - 1; i >= 0; i--)
            fibo[i] = (fibo[i+2] - fibo[i+1]) % MODULO;
        for (int i = MAX_ABS + 2; i < LENGTH; i++)
            fibo[i] = (fibo[i-1] + fibo[i-2]) % MODULO;

        int answer = fibo[MAX_ABS + N];

        if (answer > 0 ) System.out.println(1);
        else if (answer == 0 ) System.out.println(0);
        else System.out.println(-1);

        System.out.println(Math.abs(answer));
    }
}