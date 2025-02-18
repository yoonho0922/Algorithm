package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class IF문좀대신짜줘 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<Type> types = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            types.add(new Type(st.nextToken(), Integer.parseInt(st.nextToken())));
        }
        for (int i = 0; i < M; i++) {
            int value = Integer.parseInt(br.readLine());
            int start = 0;
            int end = N-1;
            while (start <= end) {
                int mid = (start + end) / 2;
                if (value > types.get(mid).maxVal) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
            sb.append(types.get(end+1).name).append('\n');
        }
        System.out.println(sb);
    }

    public static class Type {
        String name;
        int maxVal;

        Type(String name, int maxVal) {
            this.name = name;
            this.maxVal = maxVal;
        }
    }
}
