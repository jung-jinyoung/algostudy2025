def solution(n):
    if n == 1 : 
        return 1
    if n == 2 : 
        return 2
    
    answer = 0
    dp = [0]*(n+1)
    mod = 1234567
    
    dp[1] = 1 # 1번에 갈 수 있는 경우
    dp[2] = 2 # 2번에 갈 수 있는 경우
    
    for i in range (3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % mod
        
    return dp[n]