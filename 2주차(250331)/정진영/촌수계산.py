import sys
from collections import deque 

input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

graph = [ [] for _ in range(n+1)]
# 촌수 계산을 위한 양방향 간선 그래프 생성
for _ in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

answer = -1

queue = deque()
visited = [False] * (n+1)
queue.append((p1, 0)) # 현재 노드와 촌수 
visited[p1] = True

while queue:
    curr, dist = queue.popleft()
    if curr == p2 :
        answer = dist
        break
    
    for neighbor in graph[curr]:
        if (not visited[neighbor]) :
            visited[neighbor] = True
            queue.append((neighbor, dist+1))
        
print(answer)
