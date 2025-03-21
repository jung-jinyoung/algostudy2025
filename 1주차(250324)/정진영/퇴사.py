# 이전엔 역순 dp로 해결해서 다르게 풀었습니다.

import sys

input = sys.stdin.readline
N = int(input())
T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N+1)

for i in range(N):
    # 상담 진행 
    if (i + T[i] <=N):
        dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])
    # 상당 진행 X
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[-1])   