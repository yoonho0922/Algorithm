package daily.y2025.m02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 랭킹전대기열 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        ArrayList<ArrayList<Player>> rooms = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int level = Integer.parseInt(st.nextToken());
            String name = st.nextToken();

            int selected = -1;
            for (int j = 0; j < rooms.size(); j++) {
                int roomLv = rooms.get(j).get(0).level;
                if (rooms.get(j).size() < M && roomLv - 10 <= level && level <= roomLv + 10) {
                    selected = j;
                    break;
                }
            }

            Player player = new Player(name, level);
            if (selected == -1) {
                ArrayList<Player> newRoom = new ArrayList<>();
                newRoom.add(player);
                rooms.add(newRoom);
            } else {
                rooms.get(selected).add(player);
            }
        }

        for (ArrayList<Player> room : rooms) {
            if (room.size() == M) {
                sb.append("Started!").append('\n');
            } else {
                sb.append("Waiting!").append('\n');
            }
            // 사전순 정렬
            room.sort((a, b) -> a.name.compareTo(b.name));
            for (Player p : room) {
                sb.append(p.level).append(' ').append(p.name).append('\n');
            }
        }
        System.out.println(sb);
    }

    public static class Player {
        String name;
        int level;

        public Player(String name, int level) {
            this.name = name;
            this.level = level;
        }

    }
}
