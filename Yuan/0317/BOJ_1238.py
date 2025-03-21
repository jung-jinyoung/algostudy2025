'''
n명, m개 도로, x(마을 번호)
m줄동안 t 시간
도로 한개
시작, 끝, t시간

n 개의 노드가 있음, n에서 출발해서 x찍고 돌아오는 최소경로
단방향 도로, 중복가능

# 다익스트라임
'''
import heapq

n, m,x = map(int,input().split())
graph = [ [] for _ in range(n+1)]
# print(graph) i부터 n까지 가는길 값 저장
for _ in range(m):
    s,e,c = map(int,input().split())
    graph[s].append((c,e))
# print(graph)

diks = [[]]
# node 1부터 n까지 확인 해야함
for start in range(1,n+1):
    dis = [1e9 for _ in range(n+1)]
    dis[0], dis[start] = 0,0
    heap = [(0,start)]
    # cos,now = 0,1번
    while heap:
        cos, now = heapq.heappop(heap)
        # 꺼낸 값이 크면 무시
        if cos > dis[now]:
            continue

        for nxc, nxt in graph[now]:
            if cos + nxc < dis[nxt]:
                dis[nxt] = cos+nxc
                heapq.heappush(heap,(cos+nxc,nxt))

    diks.append(dis)
# print(diks)
res = 0
for i in range(1,n+1):
    r = diks[i][x] + diks[x][i]
    if r>res:
        res = r
print(res)