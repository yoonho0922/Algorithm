package daily.y2025.m02;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Objects;

public class 충돌위험찾기 {

    public static void main(String[] args) {
        int[][] points = {{3, 2}, {6, 4}, {4, 7}, {1, 4}};
        int[][] routes = {{4, 2}, {1, 3}, {2, 4}};
        System.out.println(solution(points, routes));
    }

    public static int solution(int[][] points, int[][] routes) {
        ArrayList<ArrayList<Point>> paths = new ArrayList<>();
        int answer = 0;
        int maxPathSize = 0;

        for (int i = 0; i < routes.length; i++) {
            ArrayList<Point> path = new ArrayList<>();
            path.add(new Point(points[routes[i][0] - 1]));
            for (int j = 0; j < routes[i].length - 1; j++) {
                Point start = new Point(points[routes[i][j] - 1]);
                Point end = new Point(points[routes[i][j+1] - 1]);
                path.addAll(getPath(start, end));
            }
//            for (Point c : path) {
//                System.out.print(c + " ");
//            }
//            System.out.println();
            maxPathSize = Math.max(maxPathSize, path.size());
            paths.add(path);
        }

        for (int step = 0; step < maxPathSize; step++) {
            // 현재 스텝에서 겹치는 포인트 저장
            HashMap<Point, Integer> hs = new HashMap<>();
            for (ArrayList<Point> path : paths) {
                if (step < path.size()) {
                    Point curPoint = path.get(step);
                    hs.put(curPoint, hs.getOrDefault(curPoint, 0) + 1);
                }
            }
            // 겹치는 포인트 구하기
            int cnt = 0;
            for (int value : hs.values()) {
                if (value > 1) cnt++;
            }
            answer += cnt;
        }

        return answer;
    }

    private static ArrayList<Point> getPath(Point here, Point target) {
        ArrayList<Point> path = new ArrayList<>();

        while (!here.equals(target)) {
            if (here.y != target.y) {
                here.y = here.y < target.y ? here.y + 1 : here.y - 1;
            } else {
                here.x = here.x < target.x ? here.x + 1 : here.x - 1;
            }
            path.add(new Point(here.y, here.x));
        }
        return path;
    }


    static class Point {

        int y, x;

        Point(int y, int x) {
            this.y = y;
            this.x = x;
        }

        Point(int[] c) {
            this.y = c[0];
            this.x = c[1];
        }

        @Override
        public boolean equals(Object o) {
            if (o == null || o.getClass() != getClass()) {
                return false;
            }
            Point p = (Point) o;
            return p.y == y && p.x == x;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        @Override
        public String toString() {
            return y + "," + x;
        }
    }
}
