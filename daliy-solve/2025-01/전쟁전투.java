import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 전쟁전투 {

    static int N;
    static int M;

    static char matrix[][];
    static boolean visited[][];

    static int dirY[] = {-1, 1, 0, 0};
    static int dirX[] = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        matrix = new char[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < M; j++) {
                char ch = str.charAt(j);
                matrix[i][j] = ch;
            }
        }

        int whitePower = getPower('W');
        int bluePower = getPower('B');
        System.out.println(whitePower + " " + bluePower);
    }

    private static int getPower(char type) {
        int power = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!visited[i][j] && matrix[i][j] == type) {
                    int count = countByBfs(i, j, type);
                    power += (int) Math.pow(count, 2);
                }
            }
        }
        return power;
    }

    private static int countByBfs(int startY, int startX, char type) {
        int count = 1;
        Queue<Point> q = new LinkedList<>();
        visited[startY][startX] = true;
        q.offer(new Point(startY, startX));

        while (!q.isEmpty()) {
            Point here = q.poll();
            for (int i = 0; i < 4; i++) {
                int nextY = here.y + dirY[i];
                int nextX = here.x + dirX[i];
                if (0 <= nextY && nextY < N && 0 <= nextX && nextX < M
                    && !visited[nextY][nextX] && matrix[nextY][nextX] == type) {
                    count++;
                    visited[nextY][nextX] = true;
                    q.offer(new Point(nextY, nextX));
                }
            }
        }
        return count;
    }

    private static class Point {

        int y;
        int x;

        Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}
