import java.util.*;
import java.io.*;
class Main{
    static int n,m;// 처음,다음
    static String[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str1 = br.readLine();
        String str2 = br.readLine();
        n = str1.length(); m= str2.length();

        dp = new String[n+1][m+1];

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                dp[i][j] = "";
            }
        }

        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (str1.charAt(i) == str2.charAt(j)){
                    dp[i+1][j+1] = dp[i][j] + str1.charAt(i);
                    continue;
                }
                if (dp[i][j+1].length() > dp[i+1][j].length()){
                    dp[i+1][j+1] = dp[i][j+1];
                } else{
                    dp[i+1][j+1] = dp[i+1][j];
                }
            }
        }
        System.out.println(dp[n][m]);
//        for (String[] d: dp){
//            System.out.println(Arrays.toString(d));
//        }
        }
    }
