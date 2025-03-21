'''

예외 처리 중요함
당일 날짜 + t 가 전체배열수n +1 인경우
최대값은 p or 날짜+1(내일) 이므로 예외 처리 해줘야함


n, t, p
1) n-n 일 >= t 여야함
2) 잔여일 있는지 없는지
    (1) t일 후의 값 + p
'''
n = int(input())
a = [ list(map(int, input().split())) for _ in range(n)]
days = [0]
days.extend(a)

dp = [0]*(n+1)

# 첫번쨰 dp 배열
if days[n][0] <=1:
    dp[n] = days[n][1]
    # dp[n+1] = days[n][1]

for i in range(n-1,0,-1): # i일
    t,p = days[i][0], days[i][1]
    if i+t-1>n:
        dp[i] = dp[i+1]
        continue # 넘으면 일못함
    if (i+t) == (n+1):
        dp[i] = max(p,dp[i+1])
        continue

    # print(i,'일',t,'소요',p,'값')
    dp[i] = max(dp[i+1],dp[i+t] + p)
    # print(dp)

# print(dp)
print(max(dp))
