import heapq

def solution(n, k, enemy):
    answer = 0
    hq = []
    if len(enemy) <= k:
        return len(enemy)
    for i in range(len(enemy)):
        heapq.heappush(hq, enemy[i])
        if len(hq) > k:
            a = heapq.heappop(hq)
            if a > n:
                return i
            n -= a
    answer = len(enemy)
    return answer