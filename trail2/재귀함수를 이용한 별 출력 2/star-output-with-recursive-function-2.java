import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        boolean isZero = false;
        dfs(n, isZero, n);
    }

    public static void dfs(int num, boolean isZero, int n) {
        if (isZero && num > n) {
            return;
        }

        if (num == 0) {
            isZero = !isZero;
            num++;
        }

        for (int i = 0; i < num; i++) {
            System.out.print("* ");
        }
        System.out.println();

        if (!isZero) {
            dfs(num - 1, isZero, n);
        } else {
            dfs(num + 1, isZero, n);
        }
    }
}