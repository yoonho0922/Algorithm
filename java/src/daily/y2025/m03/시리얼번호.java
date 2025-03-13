package daily.y2025.m03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 시리얼번호 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(new StringBuilder());

        int N = Integer.parseInt(br.readLine());
        String[] guitars = new String[N];

        for (int i = 0; i < N; i++) {
            guitars[i] = br.readLine();
        }

        Arrays.sort(guitars, (a, b) -> {
            if (a.length() != b.length()) {
                return a.length() - b.length();
            }

            int sumA = sumNumber(a);
            int sumB = sumNumber(b);

            if (sumA != sumB) {
                return sumA - sumB;
            }

            return a.compareTo(b);
        });

        for (String g : guitars) {
            sb.append(g).append('\n');
        }

        System.out.println(sb);
    }

    private static int sumNumber(String str) {
        int sum = 0;
        for (char c : str.toCharArray()) {
            if (Character.isDigit(c)) {
                sum += Character.getNumericValue(c);
            }
        }
        return sum;
    }
}
