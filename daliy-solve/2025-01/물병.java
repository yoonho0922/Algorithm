import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 물병 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int num = N;
        String binary = Integer.toBinaryString(num);

        while (binary.chars().filter(c -> c == '1').count() > K) {
            int index = binary.length() - 1 - binary.lastIndexOf("1");
            num += (int) Math.pow(2, index);
            binary = Integer.toBinaryString(num);
        }

        System.out.println(num - N);
    }
}
