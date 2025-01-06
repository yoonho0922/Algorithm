package algorithm;

import java.util.HashMap;
import java.util.Map;

public class Interview383 {

    public boolean canConstruct(String ransomNote, String magazine) {

        Map<Character, Integer> map = new HashMap<>();

        initMap(map, magazine);

        for (char c : ransomNote.toCharArray()) {
            if (map.getOrDefault(c, 0) != 0) {
                map.put(c, map.get(c) - 1);
            } else {
                return false;
            }
        }

        return true;
    }

    private void initMap(Map<Character, Integer> map, String words) {

        for (char c : words.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
    }
}
