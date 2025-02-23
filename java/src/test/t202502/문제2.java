package test.t202502;

public class 문제2 {

    public static void main(String[] args) {
        System.out.println(solution(9));
    }

    public static long solution(long n) {
        // n <= 2^k인 k 구하기
        int k = 0;
        while (n > Math.pow(2, k)) {
            k++;
        }
        // 3^(k-1) 에
        if (n == (int) Math.pow(2, k)) {
            return (int) Math.pow(3, k);
        } else {
        long[] subs = getSubs(k - 1);
        int index = (int) (n - (long) Math.pow(2, k));
        System.out.println(index);
//        for (long c : subs) {
//            System.out.print(c + " ");
//        }
//        System.out.println();
        return (long) Math.pow(3, k-1) + subs[index];
        }
    }

    // 3^0, 3^1, 3^0+3^1, 3^2, 3^0+3^2, 3^1+3^2, 3^0+3^1+3^2, ..., 3^0+...3^max 배열 반환
    public static long[] getSubs(int max) {
        int total = (int) Math.pow(2, max); // 집합 개수
        long[] result = new long[total];

        for (int i = 0; i < total; i++) {
            long sum = 0;
            int index = i;
            for (int j = 0; j < max; j++) {
                if (index % 2 == 1) {
                    sum += Math.pow(3, j);
                }
                index /= 2;
            }
            result[i] = sum;
        }

        return result;
    }
}
