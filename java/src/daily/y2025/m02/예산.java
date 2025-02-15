package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 예산 {

    static int N;
    static int M;
    static int max_req;
    static int[] requests;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        requests = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            requests[i] = Integer.parseInt(st.nextToken());
            max_req = Math.max(max_req, requests[i]);
        }
        M = Integer.parseInt(br.readLine());

        int start = 0;
        int end = max_req;
        int answer = 0;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (getTotal(mid) <= M) {
                start = mid + 1;
                answer = mid;
            } else {
                end = mid - 1;
            }
        }
        System.out.println(answer);
    }

    private static int getTotal(int limit) {
        int total = 0;
        for (int r : requests) {
            if (r < limit) {
                total += r;
            } else {
                total += limit;
            }
        }
        return total;
    }
}
