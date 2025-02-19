package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 볼모으기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String balls = br.readLine();
        String reverseBalls = (new StringBuilder(balls)).reverse().toString();

        int answer = count(balls, 'R');
        answer = Math.min(answer, count(reverseBalls, 'R'));
        answer = Math.min(answer, count(balls, 'B'));
        answer = Math.min(answer, count(reverseBalls, 'B'));
        System.out.println(answer);
    }

    public static int count(String s, char target) {
        int start = 1;
        for (char c : s.toCharArray()) {
            if (c != target)
                break;
            start++;
        }
        int cnt = 0;
        for (int i = start; i < s.length(); i++) {
            if (s.charAt(i) == target)
                cnt++;
        }
        return cnt;
    }
}
