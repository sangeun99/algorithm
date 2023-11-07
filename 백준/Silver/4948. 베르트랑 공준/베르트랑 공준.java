import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int n = sc.nextInt();
            if (n == 0)
                break;
            // n보다 크고 2n보다 작거나 같은 소수의 개수
            int count = 0;
            if (n == 1)
                count = 1;
            else if (n == 2)
                count = 1;
            for (int i = n + 1; i <= 2 * n; i++){
                // i가 소수일 때 count++
                for (int j = 2; j <= Math.sqrt(i); j++){
                    if (i % j == 0)
                        break;
                    else if (j == (int)Math.sqrt(i)) {
                        count++;
                    }
                }
            }
            System.out.println(count);
        }
    }
}
