import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int []num= new int[N];
        for (int i = 0; i < K; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();

            for(int j=A-1;j<B;j++){
                num[j]++;
            
            }
        }

        int max = num[0];
        for (int i = 1; i < N; i++) {
            if (num[i] > max) {
                max = num[i];
            }
        }

        System.out.println(max);
        }
}