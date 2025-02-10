import java.io.BufferedReader;
import java.io.InputStreamReader;

public class P28702_FizzBuzz {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long answerNum = 0;
        for (int i = 0; i < 3; i++){
            String input = br.readLine();
            if (Character.isDigit(input.charAt(0))) {
                long num = Long.parseLong(input);
                answerNum = num + (3 - i);
                break;
            }
        }
        if ((answerNum % 5 == 0) && (answerNum % 3 == 0))
            System.out.println("FizzBuzz");
        else if (answerNum % 3 == 0)
            System.out.println("Fizz");
        else if (answerNum % 5 == 0)
            System.out.println("Buzz");
        else
            System.out.println(answerNum);
    }
}