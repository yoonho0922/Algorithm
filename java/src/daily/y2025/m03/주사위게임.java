package daily.y2025.m03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 주사위게임 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int cyScore = 100;
        int sdScore = 100;

        for (int i = 0; i < N; i++) {
            st  = new StringTokenizer(br.readLine());
            int cyPoint = Integer.parseInt(st.nextToken());
            int sdPoint = Integer.parseInt(st.nextToken());

            if (cyPoint > sdPoint) {
                sdScore -= cyPoint;
            } else if (cyPoint < sdPoint) {
                cyScore -= sdPoint;
            }
        }
        System.out.println(cyScore);
        System.out.println(sdScore);
    }

}
