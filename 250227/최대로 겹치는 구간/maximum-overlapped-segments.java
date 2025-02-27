import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] num = new int[201]; // 좌표 범위 -100 ~ 100을 0 ~ 200으로 변환하여 저장

        for (int i = 0; i < n; i++) {
            int x1 = sc.nextInt();
            int x2 = sc.nextInt();

            // 해당 구간에 대한 카운트 증가
            for (int j = x1; j < x2; j++) { // 끝점 x2는 포함되지 않음
                num[j + 100]++; // 음수를 0 기반 인덱스로 변환
            }
        }

        // 배열에서 최대 겹치는 개수 찾기
        int maxOverlap = 0;
        for (int i = 0; i < 201; i++) {
            maxOverlap = Math.max(maxOverlap, num[i]);
        }

        System.out.println(maxOverlap);
        sc.close();
    }
}
