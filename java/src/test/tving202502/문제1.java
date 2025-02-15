package test.tving202502;

public class 문제1 {

    public static void main(String[] args) {
        int[][] array = {
            {1, 0, 0, 0},
            {0, 0, 0, 1},
            {0, 0, 1, 0},
            {0, 1, 1, 0}
        };
        System.out.println(solution(array, 2));
    }

    public static int solution(int[][] office, int k) {
        int answer = 0;
        int N = office.length;
        for (int i = 0; i < N - k + 1; i++) {
            for (int j = 0; j < N - k + 1; j++) {
                answer = Math.max(answer, count(office, i, j, k));
            }
        }
        return answer;
    }

    private static int count(int[][] office, int r, int c, int k) {
        int cnt = 0;
        for (int i = r; i < r + k; i++) {
            for (int j = c; j < c + k; j++) {
                cnt += office[i][j];
            }
        }
        return cnt;
    }
}
