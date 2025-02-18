package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 타노스 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String s = br.readLine();
        int zero = 0;
        int one = 0;
        for (char c : s.toCharArray()) {
            if (c == '0') zero++;
            else one++;
        }
        zero /= 2;
        one /= 2;
        for (char c : s.toCharArray()) {
            if (c == '0') {
                if (zero > 0) {
                    sb.append('0');
                    zero--;
                }
            } else {
                if (one == 0) {
                    sb.append('1');
                } else {
                    one--;
                }
            }
        }
        System.out.println(sb);
    }
}
