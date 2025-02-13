package daily.y2025.m02;

import java.util.HashMap;

public class 대충만든자판 {

    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        HashMap<Character, Integer> hs = new HashMap<>();
        for (String keys : keymap) {
            for (int i = 0; i < keys.length(); i++) {
                char key = keys.charAt(i);
                hs.put(key, Math.min(hs.getOrDefault(key, 100), i + 1));
            }
        }

        for (char c : hs.keySet()) {
            System.out.println(c + " " + hs.get(c));
        }

        for (int i = 0; i < targets.length; i++) {
            String target = targets[i];
            int cnt = 0;
            for (int j = 0; j < target.length(); j++) {
                if (hs.containsKey(target.charAt(j))) {
                    cnt += hs.get(target.charAt(i));
                } else {
                    cnt = -1;
                    break;
                }
            }
            answer[i] = cnt;
        }

        return answer;
    }
}
