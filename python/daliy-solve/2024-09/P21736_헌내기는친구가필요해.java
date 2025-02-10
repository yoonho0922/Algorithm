import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int[] DY = {1, -1, 0, 0};
    static int[] DX = {0, 0, 1, -1};

    static class Point {
        int y, x;
        Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Point start = null;
        char[][] grid = new char[N][M];
        for (int i = 0; i < N; i++) {
            String row = br.readLine();
            for (int j = 0; j < M; j++) {
                grid[i][j] = row.charAt(j);
                if (grid[i][j] == 'I')
                    start = new Point(i, j);
            }
        }

        boolean[][] visited = new boolean[N][M];
        Queue<Point> q = new LinkedList<>();
        q.add(start);
        visited[start.y][start.x] = true;

        int answer = 0;

        while (!q.isEmpty()) {
            Point now = q.poll();
            for (int i = 0; i < 4; i++) {
                int ny = now.y + DY[i];
                int nx = now.x + DX[i];
                if ((0 <= ny && ny < N) && (0 <= nx && nx < M) && !visited[ny][nx] && grid[ny][nx] != 'X') {
                    visited[ny][nx] = true;
                    q.add(new Point(ny, nx));
                    if (grid[ny][nx] == 'P') {
                        answer++;
                    }
                }
            }
        }

        if (answer > 0)
            System.out.println(answer);
        else
            System.out.println("TT");
    }
}