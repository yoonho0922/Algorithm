package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 단어나누기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String S = br.readLine();
        String answer = "";
        for (int i = 1; i < S.length() - 1; i++) {
            for (int j = i + 1; j < S.length(); j++) {
                StringBuffer a = new StringBuffer(S.substring(0, i)).reverse();
                StringBuffer b = new StringBuffer(S.substring(i, j)).reverse();
                StringBuffer c = new StringBuffer(S.substring(j)).reverse();
                String result = a.append(b).append(c).toString();
                if (answer.isEmpty() || result.compareTo(answer) < 0) {
                    answer = result;
                }
            }
        }
        System.out.println(answer);
    }

}
