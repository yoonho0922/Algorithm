package daily.y2025.m03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 모음의개수 {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        String vowels = "aeiou";
        int cnt = 0;

        for (char c : str.toCharArray()) {
            if (vowels.indexOf(c) != -1) {
                cnt++;
            }
        }

        System.out.println(cnt);
    }

}
