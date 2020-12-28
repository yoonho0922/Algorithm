package Baek10817;

import java.io.IOException;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int a[] = new int[3];
        int tmp;
        a[0] = sc.nextInt();
        a[1] = sc.nextInt();
        a[2] = sc.nextInt();

        for(int i = 0; i<2; i++){
            for(int j = 2; j>i; j--){
                if(a[j-1] < a[j]){
                    tmp = a[j-1];
                    a[j-1] = a[j];
                    a[j] = tmp;
                }
            }
        }
        System.out.println(a[1]);
    }
}
