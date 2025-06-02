'''
이분탐색 풀떄 

'''
from collections import deque
n = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)

now = float('inf')
res = []
for i in range(n-2):
    x = arr[i]
    # arr[i+1] 부터 arr[n-1] 중에 두개 합이 -x 찾기
    for j in range(i+1,n-1):
        y = arr[j]
        l,r = j+1,n-1
        # find(l,r,arr) -> arr중에 x+y+z가 0가까운거 찾기
        # z는 -y-x
        while l<=r:
            mid = (l+r)//2
            z = arr[mid]
            if abs(x + y + z) < now:
                now = abs(x + y + z)
                res = [x, y, z]

            if z > (-y-x):
                r = mid-1
            elif z < (-y-x):
                l = mid+1
            else:
                res = [x,y,z]
                print(*sorted(res))
                exit()


print(*sorted(res))



