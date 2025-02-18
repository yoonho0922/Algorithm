package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class KCPC {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int[][] scores = new int[n][k];
            List<Team> teams = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                teams.add(new Team(j+1));
            }

            //  점수 업데이트
            for (int j = 0; j < m; j++) {
                st = new StringTokenizer(br.readLine());
                int teamIdx = Integer.parseInt(st.nextToken()) - 1;
                int question = Integer.parseInt(st.nextToken()) - 1;
                int score = Integer.parseInt(st.nextToken());
                if (score > scores[teamIdx][question]) {
                    teams.get(teamIdx).score += score - scores[teamIdx][question];
                    scores[teamIdx][question] = score;
                }
                teams.get(teamIdx).cnt++;
                teams.get(teamIdx).last = j;
            }

            // 점수 내림차순, 제출 오름차순, 마지막제출 오름차순 정렬
            Collections.sort(teams);

            // 등수 찾기
            for (int j = 0; j < n; j++) {
                if (teams.get(j).id == t) {
                    sb.append(j+1).append('\n');
                }
            }
        }
        System.out.println(sb);
    }

    public static class Team implements Comparable<Team> {
        int id;
        int score;
        int cnt;
        int last;

        public Team(int id){
            this.id = id;
        }

        @Override
        public int compareTo(Team o) {
            if (this.score != o.score) {
                return o.score - this.score; // 내림차순
            } else if (this.cnt != o.cnt) {
                return this.cnt - o.cnt; // 오름차순
            } else {
                return this.last - o.last; // 오름차순
            }
        }
    }
}
