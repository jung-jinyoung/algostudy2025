def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x: (x[col-1],-x[0]))
    for r in range(row_begin, row_end+1):
        answer ^= sum(map(lambda x:x%r,data[r-1]))
    return answer