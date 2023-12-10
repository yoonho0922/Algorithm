import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int m, d, daySum = 0;
        int days[] = {31,28,31,30,31,30,31,31,30,31,30,31};
        m = sc.nextInt();
        d = sc.nextInt();

        for(int i = 1; i<m; i++)
            daySum += days[i-1];
        daySum += d;
        switch(daySum%7){
            case 0 : System.out.println("SUN");break;
            case 1 : System.out.println("MON");break;
            case 2 : System.out.println("TUE");break;
            case 3 : System.out.println("WED");break;
            case 4 : System.out.println("THU");break;
            case 5 : System.out.println("FRI");break;
            case 6 : System.out.println("SAT");break;
        }
    }
}
