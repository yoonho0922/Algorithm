package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 햄버거분배 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        String s = br.readLine();
        boolean[] eat = new boolean[N];
        int answer = 0;
        for (int i = 0; i < N; i++) {
            if (s.charAt(i) == 'P') {
                for (int j = i - K; j < i + K + 1; j++) {
                    if (0 <= j && j < N && s.charAt(j) == 'H' && !eat[j]) {
                        eat[j] = true;
                        answer++;
                        break;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
