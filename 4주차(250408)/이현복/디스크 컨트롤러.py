import heapq
def solution(jobs):
    pq = []  # 소요시간 작은, 요청시각 빠른, 작업번호 작은
    total_time = 0
    lll = len(jobs)
    for i in range(lll):
        jobs[i].append(i)
    jobs.sort()
    t = 0
    pointer = 0
    while pointer < lll or pq:
        while pointer < lll and jobs[pointer][0] <= t:
            s, l, i = jobs[pointer]
            heapq.heappush(pq, (l, s, i))
            pointer += 1

        if pq:
            L, S, I = heapq.heappop(pq)
            t += L
            total_time += (t - S)
        else:
            t += 1

    return total_time // lll