import java.util.Scanner;
public class Fact {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);        
        System.out.print("Enter a non-negative integer: ");
        int n = scanner.nextInt();
        if (n < 0) {
            System.out.println("Invalid input. Please enter a non-negative integer.");
        } else {
            long factorial = calculateFactorial(n);
            System.out.println("The factorial of " + n + " is: " + factorial);
        }
    }

    private static long calculateFactorial(int n) {
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}