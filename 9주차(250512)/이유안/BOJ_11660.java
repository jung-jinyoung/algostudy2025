import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main{
    static int n,m;
    static int[][] map;
    static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String inputs[] = br.readLine().split(" ");
        n = Integer.parseInt(inputs[0]);
        m = Integer.parseInt(inputs[1]);
        map = new int[n][n];
        for (int i=0; i<n; i++){
            String inputs2[] = br.readLine().split(" ");
            for (int j=0; j<n; j++){
                map[i][j] = Integer.parseInt(inputs2[j]);
            }
        }

        dp = new int[n][n];
        dp[0][0] = map[0][0];
        // dp 넣기: 위 + 옆 - 대각선
        for (int x = 0; x <n; x++){
            for (int y = 0; y <n; y++){
                if (dp[x][y] !=0) continue;
                dp[x][y] +=map[x][y];
//                int s = 0;
                // 위, 옆, 대각선앞
                int[] o1 = new int[]{x -1, y};
                int[] o2 = new int[]{x, y -1};
                int[] o3 = new int[]{x -1, y -1};
                // dp[x][y] 가 0 아니고
                if (0<=o1[0] && o1[0]<n && 0<=o1[1] && o1[1]<n){
                    dp[x][y] += dp[o1[0]][o1[1]];
                }
                if (0<=o2[0] && o2[0]<n && 0<=o2[1] && o2[1]<n){
                    dp[x][y] += dp[o2[0]][o2[1]];
                }
                if (0<=o3[0] && o3[0]<n && 0<=o3[1] && o3[1]<n){
                    dp[x][y] -= dp[o3[0]][o3[1]];
                }

            }
        }
        //  찾기
        for (int i=0; i<m; i++){
            String[] ip3 = br.readLine().split(" ");
            int x1 = Integer.parseInt(ip3[0])-1;
            int y1 = Integer.parseInt(ip3[1])-1;
            int x2 = Integer.parseInt(ip3[2])-1;
            int y2 = Integer.parseInt(ip3[3])-1;
            int s = dp[x2][y2];

            if (0<=x1-1 && x1-1<n){
                s-=dp[x1-1][y2];
            }

            if (0<=y1-1 && y1-1<n){
                s-=dp[x2][y1-1];
            }

            if (0<=x1-1 && x1-1<n && 0<=y1-1 && y1-1<n){
                s+=dp[x1-1][y1-1];
            }

            System.out.println(s);
        }


    }
}