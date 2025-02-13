package daily.y2025.m02;

public class 바탕화면정리 {

    public static void main(String[] args) {
        int[] answer = solution(new String[]{"..........", ".....#....", "......##..", "...##.....", "....#....."});
        for (int a : answer) {
            System.out.print(a + " ");
        }
    }

    public static int[] solution(String[] wallpaper) {
        int[] answer = {100, 100, -1, -1};
        int R = wallpaper.length;
        int C = wallpaper[0].length();
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (wallpaper[r].charAt(c) == '#') {
                    answer[0] = Math.min(answer[0], r);
                    answer[1] = Math.min(answer[1], c);
                    answer[2] = Math.max(answer[2], r + 1);
                    answer[3] = Math.max(answer[3], c + 1);
                }
            }
        }
        return answer;
    }
}
