package algorithm;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Map;

public class Interview20 {

    public boolean isValid(String s) {

        Map<Character, Character> matchingBrackets = Map.of(')', '(', '}', '{', ']', '[');
        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (matchingBrackets.containsValue(c)) { // Open bracket
                stack.push(c);
            } else if (matchingBrackets.containsKey(c)) { // Close bracket
                if (stack.isEmpty() || stack.pop() != matchingBrackets.get(c)) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
