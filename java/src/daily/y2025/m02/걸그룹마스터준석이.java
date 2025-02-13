package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class 걸그룹마스터준석이 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String, ArrayList<String>> teams = new HashMap<>();
        HashMap<String, String> members = new HashMap<>();

        for (int i = 0; i < N; i++) {
            String teamName = br.readLine();
            int K = Integer.parseInt(br.readLine());
            ArrayList<String> memberNames = new ArrayList<>();
            for (int j = 0; j < K; j++) {
                String memberName = br.readLine();
                memberNames.add(memberName);
                members.put(memberName, teamName);
            }
            Collections.sort(memberNames);
            teams.put(teamName, memberNames);
        }

        for (int i = 0; i < M; i++) {
            String name = br.readLine();
            int cmd = Integer.parseInt(br.readLine());
            if (cmd == 0) {
                ArrayList<String> memberNames = teams.get(name);
                for (String teamName : memberNames) {
                    sb.append(teamName).append('\n');
                }
            } else {
                sb.append(members.get(name)).append('\n');
            }
        }

        System.out.println(sb);
    }
}
