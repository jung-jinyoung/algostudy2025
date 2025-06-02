import sys
input = sys.stdin.readline

from collections import deque
n = int(input())
a,b = map(int,input().split())
arr = [[] for _ in range(n)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    arr[x-1].append(y-1)
    arr[y-1].append(x-1)
q = deque()
q.append((a-1,0))
ans = -1
fin = [-1]*n
fin[a-1] = 0

while q:
    node,l = q.popleft()
    if arr[node]:
        for i in arr[node]:
            if i == b-1:
                ans = l+1
                q = 0
                break
            else:
                if fin[i]>l+1 or fin[i]==-1:
                    fin[i] = l + 1
                    q.append((i,l+1))
print(ans)