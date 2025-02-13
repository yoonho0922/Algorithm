package daily.y2025.m02;

public class 카드뭉치 {

    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        int a = 0;
        int b = 0;

        for (String word : goal) {
            if (a < cards1.length && cards1[a].equals(word)) {
                a++;
            } else if (b < cards2.length && cards2[b].equals(word)) {
                b++;
            } else {
                answer = "No";
            }
        }

        return answer;
    }
}
