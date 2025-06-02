N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = [1000000000, 1000000000, 1000000000]
for i in range(N):
    j = i + 1
    k = N - 1
    while j < k:
        if abs(arr[i] + arr[j] + arr[k]) < abs(sum(result)):
            result = [arr[i], arr[j], arr[k]]
        if arr[i] + arr[j] + arr[k] > 0:
            k -= 1
        elif arr[i] + arr[j] + arr[k] < 0:
            j += 1
        else:
            break
print(result)