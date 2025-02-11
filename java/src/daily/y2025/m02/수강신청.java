package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.StringTokenizer;

public class 수강신청 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int K = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        LinkedHashSet<String> hs = new LinkedHashSet<>();

        for (int i = 0; i < L; i++) {
            String id = br.readLine();
            hs.remove(id);
            hs.add(id);
        }

        Iterator<String> it = hs.iterator();
        for (int i = 0; i < K && it.hasNext(); i++) {
            sb.append(it.next()).append('\n');
        }
        System.out.println(sb);
    }
}
