import java.util.*;
public class Fibon {
    public static void main(String[] args){
        int n, a = 0, b = 1, c;
        Scanner s = new Scanner(System.in);
        System.out.print("Enter value of n:");
        n = s.nextInt();
        System.out.print("Fibonacci Series:");
        for(int i = 1; i <= n; i++) {
            System.out.print(a+" ");
            c = a + b;
            a = b;
            b = c;
        }
    }
}
