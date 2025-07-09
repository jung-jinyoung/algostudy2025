N = int(input())
a = dict()
b = []
cnt = 0
for i in range(N):
    a[input()] = i
for j in range(N):
    b.append(a[input()])
for k in range(N):
    for l in range(k + 1, N):
        if b[k] > b[l]:
            cnt  += 1
            break
print(cnt)