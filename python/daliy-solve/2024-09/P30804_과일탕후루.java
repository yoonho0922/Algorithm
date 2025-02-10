import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class P30804_과일탕후루 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] fruits = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++)
            fruits[i] = Integer.parseInt(st.nextToken());

        Map<Integer, Integer> hs = new HashMap<>();
        int right = 0;
        int left = 0;
        int nowCount = 0;
        int answer = 0;

        while (right < N) {
            // right에 있는 과일 수 증가, 새로운 과일이라면 현재 카운트도 증가
            if (hs.getOrDefault(fruits[right], 0) == 0)
                nowCount++;
            hs.put(fruits[right], hs.getOrDefault(fruits[right], 0) + 1);

            // 현재 카운트가 2 이하가 될 때까지 left를 옮김
            while (nowCount > 2) {
                // left에 있는 과일 제거
                hs.put(fruits[left], hs.get(fruits[left]) - 1);
                if (hs.get(fruits[left]) == 0)
                    nowCount--;
                left++;
            }

            // 결과 값 업데이트
            answer = Math.max(answer, right - left + 1);
            right++;
        }

        System.out.println(answer);
    }
}
