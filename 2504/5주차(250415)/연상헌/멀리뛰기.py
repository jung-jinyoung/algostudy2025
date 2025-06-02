def solution(n):
    answer = 0
    # dp = [[] for _ in range(n + 1)]
    # dp[1].append([1])
    # dp[2].append([1, 1])
    # dp[2].append([2])
    # if n >= 3:
    #     for i in range(3, n + 1):
    #         for j in dp[i - 1]:
    #             dp[i].append(j + [1])
    #         if i % 2 == 0:
    #             dp[i].append(dp[i - 2][-1] + [2])
    # for k in dp[n]:
    #     answer += len(set(permutations(k, len(k))))
    #     answer %= 1234567
    arr = [0]
    arr.append(1)
    arr.append(2)
    if n >= 3:
        for i in range(3, n + 1):
            arr.append(arr[i - 2] + arr[i - 1])
    answer = arr[n] % 1234567
    return answer