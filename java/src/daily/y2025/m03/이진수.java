package daily.y2025.m03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 이진수 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int num = Integer.parseInt(br.readLine());
            int index = 0;
            while (num > 0) {
                if (num % 2 == 1) {
                    sb.append(index).append(' ');
                }
                num /= 2;
                index++;
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }

}
