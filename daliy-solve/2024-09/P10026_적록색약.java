import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    static int N;
    static char[][] grid;
    static boolean[][] visited;

    static int[] dy = {0, 0, 1, -1};
    static int[] dx = {1, -1, 0, 0};

    static class Point {
        int y;
        int x;
        Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) throws Exception {
        input();
        System.out.println(count(false));
        System.out.println(count(true));
    }

    private static int count(boolean redGreenBlind) {
        int cnt = 0;
        visited = new boolean[N][N];
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (!visited[r][c]) {
                    cnt++;
                    bfs(r, c, redGreenBlind);
                }
            }
        }
        return cnt;
    }

    private static void bfs(int sy, int sx, boolean redGreenBlind) {
        Deque<Point> q = new ArrayDeque<>();
        visited[sy][sx] = true;
        q.add(new Point(sy,sx));

        while (!q.isEmpty()) {
            Point now = q.pollFirst();
            for (int i = 0; i < 4; i++) {
                int ny = dy[i] + now.y;
                int nx = dx[i] + now.x;
                if (isInRange(ny, nx) && !visited[ny][nx] && isSameColor(now, ny, nx, redGreenBlind)) {
                    visited[ny][nx] = true;
                    q.add(new Point(ny, nx));
                }
            }
        }
    }

    private static boolean isSameColor(Point now, int ny, int nx, boolean redGreenBlind) {
        if (redGreenBlind)
            return (grid[now.y][now.x] == 'B' && grid[now.y][now.x] == grid[ny][nx])
                || (grid[now.y][now.x] != 'B' && grid[ny][nx] != 'B');
        else
            return grid[now.y][now.x] == grid[ny][nx];
    }

    private static boolean isInRange(int ny, int nx) {
        return (0 <= ny && ny < N) && (0 <= nx && nx < N);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        grid = new char[N][N];
        for (int i = 0; i < N; i++) {
            String row = br.readLine();
            for (int j = 0; j < N; j++)
                grid[i][j] = row.charAt(j);
        }
    }
}