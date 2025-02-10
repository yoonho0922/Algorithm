import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        HashSet<Long> setA = new HashSet<>();
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < A; i++)
            setA.add(Long.parseLong(st.nextToken()));
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < B; i++)
            setA.remove(Long.parseLong(st.nextToken()));

        System.out.println(setA.size());
        System.out.println(setA.stream()
                .sorted()
                .map(String::valueOf)
                .collect(Collectors.joining(" ")));
    }
}