import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.IntStream;

public class 볼모으기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String balls = br.readLine();

        int answer = IntStream.of(
            count(rstrip(balls, 'B'), 'B'),
            count(lstrip(balls, 'B'), 'B'),
            count(rstrip(balls, 'R'), 'R'),
            count(lstrip(balls, 'R'), 'R')
        ).min().orElseThrow(() -> new IllegalStateException("잘못된 입력입니다."));

        System.out.println(answer);
    }

    private static String rstrip(String balls, char r) {
        for (int i = balls.length() - 1; i > 0; i--) {
            if (balls.charAt(i) != r) {
                return balls.substring(0, i + 1);
            }
        }
        return "";
    }

    private static String lstrip(String balls, char r) {
        for (int i = 0; i < balls.length(); i++) {
            if (balls.charAt(i) != r) {
                return balls.substring(i);
            }
        }
        return "";
    }

    private static int count(String r, char b) {
        return (int) r.chars().filter(c -> c == b).count();
    }
}
