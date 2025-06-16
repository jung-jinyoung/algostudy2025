from collections import deque


def solution(progresses, speeds):
    answer = []
    #   맨 앞에있는놈이 완료되면 뒤에 애들까지 전부 확인해서 처리함
    q = deque(progresses)
    sq = deque(speeds)
    while q:
        cnt = 0
        while q and q[0] >= 100:
            q.popleft()
            sq.popleft()
            cnt += 1
        if cnt:
            answer.append(cnt)
        for i in range(len(q)):
            q[i] += sq[i]

    return answer
