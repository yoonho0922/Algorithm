import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        long N = Long.parseLong(st.nextToken());
        long C = Long.parseLong(st.nextToken());
        ArrayList<Long> nums = new ArrayList<>();
        HashMap<Long, Long> hm = new HashMap<>();
        st = new StringTokenizer(br.readLine(), " ");

        for (int i = 0; i < N; i++) {
            long num = Long.parseLong(st.nextToken());
            nums.add(num);
            hm.put(num, hm.getOrDefault(num, 0L) + 1);
        }

        List<Long> answer = nums.stream()
                .sorted((o1, o2) -> {
                    // override public int compare(Long o1, Long o2)
                    if (hm.get(o1).equals(hm.get(o2)))
                        return nums.indexOf(o1) - nums.indexOf(o2);
                    return hm.get(o2).compareTo(hm.get(o1));
                })
                .toList();
        System.out.println(answer.stream()
                .map(String::valueOf)
                .collect(Collectors.joining(" ")));
    }
}