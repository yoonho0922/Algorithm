package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 가희와키워드 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        HashSet<String> hs = new HashSet<>();
        for (int i = 0; i < N; i++) {
            hs.add(br.readLine());
        }
        for (int i = 0; i < M; i++) {
            String[] words = br.readLine().split(",");
            for (String w : words) {
                hs.remove(w);
            }
            sb.append(hs.size()).append('\n');
        }
        System.out.println(sb);
    }
}
