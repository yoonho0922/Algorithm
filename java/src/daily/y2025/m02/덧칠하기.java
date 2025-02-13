package daily.y2025.m02;

public class 덧칠하기 {

    public static void main(String[] args) {
        System.out.println(solution(8, 4, new int[]{2, 3, 6}));
    }

    public static int solution(int n, int m, int[] section) {
        boolean[] todo = new boolean[n+1];
        for (int s : section) {
            todo[s] = true;
        }
        int cur = 0;
        int answer = 0;
        while (cur <= n) {
            if (todo[cur]) {
                answer++;
                cur += m;
            } else {
                cur++;
            }
        }
        return answer;
    }
}
