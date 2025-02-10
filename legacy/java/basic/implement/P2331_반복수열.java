package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;

/**
 * https://www.acmicpc.net/problem/2331
 */
public class P2331_반복수열 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int A = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        ArrayList<Integer> d = new ArrayList<>();
        d.add(A);
        int index = 0;

        while (true) {
            String stringD = d.get(index).toString();
            int nextD = 0;
            for (int i = 0; i < stringD.length(); i++) {
                nextD += (int) Math.pow(Integer.parseInt(stringD.substring(i, i+1)), P);
            }

            if (d.contains(nextD)) {
                System.out.println(d.indexOf(nextD));
                break;
            } else {
                d.add(nextD);
                index++;
            }
        }
    }
}