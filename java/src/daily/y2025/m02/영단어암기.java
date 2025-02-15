package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 영단어암기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        HashMap<String, Integer> hm = new HashMap<>();
        for (int i = 0; i < N; i++) {
            String w = br.readLine();
            if (w.length() >= M) {
                hm.put(w, hm.getOrDefault(w, 0) + 1);
            }
        }

        List<String> sortedList = new ArrayList<>(hm.keySet());

        sortedList.sort((a, b) -> {
            if (!hm.get(a).equals(hm.get(b)))
                return hm.get(b) - hm.get(a);
            if (a.length() != b.length())
                return b.length() - a.length();
            return a.compareTo(b);
        });

        sortedList.forEach(e -> sb.append(e).append('\n'));
        System.out.println(sb);
    }
}
