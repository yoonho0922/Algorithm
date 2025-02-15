package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 수이어쓰기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        int num = 0;
        int idx = 0;
        while (idx < S.length()) {
            num++;
            String strNum = String.valueOf(num);
            for (char c : strNum.toCharArray()) {
                if (idx < S.length() && c == S.charAt(idx)) {
                    idx++;
                }
            }
        }
        System.out.println(num);
    }
}
