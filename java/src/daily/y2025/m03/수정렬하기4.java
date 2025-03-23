package daily.y2025.m03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class 수정렬하기4 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> nums = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            nums.add(-Integer.parseInt(br.readLine()));
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            sb.append(-nums.poll()).append('\n');
        }

        System.out.println(sb);
    }
}
