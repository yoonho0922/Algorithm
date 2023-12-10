import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String str = sc.next().toUpperCase();

        int cnt[] = new int[26];
        int max = 0;
        char result = '?';

        for(int i = 0; i<str.length(); i++){
            int tmp = str.charAt(i) - 65;
            cnt[tmp]++;
            if(max < cnt[tmp]){
                max = cnt[tmp];
                result = str.charAt(i);
            }else if(max == cnt[tmp]){
                result = '?';
            }
        }
        System.out.println(result);
    }
}
