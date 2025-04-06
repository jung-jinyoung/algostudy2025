import sys,heapq
input = sys.stdin.readline

N,K = map(int,input().split())
ans = 0
jewels = []
bags = []
for _ in range(N):
    m,v = map(int, input().split())
    jewels.append((m,v))
for _ in range(K):
    bags.append(int(input()))
bags.sort()
jewels.sort()
i=0
pq = []
for bag in bags:
    while i<N and bag>=jewels[i][0]:
        heapq.heappush(pq,-jewels[i][1])
        i+=1
    if pq:
        ans-=heapq.heappop(pq)
print(ans)