package daily.y2025.m02;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 블로그 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int max = Arrays.stream(nums, 0, X).sum();
        System.out.println(max);
        int cnt = 1;
        int cur = max;
        for (int i = 1; i < N - X + 1; i++) {
            cur = cur - nums[i - 1] + nums[i + X - 1];
            if (cur == max) {
                cnt++;
            } else if (cur > max) {
                max = cur;
                cnt = 1;
            }
        }

        if (max == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(max);
            System.out.println(cnt);
        }
    }

}
