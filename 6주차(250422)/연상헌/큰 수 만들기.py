def solution(number, k):
    answer = ''
    q = []
    for i in number:
        while (k > 0) and q and (q[-1] < i):
            q.pop()
            k -= 1
        q.append(i)
    for j in range(len(q) - k):
        answer += q[j]
    return answer