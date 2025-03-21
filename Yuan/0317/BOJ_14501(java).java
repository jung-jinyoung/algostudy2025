import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] days = new int[n+1][2];

        for (int i=1; i<=n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());

            days[i][0] = t;
            days[i][1] = p;
        }

        int[] dp = new int[n+1];
        // 마지막날 먼저 채우기
        if (days[n][0] <=1) dp[n] = days[n][1];
        // 그 다음날부터 계산하기

        for (int j = n-1; j>0; j--){
            int t = days[j][0];
            int p = days[j][1];

            if ((j+t) == (n+1)){
                dp[j] = Math.max(dp[j+1],p);
                continue;
            }
            if ((j+t)>n) {
                dp[j] = dp[j+1];
                continue;
            }

            dp[j] = Math.max(dp[j+1], dp[j+t]+p);
        }

        System.out.println(dp[1]);

    }
}