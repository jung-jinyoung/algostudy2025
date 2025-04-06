import heapq as hq
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
jews = []
for _ in range(N):
    M, V = map(int, input().split()) # M: 무게, V: 가격
    jews.append([M, V])
jews.sort()
bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()
res = 0
arr = []
j = 0
for i in bags:
    while j < N:
        if i >= jews[j][0]:
            hq.heappush(arr, -jews[j][1])
            j += 1
        else:
            break
    if arr:
        res -= hq.heappop(arr)
print(res)