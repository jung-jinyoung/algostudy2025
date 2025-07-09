n, a, b = map(int, input().split())

dp = [0] * (n + 1)
for i in range(1, n+1):
    dp[i] = dp[i - 1] + 1
    if i - 1 >= a:
        dp[i] = min(dp[i - 1 - a] + 1, dp[i])
    if i - 1 >= b:
        dp[i] = min(dp[i - 1 - b] + 1, dp[i])

print(dp[n])