package daily.y2025.m02;

public class 둘만의암호 {

    public static void main(String[] args) {
        System.out.println(solution("aukks","wbqd",5));
    }

    public static String solution(String s, String skip, int index) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            for (int i = 0; i < index; i++) {
                c = c == 'z' ? 'a' : (char) (c + 1);
                if (skip.indexOf(c) != -1) {
                    i--;
                }
            }
            sb.append(c);
        }
        return sb.toString();
    }

}
