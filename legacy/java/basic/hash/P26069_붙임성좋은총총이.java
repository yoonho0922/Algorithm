import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class P26069_붙임성좋은총총이 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        HashSet<String> dancers = new HashSet<>();
        dancers.add("ChongChong");
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String a = st.nextToken();
            String b = st.nextToken();
            if (dancers.contains(b))
                dancers.add(a);
            if (dancers.contains(a))
                dancers.add(b);
        }
        System.out.println(dancers.size());
    }
}