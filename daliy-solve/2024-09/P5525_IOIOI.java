import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int LENGTH = Integer.parseInt(br.readLine());
        String s = br.readLine();


        int left = 0, right = 0, answer = 0, cntOI = 0;

        while (left < LENGTH) {
            if (s.charAt(left) == 'I') {
                right += 2;
                if (right >= LENGTH) break;

                if (s.subSequence(right-1, right+1).equals("OI")) {
                    cntOI ++;
                    if (cntOI == N) {
                        answer ++;
                        cntOI --;
                        left += 2;
                    }
                } else {
                    right --;
                    left = right;
                    cntOI = 0;
                }
            } else {
                left ++;
                right ++;
            }
        }

        System.out.println(answer);
    }
}