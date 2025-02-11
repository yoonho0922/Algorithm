package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Map;
import java.util.TreeMap;

public class 파일정리 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());

        Map<String, Integer> hm = new TreeMap<>();
        for (int i = 0; i < N; i++) {
            String ext = br.readLine().split("\\.")[1];
            hm.put(ext, hm.getOrDefault(ext, 0) + 1);
        }
        for(String key : hm.keySet()) {
            sb.append(key).append(" ").append(hm.get(key)).append("\n");
        }
        bw.write(sb.toString());
        bw.close();
    }
}
