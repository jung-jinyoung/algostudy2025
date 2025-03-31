'''
대근: 들어가는 순서
영식: 나오는 순서

추월이 문제

'''
from collections import deque
n = int(input())
in_order = deque([input() for _ in range(n)])
out_order = deque([input() for _ in range(n)])

cnt = 0
while out_order:
    outcar = out_order.popleft()
    waiting = deque([])
    check = False
    while in_order:
        incar = in_order.popleft()
        if incar == outcar:
            break
        else:
            check = True
            waiting.append(incar)
    waiting.extend(in_order)
    in_order = waiting
    if check:
        cnt+=1
print(cnt)



