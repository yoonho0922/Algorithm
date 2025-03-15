package daily.y2025.m03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 칸토어집합 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;

        String[] cantos = initCantos(12);

        while ((input = br.readLine()) != null) {
            int n = Integer.parseInt(input);
            System.out.println(cantos[n]);
        }
    }

    private static String[] initCantos(int maxValue) {
        String[] cantos = new String[maxValue + 1];
        cantos[0] = "-";

        for (int i = 1; i <= maxValue; i++) {
            StringBuilder gap = new StringBuilder();
            for (int j = 0; j < cantos[i - 1].length(); j++) {
                gap.append(" ");
            }
            cantos[i] = cantos[i-1] + gap + cantos[i-1];
        }

        return cantos;
    }

}
