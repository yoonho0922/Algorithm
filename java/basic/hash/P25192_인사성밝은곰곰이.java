import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;

public class P25192_인사성밝은곰곰이 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        HashSet<String> hs = new HashSet<>();
        int helloCount = 0;
        while (t-- > 0) {
            String input = br.readLine();
            if (input.equals("ENTER")){
                hs.clear();
            } else {
                if (hs.add(input))
                    helloCount += 1;
            }
        }
        System.out.println(helloCount);
    }
}