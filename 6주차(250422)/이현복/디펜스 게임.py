import heapq
def solution(n, k, enemy):
    answer = 0
    stages = len(enemy)
    if sum(enemy)<=n:
        return stages
    else:
        pq = []
        for idx,E in enumerate(enemy):
            heapq.heappush(pq,-E)
            n-=E
            if n<0 and k>0:
                n -= heapq.heappop(pq)
                k-=1
            if n<0:
                return idx
        else:
            return stages