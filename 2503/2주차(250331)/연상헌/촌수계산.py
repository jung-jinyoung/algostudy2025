from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    c, d = map(int, input().split())
    arr[c].append(d)
    arr[d].append(c)
def bfs(a, b):
    q = deque([(a, 0)])
    visited = []

    while q:
        now, cnt = q.popleft()
        if now == b:
            return cnt
        for i in arr[now]:
            if i not in visited:
                visited.append(i)
                q.append((i, cnt + 1))
    return -1

print(bfs(a, b))