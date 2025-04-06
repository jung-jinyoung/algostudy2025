K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))
s = 1
e = 2**31 - 1
res = 0
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for a in range(K):
        cnt += (arr[a] // mid)
    if cnt >= N:
        res = mid
        s = mid + 1
    else:
        e = mid - 1
print(res)

