import sys

input = sys.stdin.readline
n, m = map(int, input().split()) # N: 나무갯수 M: 필요 나무길이
arr = list(map(int, input().split()))
arr.sort()
s = 0
e = arr[-1]
res = 0
while s <= e:
    namu = 0
    mid = (s + e) // 2
    for i in range(n):
        if arr[i] > mid:
            namu += arr[i] - mid
    if namu >= m:
        res = mid
        s = mid + 1
    else:
        e = mid - 1
print(res)