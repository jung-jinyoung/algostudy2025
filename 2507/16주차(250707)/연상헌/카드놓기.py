from collections import deque

n = int(input())
arr = list(map(int, input().split()))
card = list(range(1, n+1))
origin = deque()

for i in range(n):
    if arr[n-1-i] == 1:
        origin.appendleft(card[i])
    elif arr[n-1-i] == 2:
        origin.insert(1, card[i])
    elif arr[n-1-i] == 3:
        origin.append(card[i])
for j in origin:
    print(j, end=' ')