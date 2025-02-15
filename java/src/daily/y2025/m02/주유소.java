package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 주유소 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] roads = new long[N-1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N -1; i++) {
            roads[i] = Long.parseLong(st.nextToken());
        }
        long[] stations = new long[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            stations[i] = Long.parseLong(st.nextToken());
        }

        long answer = 0;
        long minPrice = stations[0];
        for (int i = 0; i < N -1; i++) {
            minPrice = Math.min(minPrice, stations[i]);
            answer += minPrice * roads[i];
        }
        System.out.println(answer);
    }
}
