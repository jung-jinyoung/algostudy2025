def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    S = []
    for i in range(1, len(data) + 1):
        tmp = 0
        for d in data[i - 1]:
            tmp += d % i
        S.append(tmp)
    S = S[row_begin - 1 : row_end]
    before = S.pop()
    while S:
        top = S.pop()
        before = before ^ top
    answer = before
    return answer
