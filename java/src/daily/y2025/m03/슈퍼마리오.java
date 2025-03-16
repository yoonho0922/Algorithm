package daily.y2025.m03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 슈퍼마리오 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int score = 0;
        int target = 100;
        boolean stop = false;
        for (int i = 0; i < 10; i++) {
            int mushroom = Integer.parseInt(br.readLine());
            if (!stop && Math.abs(target - (score + mushroom)) <= Math.abs(100 - score)) {
                score += mushroom;
            } else {
                stop = true;
            }
        }
        System.out.println(score);
    }

}
