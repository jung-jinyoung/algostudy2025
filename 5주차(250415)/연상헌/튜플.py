def solution(s):
    answer = []
    arr = dict()
    for i in range(1, len(s) - 1):
        if s[i] == '{':
            p = i + 1
        elif s[i] == '}':
            a = set(map(int, s[p:i].split(",")))
            length = len(a)
            arr[length] = a
    res = set()
    for j in range(1, len(arr.keys()) + 1):
        a = arr[j] - res
        aa = list(a)[0]
        res = res.union(a)
        answer.append(aa)
    return answer