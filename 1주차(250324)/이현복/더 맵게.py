import heapq
def solution(scoville, K):
    f = len(scoville)
    scoville.sort()
    if K==0:
        return 0
    while scoville:
        a = heapq.heappop(scoville)
        if a>=K:
            return f-len(scoville)-1
        else:
            if scoville:
                b = heapq.heappop(scoville)
                heapq.heappush(scoville,a+b*2)
            else:
                return -1