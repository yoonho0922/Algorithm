// https://www.acmicpc.net/problem/5800
package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 성적통계 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());
        for (int t = 1; t < K + 1; t++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(st.nextToken());
            int[] records = new int[N];
            for (int i = 0; i < N; i++)
                records[i] = Integer.parseInt(st.nextToken());

            Arrays.sort(records);
            int max = records[N-1];
            int min = records[0];
            int largestGap = 0;
            for (int i = 1; i < N; i++)
                largestGap = Math.max(largestGap, records[i] - records[i-1]);

            System.out.printf("Class %d\nMax %d, Min %d, Largest gap %d\n", t, max, min, largestGap);
        }
    }
}