import sys

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))  # n 개 서비스 최소 300 최대 900,
    res = 0

    arr = sorted(arr)
    num = 0
    l, r = 0, n - 1
    for i in range(n):
        if arr[i] == 300:
            num += 1
            l = i + 1
        else:
            break
    k, v = divmod(num, 3)  # 몫, 나머지
    # print('here',k,v)
    res += k
    l -= v
    for j in range(n - 1, -1, -1):
        if arr[j] == 900:
            res += 1
            r = j - 1
        else:
            break
    # print('l:',l,'r',r)
    while 0 <= l <= r < n:
        if (arr[l] + arr[r]) > 900:
            res += 1
            r -= 1
        else:
            res += 1
            l += 1
            r -= 1

    print(res)
