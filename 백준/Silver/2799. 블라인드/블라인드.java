import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        int n = sc.nextInt();
        String[] wndw = new String[5 * m + 1];
        for (int i = 0; i < 5 * m + 1; i++) {
            String str = sc.next();
            wndw[i] = str;

        }

        int[] kinds = new int[5];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int cnt = 0;
                for (int k = 0; k < 4; k++) {
                    if (wndw[5 * i + k + 1].charAt(5 * j + 2) == '.') {
                        break;
                    }
                    cnt++;
                }
                kinds[cnt]++;
            }
        }
        for (int kind : kinds) System.out.print(kind + " ");
    }
}
