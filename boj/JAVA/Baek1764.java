import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int nhCnt = 0;
        int nsCnt = 0;
        int Cnt = 0;
        HashSet<String> nhSet = new HashSet<>();
        ArrayList<String> list = new ArrayList<>();

        nhCnt = sc.nextInt();
        nsCnt = sc.nextInt();

        for(int i = 0; i<nhCnt; i++) {
            String nh = sc.next();
            nhSet.add(nh);
        }
        for(int i = 0; i<nsCnt; i++){
            String ns = sc.next();
            if(nhSet.contains(ns)){
                list.add(ns);
                Cnt++;
            }
        }

        Collections.sort(list);
        System.out.println(Cnt);
        for(int i = 0; i<Cnt; i++){
            System.out.println(list.get(i));
        }
    }
}
