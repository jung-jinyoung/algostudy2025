from heapq import heappush, heappop

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
reverse = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    # 각각 도착점과 걸린 시간 연결 
    graph[s].append((e, t))
    # x->i로의 정보 저장
    reverse[e].append((s, t))
    

def dikstra(graph, start , n) :
    # 노드별 거리 초기화 
    nodes = {node: float('inf') for node in range(1, n+1)}
    queue = []

    # 시작점 초기화
    nodes[start] = 0
    heappush(queue, (start, nodes[start]))
    
    while queue:
        node, distance = heappop(queue)
        if distance > nodes[node] :
            continue
            
        for neighbor in graph[node] :
            ne, nt = neighbor
            next_distance = distance + nt
            if next_distance < nodes[ne] :
                nodes[ne] = next_distance
                queue.append((ne, next_distance))
        
    
    return nodes

from_x = dikstra(graph, x, n)
to_x = dikstra(reverse, x, n)

max_answer = 0
for i in range(1, n+1):
    if (i == x):
        continue
    temp = from_x[i] + to_x[i]
    max_answer = max(max_answer ,temp)
print(max_answer)