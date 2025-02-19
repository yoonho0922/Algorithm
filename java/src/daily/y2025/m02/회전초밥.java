package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 회전초밥 {

    static int N;
    static int D;
    static int K;
    static int C;
    static List<Integer> nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        nums = new ArrayList<>();
        for (int i = 0; i< N; i++) {
            nums.add(Integer.parseInt(br.readLine()));
        }
        nums.addAll(nums);

        int answer = 1;
        for (int i = 0; i < N; i++) {
            HashSet<Integer> hs = new HashSet<>(3000, 1.0f);
            hs.add(C);
            for (int j = i; j < i + K; j++) {
                hs.add(nums.get(j));
            }
            answer = Math.max(answer, hs.size());
        }

        System.out.println(answer);
    }
}
