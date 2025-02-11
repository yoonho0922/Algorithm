package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class BaseConversion {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(br.readLine());

        // A to Decimal
        st = new StringTokenizer(br.readLine(), " ");
        int decimal = 0;
        for (int i = M - 1; i > -1; i--) {
            decimal += Integer.parseInt(st.nextToken()) * (int) Math.pow(A, i);
        }

        // B to Decimal
        ArrayList<Integer> result = new ArrayList<>();
        while (decimal > 0) {
            result.add(decimal % B);
            decimal /= B;
        }

        Collections.reverse(result);
        result.forEach(n -> System.out.print(n + " "));
    }
}
