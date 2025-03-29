import sys

input = sys.stdin.readline

n = int(input())

# 길이가 i 일 때 끝자리수들의 dp 
dp = [ [0] * 10 for _ in range(n+1)]

# 길이가 1일 때 경우의 수 저장
for j in range(10):
    dp[1][j] = 1
    
# 길이가 2 이상일 경우의 dp 저장
for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = sum([dp[i-1][k] for k in range(j+1)])

print(sum(dp[n]) % 10007)
    
    