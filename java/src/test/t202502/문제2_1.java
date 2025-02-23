package test.t202502;

public class 문제2_1 {

    public static long solution(long n) {
        long anwer = 0;
        long curPow = 1;

        while (n > 0) {
            if (n % 2 == 1) {
                anwer += curPow;
            }
            curPow *= 3;
            n /= 2;
        }

        return anwer;
    }

    public static void main(String[] args) {
        long n = 15;
        System.out.println(solution(n));
    }
}
