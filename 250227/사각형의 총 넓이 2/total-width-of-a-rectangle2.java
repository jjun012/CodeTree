import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        boolean[][] grid = new boolean[201][201]; // 좌표 범위: -100 ~ 100 -> 0 ~ 200으로 변환

        for (int i = 0; i < n; i++) {
            int x1 = sc.nextInt() + 100;
            int y1 = sc.nextInt() + 100;
            int x2 = sc.nextInt() + 100;
            int y2 = sc.nextInt() + 100;

            // (x1, y1) ~ (x2, y2) 영역을 true로 설정
            for (int x = x1; x < x2; x++) {
                for (int y = y1; y < y2; y++) {
                    grid[x][y] = true;
                }
            }
        }

        // 총 넓이 계산
        int area = 0;
        for (int x = 0; x < 201; x++) {
            for (int y = 0; y < 201; y++) {
                if (grid[x][y]) {
                    area++;
                }
            }
        }

        System.out.println(area);
        sc.close();
    }
}
