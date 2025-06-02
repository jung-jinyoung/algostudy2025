import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
ans = [3000000000,0,0,0]
for i in range(n-1):
    l,r = i+1,n-1
    while l<r:
        tmp = arr[l] + arr[r] + arr[i]
        if abs(tmp) < abs(ans[0]):
            ans = [tmp,arr[i],arr[l],arr[r]]

        if tmp == 0:
            break
        elif tmp>0:
            r-=1
        else:
            l+=1
print(ans[1],ans[2],ans[3])