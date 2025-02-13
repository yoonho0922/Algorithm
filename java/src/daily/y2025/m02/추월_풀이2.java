package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

public class 추월_풀이2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        HashMap<String, Integer> hs = new HashMap<>();
        for (int i = 0; i < N; i++) {
            hs.put(br.readLine(), i);
        }

        String[] exits = new String[N];
        for (int i = 0; i < N; i++) {
            exits[i] = br.readLine();
        }

        int[] exitMins = new int[N];
        exitMins[N-1] = hs.get(exits[N-1]);
        for (int i = N-2; i > -1; i--) {
            exitMins[i] = Math.min(hs.get(exits[i]), exitMins[i + 1]);
        }

        int answer = 0;
        for (int i = 0; i < N - 1; i++) {
            if (hs.get(exits[i]) > exitMins[i+1])
                answer++;
        }

        System.out.println(answer);
    }
}
