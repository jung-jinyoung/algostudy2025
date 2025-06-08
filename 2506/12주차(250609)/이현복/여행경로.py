from collections import defaultdict

def solution(tickets):
    answer = []
    D = defaultdict(list)
    for f, t in tickets:
        D[f].append(t)
    for key in D.keys():
        D[key].sort(reverse=True)
    print(D)

    def dfs(now):
        while D[now]:
            dfs(D[now].pop())
        answer.append(now)

    dfs("ICN")
    return answer[::-1]
