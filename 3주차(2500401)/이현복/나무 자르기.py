from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
low, high = 0, arr[-1]
ans = 0
while low <= high:
    mid = (low + high) // 2
    cut = sum((tree - mid) for tree in arr if tree > mid)
    if cut >= M:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)