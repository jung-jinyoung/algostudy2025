import sys
from collections import deque

# input 파일에서 입력 받을 때 사용
# sys.stdin = open('input.txt', 'r')

N, M, K, X = map(int, input().split())

# 도로 정보 입력
roads = [tuple(map(int, input().split())) for _ in range(M)]

# 인접 리스트로 그래프 구성
graph = [[] for _ in range(N + 1)]
for a, b in roads:
    graph[a].append(b)

# 피라미드 구조: 거리(층) 별로 도시를 저장하는 이중 리스트
pyramid = [[] for _ in range(K + 1)]  # 0층부터 K층까지

visited = [False] * (N + 1)
visited[X] = True
pyramid[0].append(X)

# 거리 1부터 K까지 순차적으로 채우기
for level in range(K):
    for i in pyramid[level]:
        for j in graph[i]:
            if not visited[j]:
                visited[j] = True
                pyramid[level + 1].append(j)

# K층에 해당하는 도시 출력
result = pyramid[K]

if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)

"""
층 별로 배열을 생성해서
K-1 열에 위치한 도시를 출력하면 될듯?
최대 길이는 도로의 개수인 M이다.

"""

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

N, M, K, X = map(int, input().split())

roads = deque()
for _ in range(M):
    mom, son = map(int, input().split())
    roads.append((mom, son))

result = []

# 층별로 넣을 리스트
pyramid = [[] for _ in range(K + 1)]

# 첫 번쨰 시작노드 X 삽입
pyramid[0].append(X)

next = 1
for i in range(M):
    mom, son = roads.popleft()
    if mom == X:
        pyramid[next].append(son)
    # 부모 노드는 시작 노드와 다르지만 부모와 자식이 이미 같은 층에 있는 경우
    elif mom != X and son in pyramid[next] and mom in pyramid[next]:
        continue
    # 부모 노드와 시작 노드가 다르고 부모 노드는 피라미드에 있지만 자식 노드는 없는 경우
    elif mom != X and mom in pyramid[next] and son not in pyramid[next]:
        next += 1
        if next <= K:
            pyramid[next].append(son)

for city in pyramid[K]:
    result.append(city)

if result:
    result.sort()
    for city in result:
        print(city)
else:
    print(-1)
