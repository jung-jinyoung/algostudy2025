import heapq as hq
from collections import defaultdict

def solution(tickets):
    answer = []
    apt = defaultdict(list)
    for dep, arr in tickets:
        hq.heappush(apt[dep], arr)
    def f(s):
        while apt[s]:
            a = hq.heappop(apt[s])
            f(a)
        answer.append(s)
    f("ICN")
    answer = answer[::-1]
    return answer