import java.util.*;

class Solution {   
    public int solution(int N, int number) {
        Set<Integer>[] dp = new HashSet[9];
        for (int i=1; i<9; i++){
            dp[i] = new HashSet<>();
        }
        
        dp[1].add(N); // 1번 씀 
        if (N == number) return 1;
        
        for (int i=2; i<9; i++){
            
            int res = func(N,i);
            dp[i].add(res);
            if (res == number) return i;
            
        // dp[i] 에 j와 i-j 계산한거 넣어주기
            for (int j=1; j<i; j++){
                for (int x: dp[j]) {
                    for (int y: dp[i-j]){
                        dp[i].add(x-y);
                        if ((x-y) == number) return i;
                        dp[i].add(x+y);
                        if ((x+y) == number) return i;
                        dp[i].add(x*y);
                        if ((x*y) == number) return i;
                        dp[i].add(y-x);
                        if ((y-x) == number) return i;
                        if (x !=0){
                            dp[i].add(y/x);
                            if ((y/x) == number) return i;
                        }
                        if (y!=0){
                            dp[i].add(x/y);
                            if ((x/y) == number) return i;
                        }
                        
                        
                    }
                    
                }
                
            }
            
        }
        return -1;
    }
    static int func(int N,int num){
        return Integer.parseInt(String.valueOf(N).repeat(num));
    }
    
}