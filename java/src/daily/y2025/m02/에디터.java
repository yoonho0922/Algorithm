package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 에디터 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        String s = br.readLine();
        Stack<Character> front = new Stack<>();
        Stack<Character> back = new Stack<>();
        for (char c : s.toCharArray()) {
            front.add(c);
        }
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            switch (st.nextToken()) {
                case "L" : if (!front.isEmpty()) back.add(front.pop());
                break;
                case "D" : if (!back.isEmpty()) front.add(back.pop());
                break;
                case "B" : if (!front.isEmpty()) front.pop();
                break;
                case "P" : front.add(st.nextToken().charAt(0));
            }
        }
        for (char c : front) {
            sb.append(c);
        }
        while (!back.isEmpty()) {
            sb.append(back.pop());
        }
        System.out.println(sb);
    }
}
