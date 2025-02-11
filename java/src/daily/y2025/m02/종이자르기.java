package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class 종이자르기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int W = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());
        ArrayList<Integer> yPoints = new ArrayList<>(Arrays.asList(0, H));
        ArrayList<Integer> xPoints = new ArrayList<>(Arrays.asList(0, W));
        for (int t = 0; t < K; t++) {
            st = new StringTokenizer(br.readLine(), " ");
            int type = Integer.parseInt(st.nextToken());
            int point = Integer.parseInt(st.nextToken());
            if (type == 0) {
                yPoints.add(point);
            } else {
                xPoints.add(point);
            }
        }

        Collections.sort(yPoints);
        Collections.sort(xPoints);

        System.out.println(getMaxLength(yPoints) * getMaxLength(xPoints));
    }

    private static int getMaxLength(ArrayList<Integer> points) {
        int length = 0;
        for (int i = 0; i < points.size() - 1; i++) {
            int cur_length = points.get(i + 1) - points.get(i);
            if (cur_length > length) length = cur_length;
        }
        return length;
    }
}
