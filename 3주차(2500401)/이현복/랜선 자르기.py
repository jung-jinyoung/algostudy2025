from sys import stdin

input = stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
l, r = 1, max(arr)

while l <= r:
    mid = (l + r) // 2
    lan = sum(arr[i] // mid for i in range(K))
    if lan < N:
        r = mid - 1
    else:
        ans = mid
        l = mid + 1

print(ans)