package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class 비슷한단어 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String s = br.readLine();
        HashMap<Character, Integer> originCounter = counter(s);
        int answer = 0;
        for (int t = 0; t < N-1; t++) {
            HashMap<Character, Integer> targetCounter = counter(br.readLine());
            if (isSimilar(originCounter, targetCounter)){
                answer++;
            }
        }
        System.out.println(answer);
    }

    public static boolean isSimilar(HashMap<Character, Integer> origin, HashMap<Character, Integer> target) {
        for (char key : origin.keySet()) {
            target.put(key, target.getOrDefault(key, 0) - origin.get(key));
        }
        int less = 0;
        int greater = 0;
        for (int value : target.values()) {
            if (Math.abs(value) >= 2) {
                return false;
            } else if (value == -1) {
                less++;
            } else if (value == 1) {
                greater++;
            }
        }
        return less <= 1 && greater <= 1;
    }

    private static HashMap<Character, Integer> counter(String origin) {
        HashMap<Character, Integer> hm = new HashMap<>();
        for (char c : origin.toCharArray()) {
            hm.put(c, hm.getOrDefault(c, 0) +1);
        }
        return hm;
    }
}
