def solution(n, computers):
    def find(x):
        while x != p[x]:
            x = p[x]
        return x

    def union(a, b):
        p[find(b)] = find(a)

    ans = 0
    p = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                union(i, j)
    print(p)
    for i in range(n):
        if p[i] == i:
            ans += 1
    return ans