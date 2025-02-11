// https://www.acmicpc.net/problem/2828
package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 사과담기게임_미해결 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        final int N = Integer.parseInt(st.nextToken());
        final int M = Integer.parseInt(st.nextToken());
        final int J = Integer.parseInt(br.readLine());
        int[] apples = new int[J];
        for (int t = 0; t < J; t++) {
            apples[t] = Integer.parseInt(br.readLine());
        }
        int answer = 0;
        int start = 0;
        int end = 0;
        int diff = 0;
        while (end < J) {
            if (end == J - 1) {
                answer += Math.max(0, Math.abs(apples[end] - apples[start]) - M + 1);
            } else {
                int cur_diff = apples[end+1] - apples[end];
                if (cur_diff * diff < 0) { // 변화 있음
                    answer += Math.max(0, Math.abs(apples[end] - apples[start]) - M + 1);
                    start = end;
                }
                diff = cur_diff;
            }
            end++;
        }
        System.out.println(answer);
    }
}
