import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class 행렬곱셈순서 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(reader.readLine()); // 행렬 개수
        int[][] M = new int[N][2]; // 각 행렬의 크기를 저장할 배열

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine());
            M[i][0] = Integer.parseInt(st.nextToken()); // 행
            M[i][1] = Integer.parseInt(st.nextToken()); // 열
        }

        int[][] dp = new int[N][N]; // 최소 비용을 저장할 DP 배열
        int[][][] matrix = new int[N][N][2]; // 각 구간의 행렬 크기를 저장할 배열 .. 여기서 tuple 이 안되니까.. array로 해결하는 구나...

        // 초기화
        for (int i = 0; i < N; i++) {
            matrix[i][i][0] = M[i][0];
            matrix[i][i][1] = M[i][1];
            dp[i][i] = 0; // 자기 자신으로의 곱셈 비용은 0
        }

        // DP를 이용한 행렬 곱셈 최소 비용 계산
        for (int step = 1; step < N; step++) {
            for (int i = 0; i < N - step; i++) {
                int j = i + step;
                dp[i][j] = Integer.MAX_VALUE;
                for (int m = i; m < j; m++) {
                    int[] matrix1 = matrix[i][m];
                    int[] matrix2 = matrix[m + 1][j];
                    int cost = matrix1[0] * matrix1[1] * matrix2[1];
                    dp[i][j] = Math.min(dp[i][j], dp[i][m] + dp[m + 1][j] + cost);
                    matrix[i][j][0] = matrix1[0];
                    matrix[i][j][1] = matrix2[1];
                }
            }
        }

        System.out.println(dp[0][N - 1]); // 최소 비용 출력
    }
}
