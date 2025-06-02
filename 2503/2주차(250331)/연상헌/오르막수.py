N = int(input())
arr = [[] for _ in range(N + 1)]
arr[1] = list([1] * 10)
for i in range(2, N + 1):
    for j in range(10):
        arr[i].append(sum(arr[i - 1][j:]))
print((sum(arr[-1]) % 10007))